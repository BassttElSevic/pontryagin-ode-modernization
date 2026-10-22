# 常微分方程 / Обыкновенные дифференциальные уравнения

**Л. С. 庞特里亚金 / Л. С. Понтрягин · 现代化重编**

这是庞特里亚金《常微分方程》的符号现代化项目。项目保留原书的章节结构、数学内容、定理与例题次序，改用现代线性代数和 ODE 记号，并以 TikZ 重绘插图。原书后置或省略的证明以补证单列，便于连续阅读与核对。

当前源码版本为 **`0.0.02`**，收录第一章（§1—§6）、第二章（§7—§16）及相关补证，共 38 张 TikZ 插图。后续从第三章 §17 起，按原书顺序逐章推进。

## 下载

最新 PDF 发布版本见 [GitHub Releases](https://github.com/BassttElSevic/pontryagin-ode-modernization/releases/latest)。

## 0.0.02 更新

- **电路图 7—16**：对照原扫描图重绘元件、节点与接线，修正电源极性、电流方向，以及电容被导线短接、端点错位等问题。
- **相空间与相平面图 17—38**：重绘直线与圆周上的平衡位置、环面、结点、鞍点、焦点、中心和退化情形。相图轨线按相应方程的参数解及仿射变换生成，运动方向与正文方程核对。
- **图 33 连续性**：修正斜坐标下的裁切边界，恢复完整的回折轨线。
- **尺寸与标注**：放大相图的几何尺寸，字母保持统一字号；调整标签位置，避免与轨线、坐标轴或箭头重叠。

本轮电路与相图修改已完成本地编译和成书页面检查。

## 内容与记号

- 用列向量、矩阵和 Jacobian 组织方程组，保留各节的条件、论证、例题和退化情形。
- 向量与矩阵使用**粗正体**：分别写作 `\vect{x}`、`\mat{A}`。向量值函数、初值、特征向量、向量解和矩阵多项式均遵循此约定；向量希腊字母也使用粗正体。
- 标量、标量分量 `x_i`、矩阵元素 `a_{ij}`、特征值、行列式和标量微分算子保持普通数学字体。`\vect{x}_i` 表示第 `i` 个完整向量解，与分量 `x_i` 区分。
- TikZ 插图对照原图保留数学用途与对应关系；轨线方向以正文方程为核对依据，原图箭头与方程矛盾时按方程校正。原扫描图的裁切图保留为参考资料。

当前收录范围和原书页码对应关系见 [SOURCE-MAP.md](SOURCE-MAP.md)。

## 插图

| 图号 | 内容 | 源码 |
| --- | --- | --- |
| 1—6 | 第一章的微分方程几何解释与力学模型 | `figures/01.tex`—`06.tex` |
| 7—16 | 基尔霍夫定律、元件符号、振荡回路、变压器和滤波器 | `figures/07.tex`—`16.tex` |
| 17—21 | 自治系统的相空间：直线、圆周与环面 | `figures/17.tex`—`21.tex` |
| 22—38 | 线性系统的相平面、仿射坐标变换与平衡位置分类 | `figures/22.tex`—`38.tex` |

正文直接载入 TikZ 源码；`assets/figures/` 中的扫描裁切图用于对照原书。相图使用 TikZ 的几何缩放扩大绘图范围，不启用 `transform shape`，也不对整幅图使用 `\resizebox`，使字母和下标保持正常字号。

## 封面

书名采用中俄双语：**常微分方程 / Обыкновенные дифференциальные уравнения**。作者署名为**列夫·谢苗诺维奇·庞特里亚金 / Лев Семёнович Понтрягин**；正文仍为中文现代化重编。

封面使用米白、朱红与黑色，以圆盘、红色楔形、倾斜格构和西里尔字母呼应苏联构成主义与俄国先锋派。圆盘中的曲线按稳定焦点系统的解绘制，下方为 `u = r - Kx` 的状态反馈回路。所有图形均为 LaTeX/TikZ 矢量源码，不使用位图；字体、颜色和页面图形分别在 `cover-style.tex` 与 `cover.tex` 中维护。

作者姓名核对依据：[Math-Net.Ru 作者条目](https://www.mathnet.ru/person21723)。俄文书名核对依据：[WorldCat 书目](https://search.worldcat.org/title/13273302)。封面为本项目新作，表达对原作者的敬意。

封面之后为同风格的独立人物介绍页，收录历史肖像、中文传记、生平年表与编者致意，并作为不编号章节列入目录。照片约摄于 1950 年，摄影者不详，Commons 文件页标注 CC BY 4.0；原文件、署名、许可及传记核对说明见 [照片与传记来源](assets/portraits/SOURCES.md)。正文引用莫斯科大学人物档案、MacTutor 与俄罗斯国立图书馆书目；致意文字为本项目原创。

## 目录

```text
main.tex                              主文档、版式与符号宏
cover.tex                             中俄双语构成主义封面，纯 TikZ 矢量绘制
cover-style.tex                       封面专用字体与配色
chapters/
  pontryagin-tribute.tex               封面之后的人物介绍与致敬页，不编号
  contents.tex                        正文章节清单
  frontmatter-modernization.tex       编写说明与当前进度
  chapter1.tex                        第一章正文
  chapter1-proofs.tex                 第一章补证
  chapter2-part1.tex                  第二章前半部
  chapter2-part2.tex                  第二章后半部
  chapter2-hurwitz-proof.tex          Hurwitz 判据补证
figures/01.tex ... 38.tex             38 张 TikZ 插图源码
assets/figures/                       原扫描插图裁切图，仅供参考
assets/portraits/                     历史肖像及照片许可、传记来源记录
scripts/build.py                     统一构建入口
build/                               PDF 与中间文件，构建生成，不提交
SOURCE-MAP.md                        原书页码与内容映射
LICENSE                              MIT 许可证
```

## 构建

需要 Python 3，以及可在命令行调用的 Tectonic 或 XeLaTeX。在项目根目录执行：

```sh
python scripts/build.py
```

默认使用 Tectonic。也可以指定 XeLaTeX：

```sh
python scripts/build.py --engine xelatex
```

Tectonic 首次构建会联网下载所需的 TeX 资源，后续复用本机缓存。若编译器未加入 `PATH`，可用 `--compiler` 指定其可执行文件路径；Windows 下也会自动查找当前用户的常见 Tectonic 安装位置。

XeLaTeX 环境需要安装 `ctex`、Fandol 字体、`amsmath`、`bm`、`upgreek`、TikZ 等文档所用的 TeX 包，以及 `fontspec` 和 TeX Live 的 `dejavu` 字体包。封面俄文使用 DejaVu Sans Condensed，按字体文件名加载；不依赖 Windows 专有字体。Tectonic 会按需下载对应字体资源。

使用编辑器中的 `latexmk` 构建方式时，还需安装 `latexmk`；仓库的 `.latexmkrc` 已配置 XeLaTeX 和 `build/` 输出目录。上面的 Python 构建入口不依赖 `latexmk`。

构建完成后，教材位于 `build/main.pdf`；目录、交叉引用和其他编译中间文件也写入 `build/`。此目录由构建生成，不纳入版本控制。构建只使用仓库内的文档、插图源码和构建脚本，不需要原扫描 PDF、OCR 文件或本机的其他项目目录。

## 发布 PDF

在 GitHub 创建并发布 Release 后，`Release PDF` 工作流会检出该 Release 标签，使用 Tectonic 构建 PDF，并将带版本号的 PDF 和 SHA-256 校验文件上传到同一个 Release。

仅推送 Git 标签不会触发 PDF 发布；需要在 GitHub 发布对应的 Release。

如需重新构建已有 Release，可在 Actions 中手动运行 `Release PDF`，并填写该 Release 的标签。手动运行会更新同名附件；它不会创建新的 Release。

## 继续编写

1. 在 `chapters/` 新建章节文件，例如 `chapter3.tex`，在章首使用 `\chapter{原书章名}`，按原书顺序保留节号、定理次序和对应内容。拆分章节时，仅在该章首个文件中使用 `\chapter`。
2. 在 `chapters/contents.tex` 中按顺序追加 `\input{chapters/chapter3.tex}`；补证文件同样列入章节清单。
3. 延续 `\vect`、`\mat` 的符号约定，逐项区分完整向量、向量分量和标量，尤其注意同名字母在不同语境中的含义。
4. 新增插图写入 `figures/NN.tex`，按原书图号继续编号。正文在 `figure` 环境内用 `\input{figures/39.tex}` 引入；放大相图时，在 `tikzpicture` 中设置 `scale` 并保持正常字号，不使用 `transform shape` 或整图 `\resizebox`。轨线和箭头应由同一方程或参数曲线生成，斜坐标下的裁切边界用显式顶点构造；编译后检查连续性、运动方向和标签间距。参考裁切图放入 `assets/figures/`，不作为正文插图的默认来源。
5. 更新编写说明中的进度和 `SOURCE-MAP.md`，运行统一构建命令，核对正文、目录、公式、交叉引用和插图。

## 许可与来源

本项目新增代码及作者有权许可的修改采用 [MIT 许可证](LICENSE)，版权所有 © 2026 Basstt ElSevic。

原书正文、原扫描资料与原扫描插图的权利仍归相应权利人所有。MIT 许可证不替这些原始资料声明版权，也不授予本项目作者无权授予的许可。TikZ 重绘的来源与原图对应关系记录在 `SOURCE-MAP.md`，重绘不改变原始资料的权利归属。
