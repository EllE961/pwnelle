#!/usr/bin/env python3
"""
Test script for pwnelle installation.
"""

import os
import sys

print("Testing pwnelle installation...\n")

try:
    from pwnelle import __version__
    print(f"Successfully imported pwnelle version {__version__}")
except ImportError as e:
    print(f"Error importing pwnelle: {e}")
    print("Try installing with: python -m pip install -e .")
    sys.exit(1)

print("\nChecking dependencies:")

dependencies = [
    ('pwntools', 'pwn'),
    ('pyelftools', 'elftools'),
    ('capstone', 'capstone'),
    ('ROPgadget', 'ROPgadget'),
    ('Levenshtein', 'Levenshtein'),
]

for package_name, import_name in dependencies:
    try:
        __import__(import_name)
        print(f"  [+] {package_name} found")
    except ImportError:
        print(f"  [-] {package_name} not found. Install with: pip install {package_name}")

print("\nAll done! Try running 'pwnelle --help' to verify the command works.") 