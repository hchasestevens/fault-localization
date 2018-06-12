# fault-localization

[![Build Status](https://travis-ci.org/hchasestevens/fault-localization.svg?branch=master)](https://travis-ci.org/hchasestevens/fault-localization)
[![PyPI version](https://badge.fury.io/py/fault-localization.svg)](https://badge.fury.io/py/fault-localization)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/fault-localization.svg) 
[![Liberapay receiving](https://img.shields.io/liberapay/receives/hchasestevens.svg)](https://liberapay.com/hchasestevens/)

## What is this good for?

Not all failing code raises exceptions; behavioral bugs can be the hardest to diagnose. 
`fault-localization` is a [pytest](https://docs.pytest.org/en/latest/) plugin that helps you identify and isolate the lines of code most
likely to be causing test failure, using the simple rule-of-thumb that the most suspicious code is the
code run most often in failing tests. Don't just rely on your tests to _catch_ bugs - use them to _pinpoint_ bugs.

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
exercise the area of code you're interested in, using [pytest's `-k` flag](https://docs.pytest.org/en/latest/usage.html#specifying-tests-selecting-tests) is useful for running 
fault localization on only a subset of your suite.

Fault localization, as a technique, works best when areas of your codebase are exercised repeatedly 
across a bevy of differing cases and values. That's why `fault-localization` works with Python's premiere 
property-based testing framework, [Hypothesis](http://hypothesis.works), out of the box - which does 
just that.

## Contacts

* Name: [H. Chase Stevens](http://www.chasestevens.com)
* Twitter: [@hchasestevens](https://twitter.com/hchasestevens)
