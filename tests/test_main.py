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
            "    -   id: safe-commit\n"
            "        name: safe-commit\n"
            "        entry: safe-commit\n"
            "        language: system\n"
            "        pass_filenames: false\n"
            "        always_run: true\n"
        )
    os.system("pre-commit install")
    os.system("git add .pre-commit-config.yaml")
    assert os.system("git commit -m 'test success' ")

def test_failure(tmpdir):
    os.chdir(tmpdir)
    os.system("git init")
    #os.system("git checkout -b success ")
    with open(".pre-commit-config.yaml","w") as file:
        file.write(
            "repos:\n"
            "-   repo: local\n"
            "    hooks:\n"
            "    -   id: safe-commit\n"
            "        name: safe-commit\n"
            "        entry: safe-commit\n"
            "        language: system\n"
            "        pass_filenames: false\n"
            "        always_run: true\n"
        )
    os.system("pre-commit install")
    os.system("git add .pre-commit-config.yaml")
    assert os.system("git commit -m 'test success' ")