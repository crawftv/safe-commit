import pytest
import os


@pytest.mark.parametrize(
    "branch,solution,protected_branches",
    [("success", 0, ""), ("success", 1, "success"), ("main", 1, ""), ("master", 1, "")],
)
def test_success(tmpdir, branch, solution, protected_branches):
    os.chdir(tmpdir)
    os.system("git init")
    os.system(f"git checkout -b {branch}")
    with open(".pre-commit-config.yaml", "w") as file:
        file.write(
            "repos:\n"
            "-   repo: local\n"
            "    hooks:\n"
            "    -   id: safe-commit\n"
            "        name: safe-commit\n"
            f"        entry: safe-commit {protected_branches}\n"
            "        language: system\n"
            "        pass_filenames: false\n"
            "        always_run: true\n"
        )
    os.system("pre-commit install")
    os.system("git add .pre-commit-config.yaml")
    assert os.system("git commit -m 'test' ") == solution
