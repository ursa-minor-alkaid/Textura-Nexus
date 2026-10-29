#!/usr/bin/env python3
"""读取一个或多个文件的创建时间与最后修改时间，以 JSON 输出，便于程序或 AI 批量调用比对。"""

import json
import os
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

EPOCH = datetime(1970, 1, 1, tzinfo=timezone.utc)


def ns_to_iso(ns: int) -> str:
    """纳秒时间戳转为带本地时区偏移的 ISO 8601 字符串。"""
    dt = (EPOCH + timedelta(microseconds=ns // 1000)).astimezone()
    return dt.isoformat(timespec="microseconds")


def collect(raw: str) -> dict:
    """收集单个文件的时间与大小；文件不存在或不可读时返回错误说明。"""
    path = Path(raw).expanduser().resolve()

    try:
        st = os.stat(path)
    except FileNotFoundError:
        return {"path": str(path), "exists": False, "error": "文件不存在"}
    except OSError as exc:
        return {"path": str(path), "exists": False, "error": str(exc)}

    created_ns = getattr(st, "st_birthtime_ns", None)
    if created_ns is None:
        # 非 Windows 平台上 st_ctime 是 inode 变更时间，不是创建时间
        created_ns = st.st_ctime_ns

    return {
        "path": str(path),
        "exists": True,
        "created": ns_to_iso(created_ns),
        "created_ns": created_ns,
        "modified": ns_to_iso(st.st_mtime_ns),
        "modified_ns": st.st_mtime_ns,
        "size": st.st_size,
    }


def main() -> int:
    if len(sys.argv) < 2:
        print(
            json.dumps(
                {"error": "用法: python file_time.py <文件路径> [更多文件路径...]"},
                ensure_ascii=False,
                indent=2,
            )
        )
        return 2

    files = [collect(arg) for arg in sys.argv[1:]]
    print(json.dumps({"count": len(files), "files": files}, ensure_ascii=False, indent=2))
    return 0 if all(item["exists"] for item in files) else 1


if __name__ == "__main__":
    sys.exit(main())
