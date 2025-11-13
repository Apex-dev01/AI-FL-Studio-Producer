"""
Configuration file for AI FL Studio Producer
Edit these settings to customize behavior
"""

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
GUI_FONT_SIZE = 10

# OCR Settings
OCR_CONFIDENCE_THRESHOLD = 0.7
OCR_LANGUAGE = "eng"

# Logging
LOG_LEVEL = "INFO"
LOG_FILE = "ai_producer.log"

# Feature Flags
ENABLE_VOICE_INPUT = True
ENABLE_AUTO_SAVE = True
