from setuptools import setup, find_packages

setup(
    name="generic_file_io",
    version="0.1.0",
    packages=find_packages(include=["generic_file_io", "generic_file_io.*"]),
    install_requires=[],  # Core utilities have no external dependencies
    extras_require={
        "csv": ["pandas"],  # CSV handler may use pandas (optional)
        "json": [],
        "env": []
    },
)