# AI Coder Development Guide

## Quick Start

1. **Clone and Setup**
   ```bash
   cd ai-coder
   ./start.sh
   ```

2. **Manual Setup**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   python main.py
   ```

## Project Structure

```
ai-coder/
├── main.py                 # Entry point
├── start.sh               # Startup script
├── requirements.txt       # Dependencies
├── setup.py              # Package setup
├── README.md              # Main documentation
├── config/
│   └── default.yaml       # Default configuration
├── ai_coder/              # Main package
│   ├── __init__.py
│   ├── cli.py             # Main CLI interface
│   ├── core/              # Core functionality
│   │   ├── __init__.py
│   │   └── config.py      # Configuration management
│   ├── utils/             # Utilities
│   │   ├── __init__.py
│   │   └── logger.py      # Logging utilities
│   ├── ai/                # AI integration
│   │   ├── __init__.py
│   │   └── ollama_client.py # Ollama API client
│   ├── operations/        # File & project operations
│   │   ├── __init__.py
│   │   ├── file_manager.py    # File operations with history
│   │   └── project_manager.py # Project-level operations
│   └── safety/            # Safe command execution
│       ├── __init__.py
│       └── safe_executor.py  # Secure command runner
└── tests/                 # Test suite
    └── test_basic.py
```

## Key Features Implemented

### 🤖 AI-Powered Code Generation
- **Ollama Integration**: Full API client with streaming support
- **Smart Prompts**: Context-aware prompt building for different tasks
- **Model Management**: Switch between models, test connections
- **Error Handling**: Robust error handling and retries

### 📁 Advanced File Management
- **History Tracking**: Every file change automatically backed up
- **Undo/Redo**: Full undo/redo functionality per file
- **Versioning**: Timestamp-based version management
- **Metadata**: JSON-based metadata storage for file history

### 🏗️ Project-Level Intelligence  
- **Project Templates**: Built-in templates for Python, JavaScript, React
- **AI Project Generation**: Use AI to create complete project structures
- **Project Analysis**: Automatic project type detection and analysis
- **Cross-File Refactoring**: AI-powered multi-file refactoring

### 🛡️ Safe Command Execution
- **Whitelisting**: Only allow predefined safe commands
- **Sandboxing**: Controlled environment for command execution
- **Path Protection**: Block access to sensitive system directories
- **Special Commands**: Built-in handlers for test, lint, format, build

### 🎨 Rich CLI Interface
- **Syntax Highlighting**: Beautiful code display with Rich
- **Auto-completion**: Smart command completion
- **History**: Persistent command history
- **Interactive Prompts**: User-friendly prompt interface

### ⚙️ Configuration Management
- **YAML Config**: Flexible YAML-based configuration
- **Environment Support**: Multiple environment configurations
- **Runtime Updates**: Change settings during runtime
- **Validation**: Configuration validation and error handling

## Usage Examples

### File Operations
```bash
# Create new file with AI
create app.py python "Flask web server with REST API"

# Edit existing file
edit app.py python "add error handling and logging"

# Refactor code
refactor app.py python "convert to classes and add type hints"

# Show file with syntax highlighting
show app.py
```

### Project Operations
```bash
# Create new project
create-project python myapi "REST API with authentication"

# Analyze current project
analyze-project

# Cross-file refactoring
refactor-project "add async/await throughout the codebase"
```

### Safe Commands
```bash
# Run tests
test pytest

# Lint code
lint app.py

# Format code
format app.py

# Build project
build

# Install package
install requests
```

### History Management
```bash
# Undo last change
undo app.py

# Redo last undo
redo app.py

# Show file history
history app.py

# Restore to specific version
restore app.py 20240905_143022
```

## Development Tasks

### Completed ✅
- [x] Core configuration system
- [x] Logging and action tracking
- [x] Ollama AI client with streaming
- [x] File manager with history/versioning
- [x] Project manager with templates
- [x] Safe command executor
- [x] Main CLI interface with Rich
- [x] Basic project structure
- [x] Documentation and setup scripts

### Pending 🚧
- [ ] Complete CLI command implementations
- [ ] Enhanced project templates
- [ ] Plugin system for extensions
- [ ] Web interface option
- [ ] Docker containerization
- [ ] Integration tests
- [ ] Performance optimizations
- [ ] Session management
- [ ] Configuration GUI

## Testing

```bash
# Run tests
python -m pytest tests/

# Run specific test
python -m pytest tests/test_basic.py

# Run with coverage
pip install pytest-cov
python -m pytest --cov=ai_coder tests/
```

## Configuration

The configuration is stored in YAML format. Default locations:
- `~/.config/ai-coder/config.yaml` (user config)
- `config/default.yaml` (default config)

Key configuration sections:
- `ai`: AI model settings (URL, model, timeout, etc.)
- `workspace`: Workspace settings (history, auto-save, etc.)
- `safety`: Security settings (allowed commands, blocked paths)
- `ui`: User interface settings (theme, syntax highlighting)
- `project`: Project management settings (templates, licenses)

## Architecture Notes

### Modular Design
Each component is self-contained with clear interfaces:
- **Core**: Configuration and fundamental utilities
- **AI**: All AI-related functionality isolated
- **Operations**: File and project operations
- **Safety**: Security and command execution
- **CLI**: User interface and command handling

### Error Handling
- Comprehensive error handling at every level
- Graceful degradation when AI is unavailable
- User-friendly error messages
- Detailed logging for debugging

### Extensibility
- Plugin-ready architecture
- Configuration-driven behavior
- Modular command system
- Clean separation of concerns

## Contributing

1. Follow the existing code structure
2. Add tests for new functionality
3. Update documentation
4. Use type hints where possible
5. Follow PEP 8 style guidelines

## Troubleshooting

### Common Issues

1. **Ollama Connection Failed**
   - Ensure Ollama is running: `ollama serve`
   - Check the API URL in config
   - Verify the model is installed: `ollama list`

2. **Import Errors**
   - Activate virtual environment: `source venv/bin/activate`
   - Install dependencies: `pip install -r requirements.txt`

3. **Permission Errors**
   - Check file permissions
   - Ensure write access to workspace directory
   - Verify history directory can be created

4. **Command Not Found**
   - Check safety configuration
   - Verify command is in whitelist
   - Use absolute paths if needed
