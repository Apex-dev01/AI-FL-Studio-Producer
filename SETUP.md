# Complete Setup Guide for AI FL Studio Producer

This document contains the complete code templates for creating the remaining Python modules.

## Files to Create

1. **gui.py** - Tkinter GUI interface
2. **ollama_processor.py** - Ollama AI integration
3. **automation.py** - FL Studio automation with pynput
4. **utils.py** - Utility functions

---

## gui.py

Create this file to handle the Tkinter GUI:

```python
import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
from config import *
import threading

class AIProducerGUI:
    def __init__(self, root):
        self.root = root
        self.setup_ui()
    
    def setup_ui(self):
        """Setup Tkinter UI elements"""
        # Menu bar
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Exit", command=self.root.quit)
        
        # Main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Title label
        title_label = ttk.Label(main_frame, text="AI FL Studio Producer", font=("Arial", 14, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=10)
        
        # Task selection
        ttk.Label(main_frame, text="Select Task:").grid(row=1, column=0, sticky=tk.W)
        self.task_var = tk.StringVar()
        tasks = ["OCR", "Name Tracks", "Organize Stems", "Plugin Analysis", "Custom Command"]
        task_menu = ttk.Combobox(main_frame, textvariable=self.task_var, values=tasks, state="readonly")
        task_menu.grid(row=1, column=1, sticky=(tk.W, tk.E), pady=5)
        
        # Execute button
        execute_btn = ttk.Button(main_frame, text="Execute", command=self.execute_task)
        execute_btn.grid(row=2, column=0, columnspan=2, pady=10)
        
        # Output log
        ttk.Label(main_frame, text="Log Output:").grid(row=3, column=0, columnspan=2, sticky=tk.W)
        self.log_text = scrolledtext.ScrolledText(main_frame, height=15, width=60)
        self.log_text.grid(row=4, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), pady=5)
    
    def execute_task(self):
        """Execute selected task in a separate thread"""
        task = self.task_var.get()
        if not task:
            messagebox.showwarning("Warning", "Please select a task")
            return
        
        self.log(f"[INFO] Executing task: {task}")
        thread = threading.Thread(target=self.run_task, args=(task,))
        thread.start()
    
    def run_task(self, task):
        """Run the task (implement task logic here)"""
        try:
            if task == "OCR":
                self.log("[INFO] OCR task started...")
                # Implementation here
            elif task == "Name Tracks":
                self.log("[INFO] Track naming task started...")
                # Implementation here
            self.log("[INFO] Task completed successfully")
        except Exception as e:
            self.log(f"[ERROR] Task failed: {str(e)}")
    
    def log(self, message):
        """Add message to log output"""
        self.log_text.insert(tk.END, message + "\n")
        self.log_text.see(tk.END)
        self.root.update()
```

---

## ollama_processor.py

Create this file for Ollama AI integration:

```python
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
```

---

## automation.py

Create this file for FL Studio automation:

```python
from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Controller as KeyboardController
from config import *
import time

class FLStudioAutomation:
    def __init__(self):
        self.mouse = MouseController()
        self.keyboard = KeyboardController()
        self.delay = FL_STUDIO_AUTOMATION_DELAY
    
    def click(self, x, y, button=Button.left, count=1):
        """Click at coordinates"""
        self.mouse.position = (x, y)
        time.sleep(self.delay)
        self.mouse.click(button, count)
        time.sleep(self.delay)
    
    def type_text(self, text):
        """Type text"""
        self.keyboard.type(text)
        time.sleep(self.delay)
    
    def press_key(self, key):
        """Press a single key"""
        self.keyboard.press(key)
        time.sleep(self.delay / 2)
        self.keyboard.release(key)
        time.sleep(self.delay)
    
    def hotkey(self, *keys):
        """Press hotkey combination"""
        for key in keys:
            self.keyboard.press(key)
        time.sleep(self.delay)
        for key in reversed(keys):
            self.keyboard.release(key)
        time.sleep(self.delay)
    
    def click_track_name_field(self, x=100, y=50):
        """Click on track name field"""
        self.click(x, y)
    
    def name_track(self, name):
        """Name a track"""
        self.type_text(name)
        self.press_key('Return')
```

---

## utils.py

Create this file for utility functions:

```python
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
```

---

## Next Steps

1. Copy each code block above into its corresponding Python file
2. Save all files in the project root directory
3. Run the application: `python main.py`
4. Ensure Ollama is running: `ollama serve`
5. Model is pulled: `ollama pull minicpm-v`

## Notes

- Modify coordinates in automation.py to match your FL Studio layout
- Adjust timeouts in config.py if needed
- Add more task implementations in gui.py as needed
