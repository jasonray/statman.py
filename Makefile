all: default

clean: 

deps:
	pip install -r requirements.txt

dev_deps:
	pip install -r requirements-dev.txt

check-format: dev_deps
	yapf -rd statman/

format: dev_deps
	yapf -ri statman/

lint: check-format
	pylint -r n statman/

lint-no-error: 
	pylint --exit-zero -r n statman/

test: init dev_deps
	python3 -m pytest -v

init: clean deps