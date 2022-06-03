"""
A module for Python-package building tasks.
"""

# built-in
from pathlib import Path
from typing import Dict

# third-party
from vcorelib.task.manager import TaskManager


def register(
    manager: TaskManager,
    project: str,
    cwd: Path,
    substitutions: Dict[str, str],
) -> bool:
    """Register package building tasks to the manager."""

    del manager
    del project
    del cwd
    del substitutions
    return True
