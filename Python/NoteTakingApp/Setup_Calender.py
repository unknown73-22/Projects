import tkinter as tk
from tkcalender import Calender
import os
import datetime

class Setup_Calender:
    
    def setup_calender(root):
        
        current_date = datetime.date.today()
        current_year = datetime.date.today().year
        current_month = datetime.date.today().month
        current_day = datetime.date.today().day

        calender = Calender(root, selectmode = "day", year = current_year, month = current_month, day = current_day)
        calender.pack()