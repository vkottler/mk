"""
A module implementing a task for running yamllint.
"""

# built-in
from pathlib import Path
from typing import Dict

# third-party
from vcorelib.task import Inbox, Outbox
from vcorelib.task.manager import TaskManager
from vcorelib.task.subprocess.run import SubprocessLogMixin


class Yamllint(SubprocessLogMixin):
    """A task for running a YAML linter on project source(s)."""

    async def run(self, inbox: Inbox, outbox: Outbox, *args, **kwargs) -> bool:
        """Create or update a project's virtual environment."""

        cwd: Path = args[0]

        return await self.exec(
            str(
                inbox["venv"]["venv{python_version}"]["bin"].joinpath(
                    "yamllint"
                )
            ),
            str(cwd.joinpath(kwargs["location"])),
        )


def register(
    manager: TaskManager,
    project: str,
    cwd: Path,
    substitutions: Dict[str, str],
) -> bool:
    """Register YAML linting tasks to the manager."""

    manager.register(
        Yamllint("yaml-lint-{location}", cwd),
        ["venv", "python-install-yamllint"],
    )

    del project
    del substitutions
    return True
