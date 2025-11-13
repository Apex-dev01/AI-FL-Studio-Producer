import logging
from config import *

def setup_logging():
    """Setup logging configuration"""
    logging.basicConfig(
        level=LOG_LEVEL,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(LOG_FILE),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger(__name__)

def get_screen_coordinates():
    """Get current mouse coordinates"""
    from pynput.mouse import Controller
    mouse = Controller()
    return mouse.position

def parse_region(region_string):
    """Parse region string to coordinates"""
    # Format: "x1,y1,x2,y2"
    try:
        coords = tuple(map(int, region_string.split(',')))
        return coords
    except:
        return None

def validate_ollama_connection():
    """Check if Ollama is running"""
    import requests
    try:
        response = requests.get(f"{OLLAMA_API_URL}/api/tags", timeout=5)
        return response.status_code == 200
    except:
        return False
