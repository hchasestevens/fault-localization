"""Unit tests for fault_localization/localization.py"""
import collections

import pytest

from fault_localization import localization


@pytest.mark.parametrize('failed,expected_output', (
    (False, localization.ExecutionCounts(positive_cases=1, negative_cases=0)),
    (True, localization.ExecutionCounts(positive_cases=0, negative_cases=1))
))
def test_update_executions(failed, expected_output):
    """Ensure that line counts are incremented as expected for test result."""
    executions = collections.defaultdict(
        lambda: localization.ExecutionCounts(
            positive_cases=0,
            negative_cases=0,
        )
    )
    localization.update_executions([1], failed, line_executions=executions)
    assert executions[1] == expected_output
