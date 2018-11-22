.PHONY:
	all
	clean


all:
	@python mvp.py


clean:
	@rm -rf __pycache__
	@rm -rf lexer/__pycache__
