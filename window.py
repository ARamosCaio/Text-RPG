from tkinter import *
from tkinter import ttk
import tkinter as tk

root = Tk()
root.geometry("800x800")
root.title("Main")
screen = Entry(root, text="Testing...", width=78,  justify='right', font=10, bd=1)
screen.grid(row=0, columnspan=1, padx=5, pady=30, ipady=30)

text = tk.Entry(root)
text.pack()

def first_action():
    text.delete(0,"end")
    text.insert(0, "You Opened de door")

tk.Button(root, text="Open the door", command=first_action)
    
root.mainloop()