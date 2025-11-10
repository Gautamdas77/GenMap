@echo off
REM Learning Roadmap Generator - Quick Start Script for Windows

echo.
echo ========================================
echo  Learning Roadmap Generator
echo  Quick Start Script
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python from https://www.python.org
    pause
    exit /b 1
)

echo [1/4] Checking virtual environment...
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
) else (
    echo Virtual environment already exists.
)

echo.
echo [2/4] Activating virtual environment...
call venv\Scripts\activate.bat

echo.
echo [3/4] Installing dependencies...
pip install -r requirements.txt --quiet

echo.
echo [4/4] Checking .env file...
if not exist ".env" (
    echo .env file not found!
    echo Creating .env file from template...
    copy .env.example .env
    echo.
    echo ⚠️  IMPORTANT: Please edit .env and add your GOOGLE_API_KEY
    echo Get your key from: https://makersuite.google.com/app/apikey
    echo.
    pause
)

echo.
echo ========================================
echo  Starting Learning Roadmap Generator...
echo ========================================
echo.

streamlit run main.py

pause
