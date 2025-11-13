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
