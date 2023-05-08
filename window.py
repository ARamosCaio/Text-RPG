from tkinter import *

root = Tk()

class App():
    def __init__(self):
        self.root = root
        self.screen_config()
        self.screen_frames()
        root.mainloop()
    
    def screen_config(self):
        self.root.title("ROOMS")
        self.root.geometry("1000x900")
        self.root.configure(background="#dbdbdb")
        self.root.resizable(False, False)
    
    def screen_frames(self):
        self.text_frame = Frame(self.root, bd=2, bg="#121212", highlightbackground="#5c5c5c", highlightthickness=4)
        self.text_frame.place(relx=0.005, rely=0.005, relwidth=0.99, relheight=0.70)

        self.stats_frame = Frame(self.root, bd=2, bg="#121212", highlightbackground="#5c5c5c", highlightthickness=4)
        self.stats_frame.place(relx=0.005, rely=0.710, relwidth=0.4, relheight=0.28)

App()
