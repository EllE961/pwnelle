from setuptools import setup, find_packages
import os

# Read the content of README.md for the long description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="pwnelle",
    version="1.0.0",
    author="EllE961",
    author_email="yahyaalsalmi961@gmail.com",
    description="A modern binary analysis tool that helps identify vulnerabilities and generates exploit templates",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/pwnelle",
    project_urls={
        "Bug Tracker": "https://github.com/yourusername/pwnelle/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Security",
        "Topic :: Software Development :: Debuggers",
    ],
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
        "pwntools",
        "capstone",
        "pyelftools",
        "ROPgadget",
        "python-Levenshtein",
    ],
    entry_points={
        "console_scripts": [
            "pwnelle=pwnelle.cli:main",
        ],
    },
) 