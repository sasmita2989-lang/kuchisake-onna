"""Kuchisake-onna python package."""

import signal

from .exceptions import CutByKuchisakeOnnaError
from .kuchisake_onna import ask_question

# ignore Ctrl+C
signal.signal(signal.SIGINT, signal.SIG_IGN)

__version__ = "1.0.0"

__all__ = [
    "ask_question",
    "CutByKuchisakeOnnaError",
    "__version__",
]

ask_question()
