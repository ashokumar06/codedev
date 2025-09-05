#!/usr/bin/env python3
"""
Demo script to test AI Coder functionality
"""

import sys
import os
sys.path.insert(0, '.')

from ai_coder.core.config import Config
from ai_coder.operations.file_manager import FileManager
from ai_coder.utils.logger import setup_logging

def test_basic_functionality():
    """Test basic functionality without AI"""
    print("🧪 Testing AI Coder Basic Functionality\n")
    
    # Setup logging
    setup_logging(debug=True)
    
    # Test 1: Configuration
    print("1. Testing Configuration...")
    config = Config()
    print(f"   ✅ Default model: {config.ai.model}")
    print(f"   ✅ History dir: {config.workspace.history_dir}")
    
    # Test 2: File Manager
    print("\n2. Testing File Manager...")
    file_manager = FileManager(config)
    
    # Create test file
    test_file = "demo_test.txt"
    content1 = "Hello, World! Version 1"
    
    success = file_manager.write_file(test_file, content1, create_backup=False)
    print(f"   ✅ Created file: {success}")
    
    # Read file
    read_content = file_manager.read_file(test_file)
    print(f"   ✅ Read file: {read_content == content1}")
    
    # Update file (creates backup)
    content2 = "Hello, World! Version 2"
    file_manager.write_file(test_file, content2)
    
    # Check history
    history = file_manager.get_file_history(test_file)
    print(f"   ✅ History entries: {len(history)}")
    
    # Test undo
    undo_success = file_manager.undo_last_change(test_file)
    print(f"   ✅ Undo worked: {undo_success}")
    
    # Verify undo
    after_undo = file_manager.read_file(test_file)
    print(f"   ✅ Content after undo: {after_undo == content1}")
    
    # Cleanup
    if os.path.exists(test_file):
        os.remove(test_file)
    
    print("\n✅ All basic tests passed!")
    print("\n🚀 AI Coder is ready to use!")
    print("\nTo start the CLI:")
    print("   python main.py")
    print("   or")
    print("   ./start.sh")

if __name__ == "__main__":
    test_basic_functionality()
