run:
	lualatex --output-directory=build --jobname=synopsis main.tex
	lualatex --output-directory=build --jobname=synopsis main.tex
	cp build/synopsis.pdf .
