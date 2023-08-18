from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK="✔"
reps=0
t=None
mark=""

# ---------------------------- TIMER RESET ------------------------------- # 
def res():
    global t
    global reps
    global mark
    reps=0
    mark=""
    window.after_cancel(t)
    timer.config(text="Timer")
    canvas.itemconfig(timertext, text="00:00")
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def starttimer():
    global reps
    global mark
    reps+=1
    wsec=WORK_MIN*60
    ssec=SHORT_BREAK_MIN*60
    lsec=LONG_BREAK_MIN*60

    if reps%2!=0:
        countdown(wsec)
        timer.config(text="Work", fg=GREEN)
    elif reps == 8:
        countdown(lsec)
        timer.config(text="Long Break", fg=RED)
    elif reps%2==0:
        countdown(ssec)
        timer.config(text="Short Break", fg=PINK)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    global t
    global mark
    min=math.floor(count/60)
    sec=count%60
    if sec<10:
        sec=f"0{sec}"
    canvas.itemconfig(timertext, text=f"{min}:{sec}")
    if count>0:
        t=window.after(1000, countdown, count-1)
    else:
        for _ in range(math.floor(reps/2)):
            mark+=CHECK
        check.config(text=mark)
        starttimer()
# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)


canvas=Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato=PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
timertext=canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

timer=Label(text="Timer", fg=GREEN, bg=YELLOW)
timer.config(font=(FONT_NAME, 38, "bold"))
timer.grid(row=0, column=1)


start=Button(text="Start", command=starttimer)
start.grid(row=2, column=0)

stop=Button(text="Reset", command=res)
stop.grid(row=2, column=2)

check=Label(fg=GREEN, bg=YELLOW)
check.grid(row=3, column=1)

window.mainloop()