.PHONY:
	all
	clean


all:
	@python runner.py


clean:
	@rm -rf __pycache__
	@rm -rf lexer/__pycache__
