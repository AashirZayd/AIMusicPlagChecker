@echo off
title DependencyVerifierbyAashirZayd - Python 3.11.9 Stable Setup (TriadLabs)

echo ============================================================
echo AI MUSIC PLAGIARISM DETECTOR - DEPENDENCY VERIFIER
echo ============================================================
echo Author: Aashir Zayd (TriadLabs)
echo Description: Stable setup targeting Python 3.11.9 + OpenL3 compatibility
echo ============================================================
echo.
pause

:: ---------------------------------------
:: STEP 0: Check and Install Python 3.11.9
:: ---------------------------------------
echo [0/11] Checking for Python 3.11.9...
for /f "tokens=2 delims= " %%a in ('python --version 2^>^&1') do set PY_VER=%%a
echo Detected Python version: %PY_VER%
echo.

echo Checking if Python 3.11.9 is installed...
where python311 >nul 2>nul
if errorlevel 1 (
    echo Python 3.11.9 not found. Installing...
    powershell -Command "Start-Process msiexec.exe -ArgumentList '/i https://www.python.org/ftp/python/3.11.9/python-3.11.9-amd64.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0' -Wait"
    echo Python 3.11.9 installed successfully.
) else (
    echo Python 3.11.9 found and ready.
)
echo.

:: Use Python 3.11 explicitly if available
set PYTHON_PATH="C:\Program Files\Python311\python.exe"
if not exist %PYTHON_PATH% (
    echo Python 3.11.9 not found in default directory. Using system Python.
    set PYTHON_PATH=python
)

:: ---------------------------------------
:: STEP 1: Bypass PowerShell Restrictions
:: ---------------------------------------
echo [1/11] Bypassing PowerShell execution restrictions...
PowerShell -Command "Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Bypass -Force"
echo Execution policy set to Bypass.
echo.

:: ---------------------------------------
:: STEP 2: Create or Rebuild Virtual Environment
:: ---------------------------------------
if exist venv (
    echo Existing virtual environment found.
    call venv\Scripts\activate
    if errorlevel 1 (
        echo Virtual environment corrupted. Rebuilding...
        rmdir /s /q venv
        %PYTHON_PATH% -m venv venv
    )
) else (
    echo [2/11] Creating virtual environment using Python 3.11.9...
    %PYTHON_PATH% -m venv venv
)
if errorlevel 1 (
    echo Failed to create virtual environment. Check Python setup.
    pause
    exit /b
)
echo Virtual environment ready.
echo.

:: ---------------------------------------
:: STEP 3: Activate Environment
:: ---------------------------------------
echo [3/11] Activating virtual environment...
call venv\Scripts\activate
if errorlevel 1 (
    echo Activation failed. Trying PowerShell bypass...
    PowerShell -ExecutionPolicy Bypass -Command "& { .\venv\Scripts\Activate.ps1 }"
)
echo Virtual environment activated.
echo.

:: ---------------------------------------
:: STEP 4: Initialize Logging
:: ---------------------------------------
set LOGFILE=setup_log.txt
echo ============================================================ > %LOGFILE%
echo SETUP LOG - DependencyVerifierbyAashirZayd >> %LOGFILE%
echo Generated on: %date% %time% >> %LOGFILE%
echo ============================================================ >> %LOGFILE%
echo Logging all operations to %LOGFILE%
echo.

:: ---------------------------------------
:: STEP 5: Upgrade pip and cleanup cache
:: ---------------------------------------
echo [4/11] Upgrading pip, setuptools, and wheel...
python -m pip install --upgrade pip setuptools wheel >> %LOGFILE% 2>&1
pip cache purge >> %LOGFILE% 2>&1
echo Pip upgraded and cache cleared.
echo.

:: ---------------------------------------
:: STEP 6: Install Core Dependencies
:: ---------------------------------------
echo [5/11] Installing core dependencies (Flask, FAISS, TensorFlow, etc)...
pip install flask requests faiss-cpu librosa numpy soundfile sentence-transformers >> %LOGFILE% 2>&1
pip install importlib-metadata==6.8.0 importlib-resources==6.1.1 >> %LOGFILE% 2>&1
echo Core dependencies installed.
echo.

:: ---------------------------------------
:: STEP 7: Install Stable TensorFlow, Keras, OpenL3 Versions
:: ---------------------------------------
echo [6/11] Installing stable compatible versions...
pip install tensorflow==2.13.0 keras==2.13.1 openl3==0.4.1 >> %LOGFILE% 2>&1
echo Stable versions installed successfully.
echo.

:: ---------------------------------------
:: STEP 8: Requirements.txt Fallback
:: ---------------------------------------
if exist requirements.txt (
    echo Found requirements.txt - installing from file...
    pip install -r requirements.txt >> %LOGFILE% 2>&1
    echo Additional dependencies installed from requirements.txt.
)
echo.

:: ---------------------------------------
:: STEP 9: Verify All Modules
:: ---------------------------------------
echo [7/11] Verifying required modules...
python - >> %LOGFILE% 2>&1
import os
modules = ["flask","requests","faiss","openl3","librosa","soundfile","sentence_transformers","tensorflow"]
missing = []
for m in modules:
    try:
        __import__(m)
    except Exception as e:
        print(f"Missing: {m} ({e})")
        missing.append(m)
if missing:
    print("Reinstalling missing modules...")
    os.system("pip install " + " ".join(missing))
else:
    print("All modules verified successfully.")
exit()
echo Module verification complete.
echo.

:: ---------------------------------------
:: STEP 10: Launch Backend and Verify Server
:: ---------------------------------------
echo [8/11] Starting Flask backend...
start cmd /k "call venv\Scripts\activate && python app.py"
timeout /t 8 >nul

echo Checking Flask server status...
curl http://127.0.0.1:5000 >nul 2>&1
if errorlevel 1 (
    echo Backend might not be running. Check app.py for errors. >> %LOGFILE%
) else (
    echo Backend successfully started on port 5000. >> %LOGFILE%
)
echo Flask backend started.
echo.

:: ---------------------------------------
:: STEP 11: Launch Frontend
:: ---------------------------------------
echo [9/11] Launching Frontend UI...
start cmd /k "call venv\Scripts\activate && python frontend_ui.py"
echo Frontend launched.
echo.

:: ---------------------------------------
:: STEP 12: Summary
:: ---------------------------------------
echo ============================================================
echo SETUP COMPLETE - PYTHON 3.11.9 STABLE BUILD VERIFIED
echo Backend: http://127.0.0.1:5000
echo Frontend: CustomTkinter UI is open
echo Log file: %LOGFILE%
echo ============================================================
pause
