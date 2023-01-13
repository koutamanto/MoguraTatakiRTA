from math import floor
import random, time
from threading import Thread
from tkinter import *
from tkinter import ttk
from datetime import datetime

clicks = 0
history = ""

def respawn():
    global btn, photo, clock_time, clock, clicks, history
    # if clock_time % 10 == 0:
    #     clicks = 0
    #     history = history + "\n" + str(clicks) + "回" 
    #     clock["text"] = str(clock_time) + "秒経過\n" + str(clicks) + "回" + history
        
    clicks+=1
    clicks
    clock["text"] = str(clock_time) + "秒経過\n" + str(clicks) + "回"

    btn.destroy()
    # photo = PhotoImage(file="mogura.png")
    # photo.subsample(10)
    # photo.subsample(300, 300)

    btn = ttk.Button(frm, command=respawn, image=photo, width=0)
    btn.place(x=random.randint(100, 500), y=random.randint(100, 400))
root = Tk()

frm = ttk.Frame(root, padding=10, width=1600, height=900)
frm.grid()
photo = PhotoImage(file="mogura.png")
# photo.subsample(10, 10)
photo = photo.subsample(5)
btn = ttk.Button(frm, command=respawn, image=photo, width=0)
btn.place(x=random.randint(100, 500), y=random.randint(100, 400))
start_time = datetime.now()

def clock_loop():
    global clicks, clock_time, clock, history
    clock_time = 0
    clock = ttk.Label(frm, text=str(clock_time) + "秒経過", foreground="Black", compound="top", font=("Arial", 20))
    clock.place(x=root.winfo_width()/2)
    score_history = ttk.Label(frm, text=history, foreground="Black", compound="top", font=("Arial", 20))
    score_history.place(x=floor(root.winfo_width()*(5/6)))
    while True:
        time.sleep(1)
        clock_time+=1
        clock["text"] = str(clock_time) + "秒経過\n" + str(clicks) + "回"
        clock.place(x=root.winfo_width()/2)
        score_history.place(x=floor(root.winfo_width()*(5/6)))
        if clock_time % 10 == 0:
            history = str(clicks) + "回"  + "\n" + history
            score_history["text"] = history
            clicks = 0
            clock["text"] = str(clock_time) + "秒経過\n" + str(clicks) + "回"
Thread(target=clock_loop).start()
root.mainloop()