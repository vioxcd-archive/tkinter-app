import time
import tkinter as tk
from tkinter import *

def tick(time1=''):
    #Get the current local time from the PC
    time2 = time.strftime('%I:%M:%S')
    #if the time string has changes, update it
    if time2 != time1:
        time1 = time2
        clock_frame.config(text=time2)
    #Calls itself every 200ms to update
    clock_frame.after(200, tick)

root = tk.Tk()
root.title('Digital Clock')
clock_frame = tk.Label(root, font=('times', 100, 'bold'),
                       bg='black', fg='green')
clock_frame.pack(fill='both', expand=1)
root.geometry('700x500')
tick()
root.mainloop()
