# PyPI Release Configuration for CodeAS

# .pypirc file content (place in ~/.pypirc)
[distutils]
index-servers = pypi

[pypi]
username = __token__
password = <your-pypi-api-token>

# Building and uploading to PyPI

## 1. Install build tools
pip install build twine wheel

## 2. Clean previous builds
rm -rf dist/ build/ *.egg-info/

## 3. Build package
python -m build

## 4. Check package
twine check dist/*

## 5. Upload to TestPyPI (optional)
twine upload --repository testpypi dist/*

## 6. Upload to PyPI
twine upload dist/*

## 7. Install from PyPI
pip install codeas

## 8. Test installation
codeas --version
ca --version

# Version bumping
# Update version in setup.py before each release
# Follow semantic versioning: MAJOR.MINOR.PATCH
