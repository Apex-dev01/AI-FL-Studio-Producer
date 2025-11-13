# AI FL Studio Producer

An intelligent AI-powered music production assistant that automates FL Studio workflows using vision AI, pynput automation, and a Tkinter GUI.

## Features

- **Vision-Capable AI**: Uses MiniCPM-V 2.6B for OCR, image analysis, and visual understanding
- **FL Studio Automation**: Automate click patterns, track labeling, plugin configuration via pynput
- **Tkinter GUI**: User-friendly interface for task selection and monitoring
- **Local Processing**: Everything runs locally using Ollama—no cloud dependencies
- **Lightweight**: Optimized for integrated graphics (Intel HD 630) and modest hardware

## System Requirements

- **CPU**: Intel i5-7500 or equivalent (4+ cores)
- **GPU**: Intel HD Graphics 630 or equivalent integrated GPU
- **RAM**: 8GB minimum (3.9GB shared GPU memory)
- **OS**: Windows 10/11
- **Python**: 3.10+
- **FL Studio**: 20.9+ (for automation)

## Installation

### Step 1: Install Ollama

Download and install Ollama from [ollama.com](https://ollama.com/)

### Step 2: Pull the MiniCPM-V 2.6B Model

Open terminal/command prompt and run:

```bash
ollama pull minicpm-v
```

### Step 3: Clone This Repository

```bash
git clone https://github.com/Apex-dev01/AI-FL-Studio-Producer.git
cd AI-FL-Studio-Producer
```

### Step 4: Install Python Dependencies

```bash
pip install -r requirements.txt
```

Required packages:
- `ollama` - LLM API interface
- `pynput` - Keyboard/mouse automation
- `pillow` - Image processing
- `pyimage` - Screenshot capture
- `requests` - HTTP requests

### Step 5: Verify Ollama is Running

Make sure Ollama is running on `localhost:11434`. Test with:

```bash
curl http://localhost:11434/api/tags
```

## Quick Start

### 1. Start the Application

```bash
python main.py
```

The Tkinter GUI will launch.

### 2. Select a Task

In the GUI, choose from:
- **OCR**: Extract text from selected screen region
- **Name Tracks**: Auto-name FL Studio tracks using AI
- **Organize Stems**: Sort and label audio stems
- **Plugin Analysis**: Identify and configure plugins
- **Custom Command**: Enter custom voice/text commands

### 3: Monitor Output

Watch the status window for AI analysis and automation progress.

## Architecture

### `main.py`
Entry point. Initializes Tkinter GUI and orchestrates workflows.

### `gui.py`
Tkinter interface for task selection, real-time status updates, and log display.

### `ollama_processor.py`
Handles Ollama API calls, vision processing, and OCR tasks.

### `automation.py`
pynput-based automation for FL Studio interactions:
- Mouse movement and clicking
- Keyboard input for naming/configuration
- Timing and macro execution

### `utils.py`
Utility functions for screenshots, image processing, and logging.

## Configuration

### Edit `config.py` for customization:

```python
# Ollama Settings
OLLAMA_API_URL = "http://localhost:11434"
OLLAMA_MODEL = "minicpm-v"
OLLAMA_TIMEOUT = 120  # seconds

# FL Studio Settings
FL_STUDIO_WINDOW_TITLE = "FL Studio"
FL_STUDIO_AUTOMATION_DELAY = 0.1  # seconds between actions

# GUI Settings
GUI_THEME = "dark"
GUI_WIDTH = 1000
GUI_HEIGHT = 700

# OCR Settings
OCR_CONFIDENCE_THRESHOLD = 0.7
```

## Usage Examples

### Example 1: Extract Text from Screen

```python
from ollama_processor import OllamaProcessor

processor = OllamaProcessor()
result = processor.ocr_screenshot(region=(100, 100, 400, 400))
print(result['text'])
```

### Example 2: Automate FL Studio Track Naming

```python
from automation import FLStudioAutomation

auto = FLStudioAutomation()
auto.click_track_name_field()
auto.type_text("Drums")
auto.press_enter()
```

### Example 3: Full Workflow - Analyze and Name Tracks

```python
from main import AIProducer

producer = AIProducer()
producer.analyze_and_name_tracks()
```

## Troubleshooting

### Issue: "Ollama connection refused"

**Solution**: Ensure Ollama is running:

```bash
ollama serve
```

### Issue: "Model not found: minicpm-v"

**Solution**: Pull the model:

```bash
ollama pull minicpm-v
```

### Issue: GUI freezes during processing

**Solution**: Processing happens on a separate thread. Check console for errors. Increase `OLLAMA_TIMEOUT` in config.py if needed.

### Issue: pynput clicks not working in FL Studio

**Solution**: 
1. Ensure FL Studio window is focused
2. Grant necessary permissions to Python (check Windows Defender)
3. Try increasing `FL_STUDIO_AUTOMATION_DELAY`

## Project Structure

```
AI-FL-Studio-Producer/
├── main.py                 # Entry point
├── gui.py                  # Tkinter GUI
├── ollama_processor.py     # Vision AI integration
├── automation.py           # FL Studio automation
├── utils.py                # Utilities
├── config.py               # Configuration
├── requirements.txt        # Dependencies
└── README.md               # This file
```

## Performance Tips

1. **Optimize Image Size**: Smaller screenshots = faster OCR
   ```python
   result = processor.ocr_screenshot(region=(0, 0, 400, 300))  # Faster
   ```

2. **Batch Operations**: Group automation tasks to reduce delays

3. **Cache Results**: Store OCR results to avoid re-processing

4. **Monitor Ollama Memory**: Check GPU memory usage
   ```bash
   tasklist | findstr ollama
   ```

## Advanced Usage

### Running Ollama on GPU (if you upgrade hardware)

```bash
ollama run minicpm-v --gpu 1
```

### Custom Model Switching

```python
from ollama_processor import OllamaProcessor

# Use a different lightweight model
processor = OllamaProcessor(model="llama3-vision")
```

### Headless Mode (No GUI)

```bash
python main.py --headless --task ocr --region "100,100,400,400"
```

## License

MIT License. See LICENSE file for details.

## Contributing

Contributions welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Submit a pull request

## Support

For issues, questions, or feature requests, open an issue on GitHub.

## Credits

- **Ollama**: Local LLM framework
- **MiniCPM-V**: Lightweight vision model
- **pynput**: Cross-platform input automation
- **Tkinter**: Python GUI framework
