import tkinter as tk

class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.button = tk.Button(self.root, text="Click me")
        self.button.bind("<Button-1>", self.on_button_click)
        self.button.pack()

    def on_button_click(self, event):
        print("Button clicked")

    def run(self):
        self.root.mainloop()

def start_memory_leak_8():
    gui = GUI()
    gui.run()
    print("Example code with a memory leak running...")
