#!/bin/bash

# CodeAS Build and Release Script
# Author: Ashok Kumar (https://ashokumar.in)

set -e

echo "🚀 CodeAS - Build and Release Script"
echo "===================================="

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Functions
log_info() {
    echo -e "${BLUE}ℹ️  $1${NC}"
}

log_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

log_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

log_error() {
    echo -e "${RED}❌ $1${NC}"
}

# Check if virtual environment is active
check_venv() {
    if [[ -z "${VIRTUAL_ENV}" ]]; then
        log_warning "No virtual environment detected. Consider activating one."
        read -p "Continue anyway? (y/N): " -n 1 -r
        echo
        if [[ ! $REPLY =~ ^[Yy]$ ]]; then
            exit 1
        fi
    else
        log_success "Virtual environment active: $VIRTUAL_ENV"
    fi
}

# Install build dependencies
install_deps() {
    log_info "Installing build dependencies..."
    pip install --upgrade pip
    pip install build twine wheel setuptools
    log_success "Build dependencies installed"
}

# Clean previous builds
clean_build() {
    log_info "Cleaning previous builds..."
    rm -rf dist/ build/ *.egg-info/
    find . -name "*.pyc" -delete
    find . -name "__pycache__" -type d -exec rm -rf {} + 2>/dev/null || true
    log_success "Build artifacts cleaned"
}

# Build package
build_package() {
    log_info "Building package..."
    python -m build
    log_success "Package built successfully"
}

# Check package
check_package() {
    log_info "Checking package integrity..."
    twine check dist/*
    log_success "Package check passed"
}

# Show package info
show_package_info() {
    log_info "Package information:"
    echo "==================="
    ls -la dist/
    echo
    log_info "Package contents:"
    tar -tzf dist/*.tar.gz | head -20
}

# Upload to TestPyPI
upload_test() {
    log_warning "Uploading to TestPyPI..."
    read -p "Continue with TestPyPI upload? (y/N): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        twine upload --repository testpypi dist/*
        log_success "Uploaded to TestPyPI"
        log_info "Test with: pip install --index-url https://test.pypi.org/simple/ codeas"
    fi
}

# Upload to PyPI
upload_pypi() {
    log_warning "Uploading to PyPI (PRODUCTION)..."
    log_warning "This will make the package publicly available!"
    read -p "Are you sure you want to upload to PyPI? (y/N): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        twine upload dist/*
        log_success "Uploaded to PyPI"
        log_info "Install with: pip install codeas"
    fi
}

# Test local installation
test_installation() {
    log_info "Testing local installation..."
    pip install -e .
    codeas --version
    ca --version
    log_success "Local installation test passed"
}

# Main script
main() {
    echo
    log_info "Starting CodeAS build process..."
    
    check_venv
    install_deps
    clean_build
    test_installation
    build_package
    check_package
    show_package_info
    
    echo
    log_info "Build completed successfully!"
    
    # Ask for upload options
    echo
    echo "Upload options:"
    echo "1) Test with TestPyPI"
    echo "2) Upload to PyPI (Production)"
    echo "3) Skip upload"
    read -p "Choose option (1-3): " -n 1 -r
    echo
    
    case $REPLY in
        1)
            upload_test
            ;;
        2)
            upload_pypi
            ;;
        3)
            log_info "Skipping upload"
            ;;
        *)
            log_warning "Invalid option, skipping upload"
            ;;
    esac
    
    echo
    log_success "🎉 CodeAS build and release process completed!"
    log_info "Author: Ashok Kumar (https://ashokumar.in)"
}

# Run main function
main "$@"
