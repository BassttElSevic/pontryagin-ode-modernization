# XeLaTeX builds from editors or latexmk also keep all output in build/.
$pdf_mode = 5;
$out_dir = 'build';
$aux_dir = 'build';
$xelatex = 'xelatex -interaction=nonstopmode -halt-on-error -file-line-error %O %S';
