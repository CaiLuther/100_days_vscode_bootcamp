# 100 Days of Code — VS Code Starter

This folder gives you a minimal, comfy VS Code setup for the Python course.

## 1) Open in VS Code
- **File → Open Folder...** and choose this folder.

## 2) Create & select a virtual environment
- **Windows (PowerShell):**
  ```powershell
  py -3 -m venv .venv
  .\.venv\Scripts\Activate.ps1
  ```
- **macOS / Linux:**
  ```bash
  python3 -m venv .venv
  source .venv/bin/activate
  ```
- Press **Ctrl/Cmd+Shift+P** → **Python: Select Interpreter** → choose `.venv`.

## 3) Install minimal tools
```bash
pip install -r requirements.txt
```

## 4) Run the first script
Open `day01/main.py` and press **F5** (or run in the Terminal):
```bash
python day01/main.py
```

### Notes
- The `.vscode` folder already configures:
  - **Black** formatting on save
  - **Ruff** linting/fix on save
  - **Debug** configs for current file, Flask, and pytest
- If the course asks for additional libraries (e.g., `requests`, `beautifulsoup4`, `flask`, `pandas`), just install them in your venv:
  ```bash
  pip install requests beautifulsoup4 flask pandas
  ```
# 100_days_vscode_bootcamp
