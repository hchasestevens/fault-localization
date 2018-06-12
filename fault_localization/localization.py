"""Fault localization calculations."""


import collections


ExecutionCounts = collections.namedtuple(
    "ExecutionCounts",
    "positive_cases negative_cases"
)

LINE_EXECUTIONS = collections.defaultdict(
    lambda: ExecutionCounts(
        positive_cases=0,
        negative_cases=0,
    )
)


def update_executions(lines, failed, line_executions=LINE_EXECUTIONS):
    """Update line executions to reflect test results."""
    for line in lines:
        prev_executions = line_executions[line]
        line_executions[line] = ExecutionCounts(
            positive_cases=prev_executions.positive_cases + int(not failed),
            negative_cases=prev_executions.negative_cases + int(failed)
        )


PRIOR = ExecutionCounts(
    positive_cases=1,
    negative_cases=0
)


def calc_scores(line_executions=LINE_EXECUTIONS, prior=PRIOR):
    """Return 'fault' score for each line, given prior and observations."""
    return {
        line: float(
            execution_counts.negative_cases + prior.negative_cases
        ) / (
            execution_counts.positive_cases + prior.positive_cases
            + execution_counts.negative_cases + prior.negative_cases
        )
        for line, execution_counts in line_executions.items()
    }
