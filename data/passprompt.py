import tkinter as tk
import tkinter.simpledialog

answer = tk.simpledialog.askstring("Enter sudo password", 'Password:', show="*")
print(answer)