"""Pytest plugin."""

import os
import sys

import pytest

from fault_localization.tracing import TRACER
from fault_localization.localization import update_executions, calc_scores
from fault_localization.display import generate_output


LOCALIZATION_DIR = None


def pytest_addoption(parser):
    group = parser.getgroup('fault-localization', 'fault localization')
    group.addoption('--localize', help="directory in which to localize faults")


def pytest_configure(config):
    global LOCALIZATION_DIR
    LOCALIZATION_DIR = config.getoption('--localize')


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_call(item):
    if not LOCALIZATION_DIR:
        yield
        return

    sys.settrace(TRACER.trace)
    try:
        yield
    finally:
        sys.settrace(None)


def pytest_runtest_makereport(item, call):
    failed = bool(getattr(call, 'excinfo', False))
    update_executions(
        lines=TRACER.flush_buffer(),
        failed=failed
    )


def pytest_terminal_summary(terminalreporter):
    if not LOCALIZATION_DIR:
        return
    abs_localization_dir = os.path.abspath(LOCALIZATION_DIR)

    terminalreporter.section("Fault Localization Results")
    line_scores = {
        (path, line): score
        for (path, line), score in calc_scores().items()
        if path.startswith(abs_localization_dir)
    }
    for line in generate_output(line_scores):
        terminalreporter.write_line(line)
