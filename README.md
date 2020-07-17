# Prosegrinder

[![Latest PyPI
version](https://img.shields.io/pypi/v/prosegrinder.svg)](https://pypi.python.org/pypi/prosegrinder)

[![GitHub Workflow
Status](https://github.com/prosegrinder/python-prosegrinder/workflows/Python%20CI/badge.svg?branch=master)](https://github.com/prosegrinder/python-prosegrinder/actions?query=workflow%3A%22Python+CI%22+branch%3Amaster)

[![Latest Codacy Coverage
Report](https://app.codacy.com/project/badge/Grade/fbb22c1d33a34aa3bee095fc3ff62bc9)](https://www.codacy.com/gh/prosegrinder/python-prosegrinder?utm_source=github.com&utm_medium=referral&utm_content=prosegrinder/python-prosegrinder&utm_campaign=Badge_Grade)

A relatively fast, functional prose text counter with readability
scoring.

## Installation

`prosegrinder` is available on PyPI. Simply install it with `pip`:

```bash
pip install prosegrinder
```

## Usage

The main use is via the `prosegrinder.Prose` object.

```python
>>> from prosegrinder import Prose
>>> p = Prose("Some lengthy text that's actual prose, like a novel or article.")
```

The Prose object will parse everything down and compute basic
statistics, including word count, sentence count, paragraph count,
syllable count, point of view, dialogue, narrative, and a set of
readability scores. All objects and attributes should be treated as
immutable.

I know this isn't great documentation, but it should be enough to get
you going.
