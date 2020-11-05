import pytest
import os

def test_success(tmpdir):
    os.chdir(tmpdir)
    os.system("git init")
    os.system("git checkout -b success ")
    with open(".pre-commit-config.yaml","w") as file:
        file.write(
            "repos:\n"
            "-   repo: local\n"
            "    hooks:\n"
            "    -   id: pytest-check\n"
            "        name: pytest-check\n"
            "        entry: pytest\n"
            "        language: system\n"
            "        pass_filenames: false\n"
            "        always_run: true\n"
        )

    os.system("git add .pre-commit-config.yaml")
    os.system("git commit -m 'test success' ")