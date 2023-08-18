from __future__ import annotations

from contextlib import contextmanager, redirect_stdout, redirect_stderr
import io
import sys
from typing import Generator, TextIO, List, Optional, Type, TYPE_CHECKING

if TYPE_CHECKING:
    from argparse import ArgumentParser


@contextmanager
def redirect_stdin(stream: Optional[TextIO] = None) -> Generator[None, None, None]:
    if stream is None:
        yield

    else:
        old_stdin = sys.stdin
        try:
            sys.stdin = stream
            yield
        finally:
            sys.stdin = old_stdin


class ToolRunner:
    def __init__(self, parser: ArgumentParser, tool_cls: Type):
        self.parser = parser
        self.tool_cls = tool_cls

    def run(self, args: List[str], stdin: str = None):
        stdin_str = stdin
        stdout = io.StringIO()
        stderr = io.StringIO()
        stdin_stream: Optional[TextIO] = None
        if stdin_str:
            stdin_stream = io.StringIO()
            assert stdin_stream is not None
            stdin_stream.write(stdin_str)
            stdin_stream.seek(0)
        with redirect_stdout(stdout), redirect_stderr(stderr), redirect_stdin(stdin_stream):
            self.tool_cls.run(self.parser.parse_args(args))  # noqa

        return stdout.getvalue(), stderr.getvalue()
