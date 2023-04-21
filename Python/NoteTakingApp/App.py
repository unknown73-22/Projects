
import tkinter as tk
from tkinter import filedialog
import os
import datetime
import Setup_Calender as Setup_calender


class Main:
    
    calender = Setup_calender.Setup_Calender()

    root = tk.Tk()
    root.title("the WALL")

    screen_width = 1200#2000
    screen_height = 800#1500

    root.geometry(f"{screen_width}x{screen_height}")

    calender.setup_calender(root)

    root.mainloop()