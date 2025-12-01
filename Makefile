PATH_SOURCES=advent_of_code_2025
PATH_HOOKS=.hooks
PATH_VENV=.venv
PYTHON_VERSION=3.13

.PHONY: install

install: _setup_local _install_hooks

uninstall: _uninstall_hooks _remove_venv

_install_hooks:
	${PATH_HOOKS}/install_hooks.sh -i

_uninstall_hooks:
	${PATH_HOOKS}/install_hooks.sh -u all

_setup_local:
	python${PYTHON_VERSION} -m venv .venv
	${PATH_VENV}/bin/python${PYTHON_VERSION} -m pip install --upgrade pip poetry
	${PATH_VENV}/bin/python${PYTHON_VERSION} -m poetry install --with dev

_remove_venv:
	rm -rf .venv

lint:
	export PYTHONPATH="${PYTHONPATH}:$$(pwd)/${PATH_SOURCES}" && ${PATH_VENV}/bin/python${PYTHON_VERSION} -m pylint ${PATH_SOURCES}

mypy:
	${PATH_VENV}/bin/python${PYTHON_VERSION} -m mypy ${PATH_SOURCES} --ignore-missing-imports --strict --implicit-reexport

black:
	${PATH_VENV}/bin/python${PYTHON_VERSION} -m black ${PATH_SOURCES} --check

flake:
	${PATH_VENV}/bin/python${PYTHON_VERSION} -m flake8 ${PATH_SOURCES} --config ./setup.cfg

isort:
	${PATH_VENV}/bin/python${PYTHON_VERSION} -m isort ${PATH_SOURCES} --check-only

format:
	${PATH_VENV}/bin/python${PYTHON_VERSION} -m black ${PATH_SOURCES}
	${PATH_VENV}/bin/python${PYTHON_VERSION} -m isort ${PATH_SOURCES}

check: black isort mypy flake lint
