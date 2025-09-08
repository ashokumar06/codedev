#!/usr/bin/env python3
"""
CodeDev MCP Server
Simple JSON-over-stdio server for integration with other tools
"""

import sys
import os
from pathlib import Path

# Add ai_coder to path
sys.path.insert(0, str(Path(__file__).parent / "ai_coder"))

def main():
    """Run the MCP server"""
    os.chdir(Path(__file__).parent / "ai_coder")
    from server import main as server_main
    server_main()

if __name__ == '__main__':
    main()
