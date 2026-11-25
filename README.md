# 80386 程序员参考手册 · 中文译本

在线地址：<https://stx-x.github.io/i386-manual-zh/>

《Intel 80386 Programmer's Reference Manual (1986)》的静态中文阅读站。保留原书章节结构、节号、图号与页码，提供全文检索、深浅色、响应式与打印样式。

## 快速开始

```bash
python3 build.py
python3 -m http.server 8000 --directory site
# 打开 http://localhost:8000
```

`build.py` 零第三方依赖，Python 3.9+ 即可；不需要 Node、npm 或任何前端工具链。

## 部署到 GitHub Pages

1. 把仓库推送到 GitHub，默认分支设为 `main`。
2. 仓库 **Settings → Pages → Build and deployment → Source** 选择 **GitHub Actions**。
3. 推送后 `.github/workflows/deploy.yml` 会自动构建 `site/` 并发布。

站点全部使用相对路径，因此既支持 `https://<user>.github.io/`，也支持 `https://<user>.github.io/<repo>/` 子路径，无需修改任何配置。

## 目录结构

```
.
├── build.py                 # 静态站点生成器（零依赖）
├── content/                 # 翻译源文件
│   ├── ch01/ … ch17/        # 每节一个 Markdown，front matter 记录节号/页码/锚点
│   ├── ins/                 # 94 条指令参考页
│   ├── app/                 # 附录 A–D
│   ├── glossary.md          # 术语对照表
│   └── about.md             # 关于本译本
├── assets/                  # 手写 CSS / JS / 图标
├── figures/                 # 原书插图（GIF）
├── source/                  # 英文底本镜像与清洗后的纯文本（构建时可不需要）
├── tools/                   # 底本解析、页码映射、指令页生成脚本
├── site/                    # 构建产物（GitHub Pages 发布目录）
└── .github/workflows/       # GitHub Actions 部署
```

## 内容与翻译说明

- 第 1–16 章逐段全译；第 17 章 17.1–17.2 全译。
- 94 条指令参考页均含中文标题、中文说明、中文异常条件；操作码表与操作伪代码保留原书编码形式，便于汇编核对。
- 附录 A–D 的说明文字翻译，操作码与标志位网格保留原书排版。
- 每节末尾标注原书印刷页码，便于与纸本或 PDF 核对。
- 术语表见 `content/glossary.md`，正文首次出现时采用「中文（English）」。

原文版权归 Intel Corporation 所有；本译本为非官方学习参考。译文部分采用 CC BY-NC 4.0。

## 构建细节

- Markdown 子集：标题、段落、列表、表格、围栏代码、引用、图片、`::: note/warn` 提示块。
- 检索索引在构建时写入 `site/assets/search.json`，浏览器端做中文 bigram + 英文词匹配，无后端依赖。
- 页面按章节聚合，节锚点形如 `ch/05.html#s05_02`，可直接分享。
- 打印时隐藏导航与侧栏，按 A4 排版，章节自动分页。
