from tkinter import *
import tkinter as tk
import tkinter.font as font

root = tk.Tk()
root.geometry("800x800")
root.title("Main")


text = tk.Entry(root, width=90)
text.pack()

def first_action():
    text.delete(0,"end")
    text.insert(0, "You Opened de door")

def second_action():
    text.delete(0,"end")
    text.insert(0, "You Enter the room")

set_btn = tk.Button(root, text="Open the door", command=first_action, height=3, width=10)
set_btn.pack()

set_btn2 = tk.Button(root, text="Enter the room", command=second_action, height=3, width=10)
set_btn2.pack()
root.mainloop()