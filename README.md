# 🤖 Task Automation with Python & PyAutoGUI

![Python](https://img.shields.io/badge/python-3.12+-blue.svg?logo=python&logoColor=white)
![Venv](https://img.shields.io/badge/venv-isolated-blue?logo=python&logoColor=white)
![PyAutoGUI](https://img.shields.io/badge/PyAutoGUI-3776AB?style=flat&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white)
![Platform](https://img.shields.io/badge/OS-Linux%20%7C%20Windows-lightgrey.svg)

This project features a GUI (Graphical User Interface) automation bot designed for bulk product processing and registration from databases. The system was engineered with a focus on **resilience**, **traceability**, and **security**.

## 🚀 Technologies
  
- **Python 3.12+**: Core language.
- **PyAutoGUI**: GUI automation (mouse and keyboard interaction).
- **Pandas**: Data processing and manipulation using DataFrames.
- **Virtualenv (venv)**: Development environment isolation.
- **Logging**: Rotating file log system for auditing purposes.

## 📦 Environment Management

### Why use venv?
In Linux environments (especially distributions like **Pop!_OS** and Ubuntu), the global Python environment is system-managed (PEP 668). Using a Virtual Environment (venv) is essential to prevent conflicts with the OS and ensure project portability.

### Step-by-Step Configuration:

```bash
# 1. Create the virtual environment
python3 -m venv venv

# 2. Activate the environment
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt
```

```bash
# 4. Deactivate the environment
deactivate
```

## ⚙️ Configuration & Environment Variables

The project utilizes a .env file to protect sensitive information and configure file paths. Never commit your .env file to the repository.

Create a .env file in the project root following this template:

```
BROWSER=google-chrome
URL_FORM=https://dlp.hashtagtreinamentos.com/python/intensivao/login
LOGIN=your_username
PASSWORD=your_password
CSV_FILENAME=produtos.csv
```

## ⚠️ Security & Resilience

- **Fail-Safe**: To abort the script immediately, move the mouse cursor to the top-left corner of the screen. The bot will catch the FailSafeException and terminate safely.
- **Audit Logging**: The system generates logs in logs/automation.log with automatic file rotation. Every registration is recorded with both an "intent" log and a "confirmation" (success) log.
- **Error Handling**: Differentiated exception handling for common row failures (skip and log warning) and critical system failures (safe shutdown).

## 📂 File Structure

- **bot.py**: Automation core (data parsing, login, and registration logic).
- **get_position.py**: Utility script to identify X and Y screen coordinates.
- **logs/**: Directory containing execution history (ignored by Git).
- **.gitignore**: Configured to exclude venv/, .env, and log files.
- **requirements.txt**: Dependency manifest for environment replication.
- **produtos.csv**: Example database file used in class (Portuguese).
