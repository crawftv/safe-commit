from setuptools import setup

setup(
    name="sage-commit",
    version="1.0.0",
    entry_points={"console_scripts": ["safe-commit=src.main:main"]},
)