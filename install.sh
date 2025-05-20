#!/bin/bash
# Simple installation script for pwnelle

echo "Installing pwnelle and dependencies..."

# Install dependencies
python3 -m pip install pwntools capstone pyelftools ROPgadget python-Levenshtein

# Install pwnelle in development mode
python3 -m pip install -e .

echo "Installation complete. Try running 'pwnelle --help' or 'python3 test_pwnelle.py'" 