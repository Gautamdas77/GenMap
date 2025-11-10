#!/bin/bash
# Learning Roadmap Generator - Quick Start Script for macOS/Linux

echo ""
echo "========================================"
echo " Learning Roadmap Generator"
echo " Quick Start Script"
echo "========================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed"
    echo "Please install Python from https://www.python.org"
    exit 1
fi

echo "[1/4] Checking virtual environment..."
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
else
    echo "Virtual environment already exists."
fi

echo ""
echo "[2/4] Activating virtual environment..."
source venv/bin/activate

echo ""
echo "[3/4] Installing dependencies..."
pip install -r requirements.txt --quiet

echo ""
echo "[4/4] Checking .env file..."
if [ ! -f ".env" ]; then
    echo ".env file not found!"
    echo "Creating .env file from template..."
    cp .env.example .env
    echo ""
    echo "⚠️  IMPORTANT: Please edit .env and add your GOOGLE_API_KEY"
    echo "Get your key from: https://makersuite.google.com/app/apikey"
    echo ""
    read -p "Press enter to continue..."
fi

echo ""
echo "========================================"
echo " Starting Learning Roadmap Generator..."
echo "========================================"
echo ""

streamlit run main.py
