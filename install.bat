@echo off
REM Simple installation script for pwnelle on Windows

echo Installing pwnelle and dependencies...

REM Install dependencies
python -m pip install pwntools capstone pyelftools ROPgadget python-Levenshtein

REM Install pwnelle in development mode
python -m pip install -e .

echo Installation complete. Try running 'pwnelle --help' or 'python test_pwnelle.py'
pause 