import tkinter as tk
from tkinter import ttk
from pip import main

def cheklibs(*libs):
    for lib in libs:
        try :
            __import__(lib)
        except ImportError:
            main(['install', lib])

cheklibs('pyautogui')
import pyautogui 


class WelcomePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(background="#2c3e50")

        label = ttk.Label(self, text="Welcome To UndrDsk", style="TLabel")
        label.pack(pady=20)

        # ایجاد فریمی برای قرار دادن دکمه‌ها در یک خط
        button_frame = tk.Frame(self, background="#2c3e50")
        button_frame.pack(fill=tk.X, padx=20, pady=10)

        # ایجاد دکمه با استفاده از سبک جدید و تنظیم متن به چپ
        left_button = ttk.Button(button_frame, text="Client", style="Custom.TButton", command=lambda: controller.show_frame("ClientPage1"))
        left_button.pack(side=tk.LEFT, expand=True)

        # ایجاد دکمه با استفاده از سبک جدید و تنظیم متن به راست
        right_button = ttk.Button(button_frame, text="Controller", style="Custom.TButton", command=lambda: controller.show_frame("ControllerPage1"))
        right_button.pack(side=tk.RIGHT, expand=True)

        # تنظیم ردیف و ستون
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

    def button_action(self):
        print("دکمه کلیک شد")

class ClientPage1(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(background="#2c3e50")
        back = ttk.Button(self, text="<", style="TLabel", command=lambda: controller.show_frame("WelcomePage"))
        back.pack(side=tk.LEFT, pady=20)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=2)

class ControllerPage1(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(background="#2c3e50")
        
        back = ttk.Button(self, text="<", style="TLabel", command=lambda: controller.show_frame("WelcomePage"))
        back.pack(side=tk.LEFT, pady=20)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=2)
class MainApplication(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.title("UndrDsk")
        self.geometry("800x600")

        # تنظیم استایل‌ها
        style = ttk.Style()
        style.configure("TFrame", background="#2c3e50")
        style.configure("TLabel", background="#2c3e50", foreground="#ecf0f1", font=("Helvetica", 16))
        style.configure("TButton", font=("Helvetica", 14))

        # استایل سفارشی برای دکمه‌ها
        style.configure("Custom.TButton", background="#3498db", foreground="#ecf0f1", font=("Helvetica", 14), padding=10)
        style.map("Custom.TButton", background=[("active", "#2980b9")], foreground=[("active", "#ffffff")])

        container = ttk.Frame(self)
        container.pack(fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (WelcomePage, ClientPage1, ControllerPage1):
            page_name = F.__name__
            frame = F(container, self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
        self.show_frame("WelcomePage")  # Use string representation of page_name

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
