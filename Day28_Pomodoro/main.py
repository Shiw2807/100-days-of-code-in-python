from cProfile import label
from cgitb import text
from email.mime import image
import imp
import re
from sqlite3 import Row
from tkinter import *
import math



INITIAL_REPS = 4
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
# colors for easier access
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
reps=0
timer=None



def reset_time():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title.config(text="Timer")
    check_mark.config(text="")
    global reps
    reps=0

def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60

    if reps % 8 == 0:
        count_down(long_break_sec)
        title.config(text="Break", fg=RED)
    elif reps % 2 == 0: 
        count_down(short_break_sec)
        title.config(text="Break",fg=PINK)
    else: 
        count_down(work_sec)
        title.config(text="Work", fg=GREEN)
    
    
def count_down(count):
    count_minute=math.floor(count/60)
    count_sec=count % 60
    if count_sec < 10:
        count_sec=f"0{count_sec}"

    canvas.itemconfigure(timer_text, text=f"{count_minute}:{count_sec}")
    if count>0:
        global timer
        timer= window.after(1000, count_down, count-1)
    else:
        start_timer()
        marks=""
        work_sessions=math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        check_mark.config(text="marks")



window=Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title= Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title.grid(column=1, row=0)

check_mark= Label(text="✔", fg=GREEN, bg=YELLOW )
check_mark.grid(column=1, row=3)

canvas=Canvas(width=200,height=224, bg=YELLOW, highlightthickness=0)
tomoto_img=PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomoto_img)

start=Button(text="Start", highlightthickness=0, command=start_timer)
start.grid(column=0, row=2)
reset=Button(text="Reset", highlightthickness=0, command=reset_time)
reset.grid(column=2, row=2)

timer_text= canvas.create_text(102,130,text="00:00", fill="white", font=(FONT_NAME,35,"bold"))
canvas.grid(column=1, row=1)

window.mainloop()