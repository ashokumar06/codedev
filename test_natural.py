#!/usr/bin/env python3
"""
Test the natural language processing in AI Coder
"""

import sys
import os
sys.path.insert(0, '.')

from ai_coder.cli import AiCoderCLI
from ai_coder.core.config import Config

def test_natural_language():
    """Test natural language processing"""
    print("🧪 Testing Natural Language Commands\n")
    
    config = Config()
    cli = AiCoderCLI(config)
    
    # Test various natural language inputs
    test_inputs = [
        "hi",
        "create a web server", 
        "show @app.py",
        "fix @test.py",
        "# todo add authentication",
        "what files do I have?",
        "thanks"
    ]
    
    print("Testing natural language patterns:")
    for test_input in test_inputs:
        print(f"\n📝 Input: '{test_input}'")
        try:
            # Test the natural language handler
            result = cli._handle_natural_language(test_input)
            print(f"   ✅ Handled: {result}")
        except Exception as e:
            print(f"   ❌ Error: {e}")
    
    print("\n✅ Natural language testing complete!")
    print("\n💡 Now you can use conversational commands like:")
    print("   • 'create a web server'")
    print("   • 'fix @app.py'") 
    print("   • 'show my files'")
    print("   • '# todo add auth'")

if __name__ == "__main__":
    test_natural_language()
