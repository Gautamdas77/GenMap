"""
Verification script to check if all dependencies are installed correctly
Run this to verify your environment is set up properly
"""

import sys
import os

def check_python_version():
    """Check if Python version is 3.8 or higher"""
    version = sys.version_info
    print(f"✓ Python Version: {version.major}.{version.minor}.{version.micro}")
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("✗ ERROR: Python 3.8+ required")
        return False
    return True


def check_imports():
    """Check if all required packages are installed"""
    required_packages = {
        'streamlit': 'Streamlit (UI Framework)',
        'google.generativeai': 'Google Generative AI',
        'dotenv': 'python-dotenv (Environment Variables)',
        'pydantic': 'Pydantic (Data Validation)',
    }
    
    all_ok = True
    for package, name in required_packages.items():
        try:
            __import__(package)
            print(f"✓ {name} installed")
        except ImportError:
            print(f"✗ {name} NOT installed")
            all_ok = False
    
    return all_ok


def check_env_file():
    """Check if .env file exists and has API key"""
    if not os.path.exists('.env'):
        print("✗ .env file NOT found")
        print("  → Copy .env.example to .env and add your API key")
        return False
    
    print("✓ .env file found")
    
    # Check if API key is set
    api_key = os.getenv('GOOGLE_API_KEY')
    if not api_key:
        print("✗ GOOGLE_API_KEY not set in .env")
        print("  → Add your API key: GOOGLE_API_KEY=your_key_here")
        return False
    
    if api_key == 'your_api_key_here':
        print("✗ GOOGLE_API_KEY is still the default value")
        print("  → Replace with your actual API key")
        return False
    
    print("✓ GOOGLE_API_KEY is set")
    return True


def check_project_files():
    """Check if all required project files exist"""
    required_files = {
        'main.py': 'Main Application',
        'config.py': 'Configuration',
        'utils/ai_service.py': 'AI Service',
        'utils/validators.py': 'Validators',
        'utils/roadmap_parser.py': 'Roadmap Parser',
        'requirements.txt': 'Requirements',
    }
    
    all_ok = True
    for file, name in required_files.items():
        if os.path.exists(file):
            print(f"✓ {name} ({file})")
        else:
            print(f"✗ {name} ({file}) NOT found")
            all_ok = False
    
    return all_ok


def check_documentation():
    """Check if documentation files exist"""
    doc_files = {
        'README.md': 'Main README',
        'SETUP_GUIDE.md': 'Setup Guide',
        'QUICKSTART.md': 'Quick Start Guide',
        'START_HERE.md': 'Start Here Guide',
    }
    
    all_ok = True
    for file, name in doc_files.items():
        if os.path.exists(file):
            print(f"✓ {name}")
        else:
            print(f"⚠ {name} missing (optional)")
            all_ok = False
    
    return all_ok


def main():
    """Run all checks"""
    print("\n" + "="*50)
    print(" Learning Roadmap Generator - Verification")
    print("="*50 + "\n")
    
    all_ok = True
    
    # Check Python version
    print("Checking Python Version...")
    if not check_python_version():
        all_ok = False
    print()
    
    # Check imports
    print("Checking Required Packages...")
    if not check_imports():
        all_ok = False
    print()
    
    # Check .env file
    print("Checking Configuration...")
    if not check_env_file():
        all_ok = False
    print()
    
    # Check project files
    print("Checking Project Files...")
    if not check_project_files():
        all_ok = False
    print()
    
    # Check documentation
    print("Checking Documentation...")
    check_documentation()  # This is optional
    print()
    
    # Summary
    print("="*50)
    if all_ok:
        print("✓ All checks passed!")
        print("\nYou're ready to run:")
        print("  streamlit run main.py")
        print("\nOr use:")
        print("  run.bat (Windows)")
        print("  bash run.sh (Mac/Linux)")
    else:
        print("✗ Some checks failed")
        print("\nTo fix:")
        print("1. Install missing packages: pip install -r requirements.txt")
        print("2. Create .env from .env.example: cp .env.example .env")
        print("3. Add your API key to .env")
        print("4. Run this script again")
    
    print("="*50 + "\n")
    
    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(main())
