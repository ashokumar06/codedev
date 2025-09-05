# CodeDev Development Guide

## Quick Setup

```bash
# Clone the repository
git clone https://github.com/ashokumar06/codedev.git
cd codedev

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install in development mode
pip install -e .

# Test the installation
codedev --version
cdev --version
```

## Development Commands

```bash
# Run tests
python test_installation.py

# Build package
python -m build

# Install locally
pip install -e .

# Clean build artifacts
rm -rf build/ dist/ *.egg-info/
```

## Project Structure

```
codedev/
├── ai_coder/           # Main package
│   ├── ai/            # AI client integration
│   ├── core/          # Core configuration
│   ├── operations/    # File and project management
│   ├── prompts/       # AI system prompts
│   ├── safety/        # Safe command execution
│   └── utils/         # Utilities and logging
├── config/            # Default configuration
├── tests/             # Test suite
├── .github/           # GitHub workflows
└── setup.py           # Package configuration
```

## Release Process

1. Update version in `setup.py`
2. Create a GitHub release
3. GitHub Actions automatically builds and publishes to PyPI

## Links

- **Repository**: https://github.com/ashokumar06/codedev
- **PyPI Package**: https://pypi.org/project/codedev/
- **Author**: [Ashok Kumar](https://ashokumar.in)
