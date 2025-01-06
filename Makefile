PHONY: install run virtualenv ipython clean test pflake8 fmt lint live


install:
	@echo "Installing for dev environment"
	@.venv/bin/python -m pip install -e '.[test,dev]'


virtualenv:
	@python -m venv .venv


live:
	@python manage.py livereload


run:
	@python manage.py runserver


ipython:
	@.venv/bin/ipython


test:
	@.venv/bin/pytest -vv -s
  
lint:
	@.venv/bin/pflake8 app kamila_project

fmt:
	@.venv/bin/isort --profile=black -m 3 app kamila_project
	@.venv/bin/black app kamila_project

clean:            ## Clean unused files.
	@find ./ -name '*.pyc' -exec rm -f {} \;
	@find ./ -name '__pycache__' -exec rm -rf {} \;
	@find ./ -name 'Thumbs.db' -exec rm -f {} \;
	@find ./ -name '*~' -exec rm -f {} \;
	@rm -rf .cache
	@rm -rf .pytest_cache
	@rm -rf .mypy_cache
	@rm -rf build
	@rm -rf dist
	@rm -rf *.egg-info
	@rm -rf htmlcov
	@rm -rf .tox/
	@rm -rf docs/_build
