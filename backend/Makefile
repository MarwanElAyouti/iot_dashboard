.PHONY: format lint

sources = .
isort = isort $(sources)
black = black $(sources)
flakehell = flakehell lint $(sources)

all: format lint

format:
	$(isort)
	$(black)

lint:
	$(flakehell)

