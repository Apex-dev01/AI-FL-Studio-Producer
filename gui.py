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
