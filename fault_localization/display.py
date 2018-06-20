"""Display utilities."""

import os
import collections
from operator import attrgetter

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


def generate_output(line_scores, line_context=LINE_CONTEXT, n_lines=1):
    """Given line scores, create final localization output."""
    ranked_lines = sorted(line_scores, key=line_scores.get, reverse=True)
    if not ranked_lines:
        yield "No lines from specified directory captured during test suite execution."
        return

    max_score = line_scores[ranked_lines[0]]
    min_score = min(line_scores.values())

    out_buffer = collections.defaultdict(set)

    for _, (fname, line_no) in zip(range(n_lines), ranked_lines):
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

        out_buffer_key = '\x1b[1m{}\x1b[0m'.format(os.path.relpath(fname, os.getcwd()))
        for line in output_lines:
            out_buffer[out_buffer_key].add(line)

    out_buffer_sequence = sorted(
        out_buffer.items(),
        key=lambda k_v: max(k_v[1], key=attrgetter('score')),
        reverse=True
    )
    for header, lines in out_buffer_sequence:
        yield header
        for line in sorted(lines, key=attrgetter('num')):
            # todo: right-justify the numeric score value (rather than tab)
            yield '{line.num}\t\x1b[48;5;{ansi_tag}m{line.content}\033[0m\t{line.score}'.format(
                line=line,
                ansi_tag=rgb_to_hex(
                    int(
                        (line.score - min_score) / (max_score - min_score) * 255
                    ), 0, 0
                )
                # TODO - want to actually represent this in HSV space and go from neutral green/orange to red - see also http://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html#background-colors
                # TODO - can we use RGB for background color rather than hex?
            )
