# runs under python2 not python3

import time
import tkinter as tk


def tick(time1=''):
    time2 = time.strftime('%H:%M:%S')
    if time2 != time1:
        time1 = time2
        CLOCK.config(text=time2)
    CLOCK.after(200, tick)


ROOT = tk.Tk()
ROOT.title("clock")
CLOCK = tk.Label(ROOT, font=('arial', 60, 'bold'), bg='green')
CLOCK.pack(fill='both', expand=1)
tick()
ROOT.mainloop()
