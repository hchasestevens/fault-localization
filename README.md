# fault-localization

[![Build Status](https://travis-ci.org/hchasestevens/fault-localization.svg?branch=master)](https://travis-ci.org/hchasestevens/fault-localization)
[![PyPI version](https://badge.fury.io/py/fault-localization.svg)](https://badge.fury.io/py/fault-localization)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/fault-localization.svg) 
[![Liberapay receiving](https://img.shields.io/liberapay/receives/hchasestevens.svg)](https://liberapay.com/hchasestevens/)

## What is this good for?

Not all failing code raises exceptions; behavioral bugs can be the hardest to diagnose. 
`fault-localization` is a pytest plugin that helps you identify and isolate the lines of code most
likely to be causing test failure, using the simple rule-of-thumb that the most suspicious code is the
code run most often in failing tests.

## Installation

```bash
pip install fault-localization
```

## Usage

With `fault-localization` installed, running

```bash
pytest --localize {dir} [pytest args]
```

will highlight suspicious lines encountered within `dir` while running the test configuration specified.
If you suspect multiple sources of failure, or if there are multiple tests within your suite that 
exercise the area of code you're interested in, using pytest's `-k` flag is useful for running 
fault localization on only a subset of your suite.

## Contacts

* Name: [H. Chase Stevens](http://www.chasestevens.com)
* Twitter: [@hchasestevens](https://twitter.com/hchasestevens)
