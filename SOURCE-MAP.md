# 庞特里亚金ODE现代化：来源映射与忠实性核对

原始依据：Л. С. 庞特里亚金《常微分方程》中文扫描本。
以下 PDF 页码按原扫描文件从 1 起计，与本项目排版后的 PDF 页码不同。
原扫描 PDF 与 OCR 文件不作为仓库构建依赖。

The scanned PDF has 283 pages. This project targets the entire book and expands
chapter by chapter. The current edition includes chapters 1 and 2, occupying PDF
pages 10-108, corresponding to printed pages 1-99. Later chapters will be added
to this map and to `chapters/contents.tex` as they are modernized.

## Chapter 1

| Section | Printed pages | PDF pages | Required material | Figures |
|---|---:|---:|---|---|
| §1 | 1-5 | 10-14 | first-order equation, solution interval, integral curve, direction field, exponential growth and decay | 1-2 |
| §2 | 5-11 | 14-20 | exact form, linear equation, constant variation, separable and ratio-homogeneous equations, nonuniqueness example | 3-4 |
| §3 | 11-15 | 20-24 | standard system, initial data, uniqueness, continuation, linear global existence | none |
| §4 | 15-21 | 24-30 | reduction of higher-order equations and systems, harmonic oscillator, spring, pendulum | 5-6 |
| §5 | 21-25 | 30-34 | complex-valued functions, complex system realification, complex exponential, examples | none |
| §6 | 25-26 | 34-35 | homogeneous superposition, affine solution set, superposition of forcing terms | none |

Proof placement:

- The statement order stays in chapter 1.
- Picard iteration, local uniqueness, continuation, and linear global existence
  are expanded in `chapters/chapter1-proofs.tex`.
- No body text may direct the reader to the original book for a missing proof.

## Chapter 2

| Section | Printed pages | PDF pages | Required material | Figures |
|---|---:|---:|---|---|
| §7 | 28-34 | 37-43 | characteristic polynomial, simple roots, real solutions, examples | none |
| §8 | 34-40 | 43-49 | repeated roots, shift formula, fundamental system, real solutions, examples | none |
| §9 | 40-44 | 49-53 | stable polynomials, quadratic/cubic criteria, Hurwitz theorem and examples | none |
| §10 | 45-49 | 54-58 | quasi-polynomials, theorem 8, undetermined coefficients, examples | none |
| §11 | 49-56 | 58-65 | polynomial matrix, adjugate elimination, solution classes, standardization | none |
| §12 | 56-60 | 65-69 | complex amplitudes, steady state, resonance | none |
| §13 | 60-71 | 69-80 | two-terminal elements, Kirchhoff laws, impedance, oscillator, transformer, filter | 7-16 |
| §14 | 71-79 | 80-88 | standard linear systems, simple spectrum, Jordan chains, variables transformation | none |
| §15 | 79-89 | 88-98 | autonomous systems, phase space, equilibria, periodic orbits, circle and torus examples | 17-21 |
| §16 | 89-99 | 98-108 | phase plane, nodes, saddle, focus, center, degenerate and zero-eigenvalue cases | 22-38 |

Proof placement:

- Hurwitz theorem is stated at its original location in §9.
- Its proof is expanded in `chapters/chapter2-hurwitz-proof.tex`.
- Chapter 2 ends at §16. §17 starts chapter 3 and will be included with that chapter.

## Notation migration

| Original usage | Modernized usage |
|---|---|
| one unknown function `x = phi(t)` | scalar `y(t)` or component `x_i(t)` |
| component upper indices `x^i` | column vector entries `x_i` |
| several equations written as a component list | `\vect{x}' = \vect{f}(t,\vect{x})` |
| partial derivatives of all components | Jacobian `D_{\vect{x}}\vect{f}` |
| formal derivative symbol `p` | `D = d/dt`; polynomial `L(s)`, operator `L(D)` |
| dot derivative in mechanics/control | retain `\dot{\vect{x}}`, `\ddot{\vect{x}}` for vector states |
| elimination equations | polynomial matrix `\mat{L}(D)\vect{x}=\vect{f}` and adjugate |
| phase coordinates `xi^1, xi^2` | coordinates in a basis of eigenvectors |

Vector and matrix symbols use bold upright type throughout, including vector-valued functions,
initial states, eigenvectors, and matrix polynomials. Use `\vect{...}` for vectors
and `\mat{...}` for matrices. Individual components, matrix entries, eigenvalues,
determinants, and scalar differential operators retain normal math weight.

## Figure requirements

- All 38 current figures are redrawn in TikZ, with editable sources in
  `figures/01.tex` through `figures/38.tex`.
- Reference crops from the original scan are stored in `assets/figures/` as
  `原图01.png` through `原图38.png`. These are source references, distinct from
  the TikZ drawings used in the typeset text.
- Figures 1-6: first chapter diagrams.
- Figures 7-16: second chapter circuit diagrams.
- Figures 17-38: second chapter phase-space and phase-plane diagrams.
- Chapter files include the TikZ sources with `\input{figures/NN.tex}`.
- Add later chapters' TikZ sources to `figures/` and reference crops to
  `assets/figures/`, preserving original numbering and their correspondence.
- Every figure keeps its original number and mathematical purpose.
- A figure must have explanatory prose beside it, not stand in for a proof.

## Typesetting outputs

- Run `python scripts/build.py` from the project root; the default engine is
  Tectonic. Use `--engine xelatex` to select XeLaTeX.
- The typeset document is `build/main.pdf`. All generated PDF and intermediate
  typesetting files belong under `build/`, which is not committed to the repository.
- Page ranges in the tables above refer to the original book and original scan,
  and must not be replaced with changing pagination from `build/main.pdf`.

## Rights and attribution

The MIT license applies to this project's added code and modifications that the
project author has the right to license. The original book, scans, and reference
figures retain their respective rights; this project does not relicense them.
