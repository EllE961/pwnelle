#!/bin/bash
set -e

# Clean previous builds
echo "Cleaning previous build artifacts..."
rm -rf build/ dist/ *.egg-info/

# Install required build tools
echo "Installing build tools..."
pip install --upgrade pip
pip install --upgrade build twine wheel

# Build the package
echo "Building the package..."
python -m build

# Check the distribution files
echo "Checking distribution files with twine..."
twine check dist/*

echo "Build complete! To publish to PyPI, run:"
echo "twine upload dist/*"
echo ""
echo "Or to upload to TestPyPI first:"
echo "twine upload --repository-url https://test.pypi.org/legacy/ dist/*" 