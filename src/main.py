# main.py
import tkinter as tk
from ui import ResourceAllocationGraphUI

if __name__ == "__main__":
    root = tk.Tk()
    app = ResourceAllocationGraphUI(root)
    root.mainloop()