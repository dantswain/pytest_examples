# Pytest Examples

[![Build Status](https://travis-ci.org/dantswain/pytest_examples.svg?branch=master)](https://travis-ci.org/dantswain/pytest_examples)

These are some examples of using pytest that I put together for a presentation.

## Setup

Uses [pipenv](https://docs.pipenv.org/) and Python 3.6.  Assuming you have
those:

```
pipenv install -d
pipenv shell
```

## Running tests

You can run pytest directly:

```
pytest
pytest -vvv # more verbose
```

Or via `pytest`:

```
python -m pytest
python -m pytest -vvv # more verbose
```

To generate a coverage report:

```
pytest -vvv --cov=.
pytest -vvv --cov=. --cov-report=html
```
