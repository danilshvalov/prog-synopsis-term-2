run:
	lualatex --output-directory=build --jobname=synopsis --shell-escape main.tex
	lualatex --output-directory=build --jobname=synopsis --shell-escape main.tex
	cp build/synopsis.pdf .
