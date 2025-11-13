#!/usr/bin/env python3
"""
AI FL Studio Producer - Main Entry Point
AI-powered music production assistant with vision AI, automation, and GUI
"""

import sys
import tkinter as tk
from pathlib import Path
from gui import AIProducerGUI
from config import GUI_WIDTH, GUI_HEIGHT


class AIProducer:
    """Main application class for AI FL Studio Producer"""
    
    def __init__(self):
        """Initialize the AI Producer application"""
        self.root = tk.Tk()
        self.root.title("AI FL Studio Producer")
        self.root.geometry(f"{GUI_WIDTH}x{GUI_HEIGHT}")
        self.gui = AIProducerGUI(self.root)
    
    def run(self):
        """Start the application"""
        try:
            self.root.mainloop()
        except KeyboardInterrupt:
            print("\n[INFO] Application interrupted by user")
            self.shutdown()
        except Exception as e:
            print(f"[ERROR] Unexpected error: {e}")
            self.shutdown()
    
    def shutdown(self):
        """Gracefully shutdown the application"""
        print("[INFO] Shutting down...")
        self.root.quit()
        sys.exit(0)


if __name__ == "__main__":
    print("="*50)
    print("AI FL Studio Producer v1.0")
    print("Powered by Ollama + MiniCPM-V")
    print("="*50)
    
    app = AIProducer()
    app.run()
