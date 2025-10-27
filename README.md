# inventory_system
# # Inventory System – Static Code Analysis (Lab 5)

## Overview
A Python program that manages an inventory of items — allowing users to add, remove, save, and load data securely.  
All code was analyzed and cleaned using **Pylint**, **Flake8**, and **Bandit** to ensure high quality, security, and PEP 8 compliance.

---

## Tools Used
| Tool | Purpose |
|------|----------|
| **Pylint** | Detects code quality and logic issues |
| **Flake8** | Checks formatting and PEP 8 style |
| **Bandit** | Scans for security vulnerabilities |

---

## Setup
Install required tools:
```bash
pip install pylint flake8 bandit

## Run the program:
python clean_inventory_system.py

##Run static analysis:

pylint clean_inventory_system.py
flake8 clean_inventory_system.py
bandit -r clean_inventory_system.py

Issues Fixed
Issue	Tool	Fix
Mutable default argument	Pylint	Replaced with None
Broad exception	Bandit / Pylint	Used KeyError instead of except:
Insecure eval() usage	Bandit	Removed
File handling	Pylint	Added with open()
Missing docstrings	Pylint	Added docstrings to all functions
Style / newline issues	Flake8	Fixed line endings & formatting