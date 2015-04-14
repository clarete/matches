.PHONY: tests deps

all: deps tests

deps:
	pip install -r requirements.txt

unit:
	nosetests -vs --with-coverage --cover-package=matches tests

acceptance:
	steadymark README.md

tests: unit acceptance
