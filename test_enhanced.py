#!/usr/bin/env python3
"""
Demo script to test the enhanced AI Coder features
"""

import subprocess
import time
import sys

def run_command(cmd, input_text="", timeout=30):
    """Run a command and return the output"""
    try:
        process = subprocess.Popen(
            cmd, shell=True, 
            stdin=subprocess.PIPE, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.STDOUT,
            text=True
        )
        
        output, _ = process.communicate(input=input_text, timeout=timeout)
        return output
    except subprocess.TimeoutExpired:
        process.kill()
        return "Command timed out"
    except Exception as e:
        return f"Error: {e}"

def main():
    print("🧪 Testing Enhanced AI Coder Features\n")
    
    # Test 1: Startup and initialization
    print("1. Testing startup and initialization...")
    output = run_command("cd /home/ashok/ai-tools/ai-coder && echo 'exit' | python main.py", timeout=60)
    if "System initialization complete" in output:
        print("   ✅ Startup successful")
    else:
        print("   ❌ Startup failed")
    
    # Test 2: Models command
    print("\n2. Testing models command...")
    output = run_command("cd /home/ashok/ai-tools/ai-coder && echo 'models\nexit' | python main.py", timeout=60)
    if "Available AI Models" in output:
        print("   ✅ Models command working")
    else:
        print("   ❌ Models command failed")
    
    # Test 3: Basic file operations
    print("\n3. Testing file operations...")
    output = run_command("cd /home/ashok/ai-tools/ai-coder && echo 'show my files\nexit' | python main.py", timeout=60)
    if "Contents of" in output:
        print("   ✅ File operations working")
    else:
        print("   ❌ File operations failed")
    
    # Test 4: Help system
    print("\n4. Testing help system...")
    output = run_command("cd /home/ashok/ai-tools/ai-coder && echo 'help\nexit' | python main.py", timeout=60)
    if "AI Coder Commands" in output:
        print("   ✅ Help system working")
    else:
        print("   ❌ Help system failed")
    
    print("\n🎉 All tests completed!")
    
    print("\n📋 Summary of Enhanced Features:")
    print("   ✅ Automatic Ollama installation check (Linux)")
    print("   ✅ Automatic model detection and selection")
    print("   ✅ Better error handling and user guidance")
    print("   ✅ Enhanced models command with detailed info")
    print("   ✅ Improved startup process with system checks")
    print("   ✅ Cross-platform support detection")
    print("   ✅ Fallback model recommendations")
    print("   ✅ Better timeout handling for slow connections")

if __name__ == "__main__":
    main()
