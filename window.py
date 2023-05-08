from tkinter import *

root = Tk()

class App():
    def __init__(self):
        self.root = root
        self.screen_config()
        root.mainloop()
    
    def screen_config(self):
        self.root.title("ROOMS")
        self.root.geometry("1000x900")
        self.root.configure(background="#121212")
        self.root.resizable(False, False)

App()
