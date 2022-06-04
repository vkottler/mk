"""
A module for Python-package building tasks.
"""

# built-in
from os import environ
from pathlib import Path
from shutil import rmtree
from typing import Dict

# third-party
from vcorelib.task import Inbox, Outbox
from vcorelib.task.manager import TaskManager
from vcorelib.task.subprocess.run import SubprocessLogMixin

# internal
from vmklib.tasks.mixins.concrete import ConcreteBuilderMixin


class PythonBuild(ConcreteBuilderMixin, SubprocessLogMixin):
    """Build a Python package."""

    async def run(
        self,
        inbox: Inbox,
        outbox: Outbox,
        *args,
        **kwargs,
    ) -> bool:
        """A task for building a Python package."""

        cwd: Path = args[0]

        # Remove any existing build artifacts.
        dist = cwd.joinpath("dist")
        rmtree(dist, ignore_errors=True)

        init_data = inbox["vmklib.init"]
        build = init_data["__dirs__"]["build"]
        rmtree(build.joinpath("lib"), ignore_errors=True)
        # We could also try to delete: $(BUILD_DIR)/bdist*

        # Build package.
        return await self.exec(
            str(inbox["venv"]["venv{python_version}"]["python"]),
            "-m",
            "build",
            "-o",
            str(dist),
            *environ.get("PY_BUILD_EXTRA_ARGS", "").split(),
            str(cwd),
        )


def register(
    manager: TaskManager,
    project: str,
    cwd: Path,
    substitutions: Dict[str, str],
) -> bool:
    """Register package building tasks to the manager."""

    # Make sure 'wheel' is also installed so we can build a wheel.
    reqs = ["venv", "python-install-build"]
    manager.register(PythonBuild("python-build", cwd, once=False), reqs)
    manager.register(PythonBuild("python-build-once", cwd), reqs)

    del project
    del substitutions
    return True
