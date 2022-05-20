<!--
    =====================================
    generator=datazen
    version=2.0.0
    hash=ccd6300d31b620785feac5581d2df14f
    =====================================
-->

# vmklib ([1.2.0](https://pypi.org/project/vmklib/))

[![python](https://img.shields.io/pypi/pyversions/vmklib.svg)](https://pypi.org/project/vmklib/)
![Build Status](https://github.com/vkottler/vmklib/workflows/Python%20Package/badge.svg)
[![codecov](https://codecov.io/gh/vkottler/vmklib/branch/master/graphs/badge.svg?branch=master)](https://codecov.io/github/vkottler/vmklib)

*Simplify project workflows by standardizing use of GNU Make.*

See also: [generated documentation](https://vkottler.github.io/python/pydoc/vmklib.html)
(created with [`pydoc`](https://docs.python.org/3/library/pydoc.html)).

This tool integrates with existing `Makefile`'s with zero additional
content or bootstrapping required.

There are many choices in technology or products for performing static
analysis on source code, building test infrastructure, or managing local
development environments. These are only a small subset of common, developer
tasks when building software. This package intends to aggregate recipes
(and their dependency relationships) for these tasks so that they can be
integrated into a project without re-building this infrastructure. Lessons
learned and improvements in each project can be back-propagated everywhere
else with simple package updates.

## Quick Links

* [datazen](#datazen)
* [grip](#grip)
* [pypi](#pypi)
* [python](#python)
* [venv](#venv)
* [vmklib](#vmklib)
* [yaml](#yaml)
* [Dependency Graph](#dependency-graph)

# Command-line Options

```
$ ./venv3.8/bin/mk -h

usage: mk [-h] [--version] [-v] [-C DIR] [-p PREFIX] [-f FILE] [-c CONFIG]
          [-P PROJ]
          [targets [targets ...]]

Simplify project workflows by standardizing use of GNU Make.

positional arguments:
  targets               targets to execute

optional arguments:
  -h, --help            show this help message and exit
  --version             show program's version number and exit
  -v, --verbose         set to increase logging verbosity
  -C DIR, --dir DIR     execute from a specific directory
  -p PREFIX, --prefix PREFIX
                        a prefix to apply to all targets
  -f FILE, --file FILE  file to source user-provided recipes from (default:
                        'Makefile')
  -c CONFIG, --config CONFIG
                        file to source user-provided variable definitions,
                        ahead of loading package makefiles (default:
                        'vmklib.json')
  -P PROJ, --proj PROJ  project name for internal variable use

```

# Targets

Note that the full invocation for a target's command is:

```
mk [options] <prefix>-<command> [ARG1=val1 ARG2=val2]
```

## datazen

Targets for use with the [datazen](https://pypi.org/project/datazen/) package.

Prefix: `dz-`

### Optional Arguments

**DZ_DIR** - Optionally override the `-C` argument.

**DZ_MANIFEST** - Optionally provide a non-default manifest file to `-m`.

**DZ_VERBOSE** - Setting this passes `-v` as an additional argument.

### Commands

**sync** - Run `dz`, executing the default target.

**clean** - Run `dz` with `-c` to clean the cache.

**describe** - Run `dz` with `-d` to describe cache contents.

**install** - Install `datazen` in the resolved virtual environment (with `pip`). This depends on a "concrete" underlying target that allows it to be installed only once.

**upgrade** - Upgrade `datazen` in the resolved virtual environment (with `pip`).

## grip

Targets for rendering [GitHub Markdown](https://docs.github.com/en/rest/reference/markdown) with [grip](https://github.com/joeyespo/grip).

Prefix: `grip-`

### Optional Arguments

**SECRETHUB_GRIP_PATH** - The full path for the `secrethub read` command to source a [GitHub personal access token](https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token) from, requires [secrethub](https://secrethub.io/).

**GRIP_PORT** - The `host:port` String to serve the rendered results on.

**GRIP_ENV** - Output file to write to for sourcing credentials.

**GRIP_FILE** - The file to render, path is relative to project root.

### Commands

**check-env** - Checks that `GRIP_TOKEN` is set in the environment, errors if not.

**render** - Serve `README.md` with `grip`.

## pypi

Targets for uploading packages to [PyPI](https://pypi.org/).

Prefix: `pypi-`

### Optional Arguments

**UPLOAD_ENV** - Output file to write to for sourcing credentials.

**SECRETHUB_PYPI_PATH** - The full path for the `secrethub read` command to source a [PyPI API token](https://pypi.org/help/#apitoken) from, requires [secrethub](https://secrethub.io/).

### Commands

**check-env** - Enforces that `TWINE_USERNAME` and `TWINE_PASSWORD` are set in the environment, errors if not.

**upload** - Attempt to upload everything in `dist` to [PyPI](https://pypi.org/).

## python

Targets for executing common, [Python](https://www.python.org/) workflow tasks.

Prefix: `python-`

### Optional Arguments

**PY_LINT_ARGS** - Set to override the default, adds the `tests` directory and `PY_LINT_EXTRA_ARGS`.

**PY_WIDTH** - Override (from `79`) to set `--line-length` arguments for formatters.

**PY_LINT_EXTRA_ARGS** - Set to add additional linting arguments.

**PYTEST_ARGS** - Set to override the default, additional [pytest](https://docs.pytest.org/en/stable/) arguments.

**PYTEST_EXTRA_ARGS** - Add additional arguments to the default set.

**PYTHON_COV_PORT** - Port to host test-coverage HTML on (using `http.server`). Defaults to zero.

**PY_BUILDER** - The target name to use as a `python-upload` dependency (e.g. `python-dist` versus `python-build`). Defaults to `python-build`.

**PY_DOCS_HOST** - Host argument passed to `pydoc` module (`-n`). Defaults to `0.0.0.0`.

**PY_DOCS_PORT** - Port argument passed to `pydoc` module (`-p`). Defaults to `0`.

**PY_DOCS_EXTRA_ARGS** - Extra arguments to pass to the `pydoc` module.

### Commands

**lint** - Run [pylint](https://www.pylint.org/) and [flake8](https://flake8.pycqa.org/en/latest/) against a project's package sources. Also runs the format checkers.

**sa** - Run [mypy](http://mypy-lang.org/) against a project's package sources.

**sa-types** - Run [mypy](http://mypy-lang.org/) without checking the result and attempt to install missing type/stub packages.

**stubs** - Run [stubgen](https://mypy.readthedocs.io/en/stable/stubgen.html) against a project's package sources.

**format** - Run [black](https://pypi.org/project/black/) and [isort](https://pypi.org/project/isort/) against a project's package sources.

**format-check** - Run [black](https://pypi.org/project/black/) with the `--check` argument and [isort](https://pypi.org/project/isort/) with the `--check-only` argument.

**tags** - Create a `tags` file for the project using [ctags](https://github.com/universal-ctags/ctags) (must be installed).

**edit** - Create `tags` and then open $EDITOR in the project directory.

**test** - Run all of a project's tests with [pytest](https://docs.pytest.org/en/stable/).

**test-%** - Run project tests based on a search pattern (i.e. the `-k` option).

**view** - Attempt to open the test-coverage HTML with `$BROWSER` (environment variable).

**host-coverage** - Host test-coverage HTML locally, with the port specified by `PYTHON_COV_PORT`.

**all** - Run `lint`, `sa` and `test` in sequence.

**clean** - Remove compiled and cached files, test coverage, built package artifacts and other caches.

**dist** - Build `sdist` and `bdist_wheel` with `setup.py` in the project root.

**build** - Build the package with `python -m build`.

**dist-with-stubs** - Build `sdist` and `bdist_wheel` with `setup.py` in the project root, this also runs `stubgen` ahead of packaging so that stubs are included in the source distribution and wheel.

**upload** - Use [twine](https://pypi.org/project/twine/) to upload the built package to [PyPI](https://pypi.org/).

**editable** - Install the project's package in editable mode (`-e` option) to the virtual environment.

**docs** - Run the `pydoc` module and host HTML documentation via an arbitrary HTTP port.

**docs-%** - Run the `pydoc` module and pass the stem as an argument.

**deps** - Run `pydeps` against the project (producing [SVG](https://www.w3.org/TR/SVG2/) output).

## venv

Targets for managing [Python virtual environments](https://docs.python.org/3/library/venv.html).

Prefix: `(no prefix)`

### Optional Arguments

**PYTHON_VERSION** - The version of Python to create a virtual environment for. (default: `3.8`)

**REQUIREMENTS_DIR** - The location of the directory containing requirements files. (default: `requirements` in the project root)

**REQ_FILES** - Text files to install requirements from (using `-r`), in the requirements directory. (default: `requirements.txt` and `dev_requirements.txt`)

### Commands

**venv** - Create or update the resolved virtual environment, if necessary.

**venv-clean** - Remove any virtual environments from the project root (or sub-directories).

## vmklib

Targets related to this package, itself.

Prefix: `mk-`

### Commands

**upgrade** - Upgrade (or install) `vmklib` in the resolved virtual environment.

**sys-upgrade** - Upgrade (or install) `vmklib` as a system or user package.

**header** - Print the `Makefile` header that should be used when integrating this package.

**todo** - Perform a case-insensitive search for `todo` in project directories.

## yaml

Targets for interacting with [yaml](https://yaml.org/) data (files).

Prefix: `yaml-`

### Optional Arguments

**YAMLLINT_ARGS** - Set to provide arguments to `yamllint` (such as the path to a config file).

### Commands

**yaml-lint-install** - Install [yamllint](https://yamllint.readthedocs.io/en/stable/index.html).

**yaml-lint-%** - Execute `yamllint` against `$*`.

# Internal Dependency Graph

A coarse view of the internal structure and scale of
`vmklib`'s source.
Generated using [pydeps](https://github.com/thebjorn/pydeps) (via
`mk python-deps`).

![vmklib's Dependency Graph](im/pydeps.svg)
