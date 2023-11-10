all: default

clean: 

deps:
	pip install -r requirements.txt

dev_deps:
	pip install -r requirements-dev.txt

check-format: dev_deps
	yapf -rd ./

format: dev_deps
	yapf -ri ./

lint: check-format
	pylint -r n ./

lint-no-error: 
	pylint --exit-zero -r n ./

test: init dev_deps
	python3 -m pytest -v

init: clean deps