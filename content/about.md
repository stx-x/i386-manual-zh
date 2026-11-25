# 关于本站

本站是《Intel 80386 Programmer's Reference Manual》的中文译本，底本为 Intel 公司 1986 年版，共 421 页。

全书保留原书的章、节编号与层级：17 章正文、94 条指令参考、4 个附录，并附 90 幅原书插图。每节末尾标注原书印刷页码，便于与纸本或 PDF 核对。

原文版权归 Intel Corporation 所有。本站为非官方、非商业性的学习参考，不替代原书；如版权方认为不妥，请联系删除。译文部分采用 [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/) 许可，转载注明出处即可。

## 技术实现

- 生成器：`build.py`，零第三方依赖的 Python 静态站点生成器；Markdown → HTML，自动生成目录、上下章、页码、检索索引。
- 检索：构建时导出 `assets/search.json`，浏览器端做中文二元组与英文词混合匹配，无需后端。
- 排版：自建 CSS，正文衬线、界面无衬线、代码等宽；支持浅色/深色、字号调节、阅读进度、图片放大与打印样式。
- 部署：`site/` 为纯静态产物，可直接部署到 GitHub Pages 或任意静态服务器。

## 构建

```bash
python3 build.py
python3 -m http.server 8000 --directory site
```

翻译源文件位于 `content/`：每章一个目录，每节一个 Markdown 文件，front matter 记录节号、标题、原书页码与锚点。修订后重新运行 `build.py` 即可。
