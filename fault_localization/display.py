"""Display utilities."""

import collections


LINE_CONTEXT = 5

OutputLine = collections.namedtuple(
    'OutputLine',
    'num content score'
)


def generate_output(line_scores, line_context=LINE_CONTEXT):
    """Given line scores, create final localization output."""
    fname, line_no = max(line_scores, key=line_scores.get)

    with open(fname, 'r') as f:
        file_contents = f.read().splitlines()

    def try_get_line(line_no):
        try:
            yield file_contents[line_no]
        except IndexError:
            return

    output_lines = (
        OutputLine(
            num=line_no,
            content=line,
            score=line_scores.get((line, line_no), 0)
        )
        for line_no in range(
            line_no - line_context,
            line_no + line_context + 1
        )
        for line in try_get_line(line_no)
    )

    yield fname  # bolded - or some kind of header
    for line in output_lines:
        yield '{line.num}\t{ansi_tag}{line.content}\033[0m'
