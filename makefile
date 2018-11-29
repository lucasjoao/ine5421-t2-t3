.PHONY:
	all
	clean


all:
	@python runner.py
	@python -m unittest discover -b

t2:
	@python runner.py t2

dump:
	@python runner.py dump

t3:
	@python runner.py

t3_phase:
	@python runner.py t3_phase

test:
	@python -m unittest discover -b

test_verbose:
	@python -m unittest discover


clean:
	@rm -rf __pycache__
	@rm -rf lexer/__pycache__
