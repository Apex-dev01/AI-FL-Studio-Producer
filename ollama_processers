import requests
import json
from PIL import ImageGrab
from config import *

class OllamaProcessor:
    def __init__(self, model=OLLAMA_MODEL):
        self.model = model
        self.api_url = OLLAMA_API_URL
        self.timeout = OLLAMA_TIMEOUT
    
    def ocr_screenshot(self, region=None):
        """Perform OCR on screenshot"""
        try:
            # Capture screenshot
            if region:
                screenshot = ImageGrab.grab(bbox=region)
            else:
                screenshot = ImageGrab.grab()
            
            # Save temporarily
            screenshot.save("/tmp/ocr_temp.png")
            
            # Send to Ollama
            with open("/tmp/ocr_temp.png", "rb") as f:
                image_data = f.read()
            
            payload = {
                "model": self.model,
                "prompt": "Extract all text from this image. Return only the text content.",
                "stream": False,
                "images": [image_data]
            }
            
            response = requests.post(
                f"{self.api_url}/api/generate",
                json=payload,
                timeout=self.timeout
            )
            
            if response.status_code == 200:
                result = response.json()
                return {"success": True, "text": result.get("response", "")}
            else:
                return {"success": False, "error": f"HTTP {response.status_code}"}
        
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    def analyze_image(self, prompt, region=None):
        """Analyze an image with custom prompt"""
        try:
            if region:
                screenshot = ImageGrab.grab(bbox=region)
            else:
                screenshot = ImageGrab.grab()
            
            screenshot.save("/tmp/analysis_temp.png")
            
            with open("/tmp/analysis_temp.png", "rb") as f:
                image_data = f.read()
            
            payload = {
                "model": self.model,
                "prompt": prompt,
                "stream": False,
                "images": [image_data]
            }
            
            response = requests.post(
                f"{self.api_url}/api/generate",
                json=payload,
                timeout=self.timeout
            )
            
            if response.status_code == 200:
                return response.json().get("response", "")
            else:
                return f"Error: HTTP {response.status_code}"
        
        except Exception as e:
            return f"Error: {str(e)}"
