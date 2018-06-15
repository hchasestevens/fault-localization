"""Display utilities."""

import os
import collections


LINE_CONTEXT = 5

OutputLine = collections.namedtuple(
    'OutputLine',
    'num content score'
)


CUBE_LEVELS = (0x00, 0x5f, 0x87, 0xaf, 0xd7, 0xff,)
SNAP_POINTS = tuple(
    (lower + upper) / 2
    for lower, upper in
    zip(CUBE_LEVELS, CUBE_LEVELS[1:])
)


def rgb_to_hex(*channels):
    r, g, b = (
        sum(
            snap_point < channel
            for snap_point in SNAP_POINTS
        )
        for channel in channels
    )
    return r * 36 + g * 6 + b + 16


def generate_output(line_scores, line_context=LINE_CONTEXT):
    """Given line scores, create final localization output."""
    try:
        fname, line_no = max(line_scores, key=line_scores.get)
    except ValueError:
        yield "No lines from specified directory captured during test suite execution."
        return

    max_score = line_scores[fname, line_no]
    min_score = min(line_scores.values())

    with open(fname, 'r') as f:
        file_contents = f.read().splitlines()

    def try_get_line(line_no):
        try:
            yield file_contents[line_no]
        except IndexError:
            return

    output_lines = (
        OutputLine(
            num=line_no + 1,
            content=line,
            score=round(line_scores.get((fname, line_no), 0), 2)
        )
        for line_no in range(
            line_no - line_context,
            line_no + line_context + 1
        )
        if line_no >= 0
        for line in try_get_line(line_no)
    )

    yield '\u001b[1m{}\u001b[0m'.format(os.path.relpath(fname, os.getcwd()))
    for line in output_lines:
        # todo: right-justify the numeric score value (rather than tab)
        yield '{line.num}\t\x1b[48;5;{ansi_tag}m{line.content}\033[0m\t{line.score}'.format(
            line=line,
            ansi_tag=rgb_to_hex(
                int(
                    (line.score - min_score) / (max_score - min_score) * 255
                ), 0, 0
            )  # TODO - want to actually represent this in HSV space and go from neutral green/orange to red - see also http://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html#background-colors
            # TODO - can we use RGB for background color rather than hex?
        )
