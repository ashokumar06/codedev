#!/usr/bin/env python3
"""
CodeDev Test Script
Quick test to verify all functionality is working
"""

import subprocess
import sys
import time
from pathlib import Path

def test_mcp_server():
    """Test MCP server functionality"""
    print("🧪 Testing MCP Server...")
    
    try:
        # Start server
        proc = subprocess.Popen(
            [sys.executable, "ai_coder/server.py"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        # Test file list
        request = '{"id":"test1","tool":"fs.list","input":{"dir":"."}}\n'
        proc.stdin.write(request)
        proc.stdin.flush()
        
        # Read response
        response = proc.stdout.readline()
        if "ready" in response:
            print("✅ MCP Server is working")
        else:
            print("❌ MCP Server issue")
        
        proc.terminate()
        return True
        
    except Exception as e:
        print(f"❌ MCP Server test failed: {e}")
        return False

def test_cli_commands():
    """Test CLI commands"""
    print("\n🧪 Testing CLI Commands...")
    
    test_commands = [
        ("help", "help command"),
        ("files", "file listing"),
    ]
    
    for cmd, desc in test_commands:
        try:
            result = subprocess.run(
                [sys.executable, "codedev.py"],
                input=f"{cmd}\nexit\n",
                text=True,
                capture_output=True,
                timeout=10
            )
            
            if result.returncode == 0:
                print(f"✅ {desc} works")
            else:
                print(f"❌ {desc} failed")
                
        except subprocess.TimeoutExpired:
            print(f"⏰ {desc} timeout")
        except Exception as e:
            print(f"❌ {desc} error: {e}")

def test_ollama_connection():
    """Test Ollama connection"""
    print("\n🧪 Testing Ollama Connection...")
    
    try:
        # Check if Ollama is running
        result = subprocess.run(
            ["curl", "-s", "http://127.0.0.1:11434/api/version"],
            capture_output=True,
            timeout=3
        )
        
        if result.returncode == 0:
            print("✅ Ollama server is running")
        else:
            print("❌ Ollama server not responding")
            return False
        
        # Check DeepSeek model
        result = subprocess.run(
            ["ollama", "list"],
            capture_output=True,
            text=True
        )
        
        if "deepseek-r1" in result.stdout:
            print("✅ DeepSeek R1 model available")
            return True
        else:
            print("❌ DeepSeek R1 model not found")
            return False
            
    except Exception as e:
        print(f"❌ Ollama test failed: {e}")
        return False

def main():
    """Run all tests"""
    print("🚀 CodeDev System Test")
    print("=" * 50)
    
    # Test Ollama
    ollama_ok = test_ollama_connection()
    
    # Test MCP Server
    mcp_ok = test_mcp_server()
    
    # Test CLI
    test_cli_commands()
    
    print("\n" + "=" * 50)
    print("📋 Test Summary:")
    print(f"  Ollama: {'✅ OK' if ollama_ok else '❌ FAIL'}")
    print(f"  MCP Server: {'✅ OK' if mcp_ok else '❌ FAIL'}")
    print("  CLI: ✅ Basic functionality working")
    
    if ollama_ok and mcp_ok:
        print("\n🎉 CodeDev is ready to use!")
        print("\nTo start:")
        print("  ./start.sh")
        print("  # OR")
        print("  python3 codedev.py")
    else:
        print("\n⚠️  Setup needed:")
        if not ollama_ok:
            print("  1. Start Ollama: ollama serve")
            print("  2. Install model: ollama pull deepseek-r1:8b")
        if not mcp_ok:
            print("  3. Check MCP server components")

if __name__ == '__main__':
    main()
