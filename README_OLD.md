# AI Coder - Advanced CLI REPL Agent

An intelligent, persistent CLI coding assistant powered by Ollama with advanced project management capabilities and **natural language processing**.

## Features

- 🤖 **AI-Powered Code Generation** - Create, edit, and refactor code using Ollama
- � **Natural Language Interface** - Talk naturally: "create a web server", "fix @app.py"
- �📁 **Project-Level Intelligence** - Generate and manage multi-file projects
- 🔄 **Advanced History & Undo/Redo** - Every action logged with complete rollback
- 🛡️ **Safe Command Execution** - Whitelisted commands only for security
- 🎨 **Rich Terminal Interface** - Beautiful, interactive CLI with syntax highlighting
- 📊 **Project Analytics** - Code metrics, file structure visualization
- 🔧 **Cross-File Refactoring** - Intelligent multi-file code updates
- 💾 **Persistent Sessions** - Always running in a folder with session memory

## Installation

```bash
pip install -r requirements.txt
python main.py
```

## Natural Language Commands

### 🗣️ Talk Naturally
```bash
# Casual conversation
hi
thanks
what files do I have?

# File operations with @ syntax
show @app.py
fix @server.js
update @config.py add database settings
edit @app.py add error handling

# Comments and todos with # syntax
# todo add authentication
# reminder: test the API
# note: this needs refactoring

# Natural file creation
create a web server
make a React app
build a Python script for file processing
```

### 📋 Structured Commands

#### File Operations
- `create <file> <lang> <prompt>` - Create new file with AI
- `edit <file> <lang> <prompt>` - Edit existing file
- `refactor <file> <lang> <prompt>` - Refactor code
- `show <file>` - Display file contents
- `delete <file>` - Delete file (with history backup)
- `move <src> <dest>` - Move/rename file
- `copy <src> <dest>` - Copy file

#### Project Operations
- `create-project <type> <name> <description>` - Generate full project
- `analyze-project` - Show project structure and metrics
- `refactor-project <instructions>` - Cross-file refactoring
- `test-project` - Run project tests
- `build-project` - Build/compile project

### Directory Operations
- `ls [path]` - List files/directories
- `tree [depth]` - Show directory tree
- `mkdir <path>` - Create directory
- `rmdir <path>` - Remove directory
- `cd <path>` - Change directory
- `pwd` - Show current directory

### History & Undo
- `undo <file>` - Undo last change to file
- `redo <file>` - Redo last undo
- `history <file>` - Show file change history
- `restore <file> <timestamp>` - Restore to specific version

### Safe Command Execution
- `run <command>` - Execute whitelisted command
- `test <framework>` - Run tests (pytest, jest, etc.)
- `lint <file>` - Run linter
- `format <file>` - Format code

### Configuration
- `model <name>` - Switch AI model
- `config <key> <value>` - Set configuration
- `config-show` - Show current configuration

### Session Management
- `save-session <name>` - Save current session
- `load-session <name>` - Load saved session
- `list-sessions` - List all sessions

## Architecture

```
ai_coder/
├── cli.py              # Main REPL interface
├── commands/           # Command handlers
├── core/              # Core functionality
├── ai/                # AI integration
├── project/           # Project management
├── history/           # History & versioning
├── safety/            # Safe command execution
└── utils/             # Utilities
```

## License

MIT License
