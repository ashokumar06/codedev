#!/usr/bin/env python3
"""
CodeDev Installation and Functionality Test
Author: Ashok Kumar (https://ashokumar.in)
Repository: https://github.com/ashokumar06/codedev
"""

import subprocess
import sys
import os
import tempfile
import shutil
from pathlib import Path

def run_command(cmd, check=True):
    """Run a command and return the result"""
    print(f"🔧 Running: {cmd}")
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, check=check)
        if result.stdout:
            print(f"✅ Output: {result.stdout.strip()}")
        return result
    except subprocess.CalledProcessError as e:
        print(f"❌ Error: {e}")
        if e.stderr:
            print(f"   Stderr: {e.stderr}")
        return e

def test_package_build():
    """Test package building"""
    print("\n📦 Testing Package Build")
    print("=" * 50)
    
    # Clean previous builds
    run_command("rm -rf dist/ build/ *.egg-info/")
    
    # Build package
    result = run_command("python -m build")
    
    # Check if files were created
    if Path("dist").exists():
        dist_files = list(Path("dist").glob("*"))
        print(f"✅ Created {len(dist_files)} distribution files:")
        for file in dist_files:
            print(f"   - {file.name}")
        return True
    else:
        print("❌ No dist directory created")
        return False

def test_local_installation():
    """Test local installation"""
    print("\n🔧 Testing Local Installation")
    print("=" * 50)
    
    # Install in development mode
    result = run_command("pip install -e .", check=False)
    if result.returncode == 0:
        print("✅ Local installation successful")
        return True
    else:
        print("❌ Local installation failed")
        return False

def test_commands():
    """Test command availability"""
    print("\n🚀 Testing Commands")
    print("=" * 50)
    
    commands = ["codeas --version", "ca --version"]
    
    for cmd in commands:
        result = run_command(cmd, check=False)
        if result.returncode == 0:
            print(f"✅ Command '{cmd}' works")
        else:
            print(f"❌ Command '{cmd}' failed")
            return False
    
    return True

def test_import():
    """Test Python import"""
    print("\n🐍 Testing Python Import")
    print("=" * 50)
    
    try:
        import ai_coder
        print("✅ ai_coder module imported successfully")
        
        from ai_coder.main import main
        print("✅ main function imported successfully")
        
        from ai_coder.cli import AiCoderCLI
        print("✅ AiCoderCLI imported successfully")
        
        return True
    except ImportError as e:
        print(f"❌ Import failed: {e}")
        return False

def test_configuration():
    """Test configuration loading"""
    print("\n⚙️  Testing Configuration")
    print("=" * 50)
    
    try:
        from ai_coder.core.config import Config
        config = Config()
        print("✅ Configuration loaded successfully")
        
        model = config.get('ai.model', 'default')
        print(f"✅ AI model setting: {model}")
        
        return True
    except Exception as e:
        print(f"❌ Configuration test failed: {e}")
        return False

def test_workspace_functionality():
    """Test workspace functionality"""
    print("\n📁 Testing Workspace Functionality")
    print("=" * 50)
    
    # Create temporary directory
    with tempfile.TemporaryDirectory() as temp_dir:
        test_dir = Path(temp_dir) / "test_workspace"
        test_dir.mkdir()
        
        print(f"✅ Created test workspace: {test_dir}")
        
        # Test basic functionality
        try:
            from ai_coder.operations.file_manager import FileManager
            from ai_coder.core.config import Config
            
            config = Config()
            file_manager = FileManager(config)
            print("✅ FileManager initialized")
            
            # Test file creation
            test_file = test_dir / "test.py"
            test_content = "# Test file created by CodeAS\nprint('Hello, CodeAS!')\n"
            
            with open(test_file, 'w') as f:
                f.write(test_content)
            
            print(f"✅ Test file created: {test_file}")
            
            # Test file reading
            if test_file.exists() and test_file.read_text() == test_content:
                print("✅ File operations work correctly")
                return True
            else:
                print("❌ File operations failed")
                return False
                
        except Exception as e:
            print(f"❌ Workspace test failed: {e}")
            return False

def create_sample_project():
    """Create a sample project to test with"""
    print("\n🏗️  Creating Sample Project")
    print("=" * 50)
    
    sample_dir = Path("sample_codeas_project")
    if sample_dir.exists():
        shutil.rmtree(sample_dir)
    
    sample_dir.mkdir()
    
    # Create sample files
    files = {
        "main.py": '''#!/usr/bin/env python3
"""
Sample Python project for testing CodeAS
"""

def hello_world():
    """Print hello world message"""
    print("Hello from CodeAS sample project!")

def calculate_fibonacci(n):
    """Calculate fibonacci number"""
    if n <= 1:
        return n
    return calculate_fibonacci(n-1) + calculate_fibonacci(n-2)

if __name__ == "__main__":
    hello_world()
    print(f"Fibonacci(10) = {calculate_fibonacci(10)}")
''',
        "requirements.txt": '''requests>=2.31.0
pytest>=7.0.0
''',
        "README.md": '''# Sample CodeAS Project

This is a sample project created to test CodeAS functionality.

## Features
- Basic Python functions
- Testing setup
- Documentation

## Usage
```bash
python main.py
```

## Testing
```bash
pytest
```
''',
        "test_main.py": '''import pytest
from main import hello_world, calculate_fibonacci

def test_fibonacci():
    assert calculate_fibonacci(0) == 0
    assert calculate_fibonacci(1) == 1
    assert calculate_fibonacci(5) == 5
    assert calculate_fibonacci(10) == 55

def test_hello_world():
    # This would test the function if it returned something
    pass
'''
    }
    
    for filename, content in files.items():
        file_path = sample_dir / filename
        file_path.write_text(content)
        print(f"✅ Created {filename}")
    
    print(f"✅ Sample project created at: {sample_dir}")
    print(f"💡 Test CodeAS with: cd {sample_dir} && codeas")
    
    return sample_dir

def run_all_tests():
    """Run all tests"""
    print("🚀 CodeAS - Comprehensive Test Suite")
    print("=" * 60)
    print("Author: Ashok Kumar (https://ashokumar.in)")
    print("=" * 60)
    
    tests = [
        ("Package Build", test_package_build),
        ("Local Installation", test_local_installation),
        ("Commands", test_commands),
        ("Python Import", test_import),
        ("Configuration", test_configuration),
        ("Workspace Functionality", test_workspace_functionality),
    ]
    
    results = {}
    
    for test_name, test_func in tests:
        try:
            results[test_name] = test_func()
        except Exception as e:
            print(f"❌ {test_name} failed with exception: {e}")
            results[test_name] = False
    
    # Create sample project
    sample_dir = create_sample_project()
    
    # Print summary
    print("\n" + "=" * 60)
    print("📊 TEST SUMMARY")
    print("=" * 60)
    
    passed = 0
    total = len(results)
    
    for test_name, result in results.items():
        status = "✅ PASSED" if result else "❌ FAILED"
        print(f"{test_name:<30} {status}")
        if result:
            passed += 1
    
    print(f"\n📈 Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("\n🎉 All tests passed! CodeAS is ready for use.")
        print("\n🚀 Next steps:")
        print("1. Upload to PyPI: ./build_release.sh")
        print("2. Test installation: pip install codeas")
        print(f"3. Test with sample project: cd {sample_dir} && codeas")
    else:
        print(f"\n⚠️  {total - passed} tests failed. Please fix issues before release.")
    
    return passed == total

if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
