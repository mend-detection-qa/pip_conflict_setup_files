# Test Case: Pip setup.py vs setup.cfg Conflict

## Package Manager
Pip

## Python Version Detection
- **Source**: setup.py (PRIORITY #5)
- **Expected Version**: >=3.9
- **Conflict**: setup.cfg says >=3.10 (PRIORITY #6 - lower)

## Files Present
- setup.py - python_requires=">=3.9" (SHOULD WIN)
- setup.cfg - python_requires = >=3.10 (SHOULD BE IGNORED)
- requirements.txt

## Test Purpose
Test priority between setup.py and setup.cfg files.
