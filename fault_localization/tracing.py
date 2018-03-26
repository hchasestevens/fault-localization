"""Line-by-line program execution tracing."""


class Tracer(object):
    LINE_BUFFER = []

    def trace(self, frame, event, arg):
        if event == 'call':
            return self.trace
        elif event != 'line':
            return
        line = frame.f_code.co_filename, frame.f_lineno
        self.LINE_BUFFER.append(line)

    def flush_buffer(self):
        buffer, self.LINE_BUFFER = self.LINE_BUFFER, []
        return buffer


TRACER = Tracer()
