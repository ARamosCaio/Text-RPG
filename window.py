from tkinter import *
from tkinter import ttk
import tkinter as tk

root = tk.Tk()
root.geometry("800x800")
root.title("Main")


text = tk.Entry(root, width=77, background="black")
text.pack()

def first_action():
    text.delete(0,"end")
    text.insert(0, "You Opened de door")

set_btn = tk.Button(root, text="Open the door", command=first_action, height=3, width=10)
set_btn.pack()
    
root.mainloop()