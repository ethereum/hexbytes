from pathlib import (
    Path,
)
import subprocess
from tempfile import (
    TemporaryDirectory,
)
import venv


def create_venv(parent_path: Path) -> Path:
    venv_path = parent_path / "package-smoke-test"
    venv.create(venv_path, with_pip=True)
    subprocess.run(
        [venv_path / "bin" / "pip", "install", "-U", "pip", "setuptools"], check=True
    )
    return venv_path


def find_wheel(project_path: Path) -> Path:
    wheels = list(project_path.glob("dist/*.whl"))

    if len(wheels) != 1:
        raise Exception(
            f"Expected one wheel. Instead found: {wheels} "
            f"in project {project_path.absolute()}"
        )

    return wheels[0]


def install_wheel(venv_path: Path, wheel_path: Path) -> None:
    subprocess.run(
        [venv_path / "bin" / "pip", "install", f"{wheel_path}"],
        check=True,
    )


def test_install_local_wheel() -> None:
    with TemporaryDirectory() as tmpdir:
        venv_path = create_venv(Path(tmpdir))
        wheel_path = find_wheel(Path("."))
        install_wheel(venv_path, wheel_path)
        print("Installed", wheel_path.absolute(), "to", venv_path)

        package_tests = Path("./scripts/release/tests_to_run_on_package.py")

        result = subprocess.run(
            [venv_path / "bin" / "python", package_tests],
            capture_output=True,
            text=True,
        )

        if result.returncode == 0:
            print("Tests Passed:", result.stdout)
        else:
            print("Error in package testing:", result.stderr)


if __name__ == "__main__":
    test_install_local_wheel()
