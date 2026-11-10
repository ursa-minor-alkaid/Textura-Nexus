<h1 align="center">TexturaNexus: Project Structure & Content Organizer</h1>

<p align="center">
  <img src="https://img.shields.io/badge/version-0.5.0-blue" alt="version">
  <img src="https://img.shields.io/badge/update-2026.11.09-green" alt="update">
</p>

依据 PARA 思想整理项目文件夹结构与文件归属，对单个文件或选定的多个文件执行保守去重，对指定的大批量 AI 生成 Markdown 做语义压缩，并初始化文件追踪记录，维护 Word、PDF、Markdown、HTML 文件的项目文件树与变动记录。

## 功能

| # | 功能 | 说明 | 定义文件 |
| - | --- | --- | --- |
| 1 | 结构检查与初始化（structure） | 确认根 Area 主要文件夹与其下的 Project 附属文件夹；评估 Area 领域分类是否合理（仅建议，不修改）；阶段一按标准结构直接新建 `ai/`、`archives/`、`originals/`、`inbox/`、`assets/`、`resources/` 等文件夹，不移动任何文件；随后给出散落文件的归类意见，移动须确认后执行 | `references/texturanexus-organize.md` |
| 2 | 内容聚类整理（organize） | 对主要项目下的附属项目与散落文件聚类、分类，重点处理"项目文件夹或其余文件"部分；按逻辑归属、聚类、合理的文件夹嵌套设计结构；输出目标结构树与文件移动对照表，确认后执行移动 | `references/texturanexus-organize.md` |
| 3 | 内容去重（prune） | 在单个文件内部或选定的多个文件之间识别重复内容；按完全重复、近似重复、包含关系分层判定；阶段一汇报重复组明细与删除方案，不修改文件；阶段二只删除确认过的重复块，保留至少一处，其余内容零改动 | `references/texturanexus-prune.md` |
| 4 | 内容压缩（compress） | 仅对 AI 生成的大量 Markdown 做语义压缩，通常是 `ai/ai_outputs/` 下尚未审核的长文本；命名规则清晰、内容逻辑清楚、有人工修改审阅痕迹、组织良好的文件默认不处理，用户要求时先询问确认；必须先指定文件与压缩档位（轻度、标准、强力），未指定时先询问；阶段一给出逐节方案，不写文件；阶段二生成压缩版；单文件为 `{原文件名}-压缩版.md`，多文件合并时使用概括名称，原文件只读；代码、公式、表格、数字、引用、`<mark>`、安全警告不压缩 | `references/texturanexus-compress.md` |
| 5 | 文件追踪（filefollow） | 在项目根创建 `AGENTS.md` 与 `ai/memo-file_track`，写入记录规则与空表；只追踪 Word、PDF、Markdown、HTML 文件，扩展名不区分大小写；每次文件操作前读取 memo 文件树并与实际文件比对，差异补记入表；操作后追加记录并用新文件树覆盖旧文件树；用户要求删除文件时，删除成功后移除该文件相关的全部表格行，不保留删除记录；查询时只读 memo 汇报文件位置、状态与变动；已有内容不覆盖，向已有 `AGENTS.md` 追加规则段须确认 | `references/texturanexus-filefollow.md` |

## 项目组织标准

从大到小的层级：Area → Projects → files/docs。

- **Area**：长期投入的领域，只要仍然感兴趣就一直存在，如狭义的精神分析流派、德国古典哲学
- **Project**：有明确目标的具体组织，如复习并总结完某一本书
- **Files/Docs**：最小的执行与完成单元

Area 的划分不能过大也不能过小：直接分为"哲学""近现代哲学"属于过大；不做深入研究时把单个思想家（如"萨特"）单列为一个 Area 属于过小。

### 标准 Area 结构（主要项目）

```text
Area/
├── ai/               # 供 llm 使用的文件夹
│   ├── context/          # 提取过便于 llm 阅读的文件（.txt 或 .md）
│   ├── ai_outputs/       # llm 输出的未经审核的内容，经仔细审核的放入 resources 文件夹
│   ├── memo-file_track   # 文件变动与当前文件树（filefollow 初始化时创建）
│   └── 其余文件夹/         # 按需添加，一般为 ai 的工程文件
├── archives/         # 已归档内容、已结束项目
├── originals/        # 原始文件档案源头（如原始书籍扫描 pdf）
├── inbox/            # 输入的（未整理）资料
├── assets/           # 以图片为首的固定资源，可能还包括 tikz 代码、svg 等
├── resources/        # 常用资源
├── 附属项目文件夹、其余文件
├── AGENTS.md         # 供 AI agent 读取的项目规则（filefollow 初始化时创建）
├── README.md         # 需要分享时，供他人阅读
└── ROADMAP.md        # 给自己的待办事项
```

### 标准 Project 结构（附属项目）

附属项目不设立 `ai/`、`archives/`、`originals/`、`inbox/`，这部分内容统一放在所属的主要项目下，避免附属项目过于臃肿。Word、PDF、Markdown、HTML 文件的变动统一记录在所属主要项目的 `ai/memo-file_track` 中，不为单个附属项目单独维护追踪文件。

```text
Project/
├── assets/           # 以图片为首的固定资源，可能还包括 tikz 代码、svg 等
├── resources/        # 该项目的常用资源
├── 项目文件夹或其余文件
├── README.md         # 需要分享时，供他人阅读
└── ROADMAP.md        # 给自己的待办事项
```

## 使用

### 安装

- 将技能目录打包为 zip 后，上传到 Agent 客户端的技能上传/安装界面
- 或将 zip 直接发送给模型，由模型在客户端安装

### 在对话中激活

对模型说"整理这个文件夹"、"检查项目结构"、"把这个项目下的文件归类"、"删除这两篇笔记里的重复内容"、"初始化文件追踪"、"查看文件变动记录"等即可触发对应功能；技能入口与各功能的详细规范见 `SKILL.md` 与 `references/`

### 压缩 AI 生成的大量文本

对模型说“把 `ai/ai_outputs/long-note.md` 按标准档压缩”即可触发。必须同时给出具体文件与压缩档位；只给文件夹或未说明档位时，技能会先询问。

适用对象：AI 生成、尚未人工审阅、篇幅较长的 Markdown，通常是 `ai/ai_outputs/` 下的长文本。命名规则清晰、内容逻辑清楚、有人工修改审阅痕迹、组织良好的文件默认不压缩；用户明确要求时，技能会先说明判断依据并询问确认。

输出为同目录下的压缩版；单文件为 `{原文件名}-压缩版.md`，多文件合并时由方案给出一个简短、概括的名称并经确认，原文件保持不变。

三档强度：轻度保留全部章节与例子；标准删除弱例子、长背景和重复总结；强力只保留定义、机制、步骤、数据、警告与引用。

### 初始化与查询文件追踪

对模型说“初始化文件追踪”即可。技能会在项目根目录创建或补全 `AGENTS.md` 与 `ai/memo-file_track`，写入记录表与当前文件树。已有内容不覆盖；向已有 `AGENTS.md` 追加规则段前，会先展示内容并征求确认。

追踪范围仅限以下四类文件，扩展名不区分大小写：

| 类型 | 追踪的扩展名 |
| --- | --- |
| Word | `.doc`、`.docx`、`.docm`、`.dot`、`.dotx`、`.dotm` |
| PDF | `.pdf` |
| Markdown | `.md`、`.markdown`、`.mdown`、`.mkdn`、`.mkd`、`.mdwn`、`.mdtxt`、`.mdtext`、`.rmd`、`.qmd`、`.mdx` |
| HTML | `.html`、`.htm`、`.xhtml`、`.xht`、`.shtml`、`.shtm`、`.html5`、`.mhtml`、`.mht` |

其他类型不记录，也不出现在文件树中；`ai/memo-file_track` 自身不追踪、不显示。

初始化后，每次文件操作前，agent 读取 memo 中的文件树并与实际文件比对，发现差异先补记入表；操作完成后追加记录，并用新文件树覆盖旧文件树。

用户要求删除某个文件时，删除成功后 memo 中与该文件相关的全部行会被移除，包括移动、重命名前后的旧记录；不新增删除行。删除失败时保留原行。文件树同步移除该文件。

查询时说“某个文件在哪”“查看文件状态”或“查看文件变动记录”，技能读取 memo 汇报当前文件树与最近一次操作，不修改文件。

`ai/memo-file_track` 保持无扩展名，表头固定，不设时间列，记录先后由表格行的追加顺序体现。文件树只保留上述四类文件，并默认排除 `.git/`、`local/`、`node_modules/`、隐藏文件夹与符号链接。

## 安全约束

- `structure` 阶段一只新建标准结构要求的文件夹，不移动、重命名、删除、修改任何文件
- 文件移动、文件删除、重复内容删除与压缩写入都必须在用户明确确认后执行
- 不主动删除文件；`prune` 只删除文件内部的重复内容；用户明确要求删除文件时，删除成功后由 `filefollow` 清理相关记录
- 不重命名文件和文件夹；目标位置存在同名文件时暂停并反馈，不覆盖
- Area 领域分类的评估结论仅作建议，不据此执行拆分、合并或改名
- `prune` 中任何重复组至少保留一处；执行前核对内容，不一致时停止，不按行号盲删
- `compress` 只处理 AI 生成的大量文件；命名规则清晰、内容逻辑清楚、有人工修改审阅痕迹、组织良好的文件默认不处理
- 用户要求压缩上述文件时，必须先说明判断依据并询问确认；未确认不得写入压缩版
- `compress` 必须先确认具体文件与压缩档位，未指定时先询问
- `compress` 阶段一不写文件；阶段二只新建压缩版，原文件只读，不覆盖同名文件
- `compress` 不删除或改写代码、公式、表格、数字、引用、`<mark>`、安全警告
- `filefollow` 初始化只创建 `ai/`、`AGENTS.md`、`ai/memo-file_track`，不覆盖、不删除已有内容；向已有 `AGENTS.md` 追加规则段须经确认
- `filefollow` 只追踪 Word、PDF、Markdown、HTML 文件，扩展名不区分大小写；其他类型不记录、不比较、不出现在文件树中
- `filefollow` 只记录实际发生的文件操作与操作前比对发现的差异，不补写、不推测；仅新建文件夹不记录
- `filefollow` 在用户要求删除文件且删除成功后，移除该文件相关的全部表格行，不保留删除记录；删除失败时保留原行
- `filefollow` 不主动删除业务文件，只清理 memo 记录
- `filefollow` 的查询汇报只读 memo，不修改文件；文件树与记录表冲突时如实说明
- `AGENTS.md` 不能保证被所有 agent 软件读取；本技能在已初始化项目中主动执行记录

## 完整规范

- 技能入口与功能索引：`SKILL.md`
- 结构检查与聚类整理：`references/texturanexus-organize.md`
- 内容去重：`references/texturanexus-prune.md`
- 内容压缩：`references/texturanexus-compress.md`
- 文件追踪：`references/texturanexus-filefollow.md`
