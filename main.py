#!/usr/bin/env python3
"""
AI Coder - Advanced CLI REPL Agent
Entry point for the application
"""

import sys
import os
import argparse
from pathlib import Path

# Add the ai_coder module to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'ai_coder'))

from ai_coder.cli import AiCoderCLI
from ai_coder.core.config import Config
from ai_coder.utils.logger import setup_logging

def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description="AI Coder - Advanced CLI REPL Agent",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument(
        '--config', '-c',
        type=str,
        help='Path to config file'
    )
    
    parser.add_argument(
        '--model', '-m',
        type=str,
        help='AI model to use'
    )
    
    parser.add_argument(
        '--workspace', '-w',
        type=str,
        help='Workspace directory'
    )
    
    parser.add_argument(
        '--debug', '-d',
        action='store_true',
        help='Enable debug logging'
    )
    
    parser.add_argument(
        '--version', '-v',
        action='version',
        version='AI Coder v1.0.0'
    )

    args = parser.parse_args()
    
    # Setup logging
    setup_logging(debug=args.debug)
    
    # Initialize configuration
    config = Config(config_file=args.config)
    
    # Override config with command line args
    if args.model:
        config.set('ai.model', args.model)
    
    if args.workspace:
        config.set('workspace.directory', args.workspace)
    
    # Initialize and start CLI
    try:
        cli = AiCoderCLI(config)
        cli.run()
    except KeyboardInterrupt:
        print("\n👋 Goodbye!")
        sys.exit(0)
    except Exception as e:
        print(f"❌ Fatal error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
