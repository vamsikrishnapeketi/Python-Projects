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
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_title.config(text = "TIMER")
    check_mark.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    work_time_insec = WORK_MIN * 60
    short_break_insec = SHORT_BREAK_MIN * 60
    long_break_insec = LONG_BREAK_MIN * 60
    global reps 
    reps += 1
    if reps % 8 == 0:
        timer_title.config(Text = "Long Break", fg = RED)
        count_down(long_break_insec)
    elif reps % 2 == 0:
        timer_title.config(text = "Short Break",fg = PINK )
        count_down(short_break_insec)
    else:
        timer_title.config(text = "Work",fg = GREEN )
        count_down(work_time_insec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = "00"
    elif count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min == 0:
        count_min = "00"        
    canvas.itemconfig(timer_text, text= f"{count_min}:{count_sec}")
    if count> 0:
        global timer
        timer = window.after(1000,count_down,count-1)#this windows.after waits for 1s and keeps calling the count_down function and the arg for count_down is count -1
    else:
        start_timer()
        mark = ""
        for _ in range(math.floor(reps/2)):
            mark += "✔"
        check_mark.config(text = mark)    
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image= tomato_img)
timer_text = canvas.create_text(100,130, text="00:00",fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1,row=1)

timer_title = Label(text="TIMER", fg=GREEN, font=(FONT_NAME, 35, "bold"))
timer_title.grid(column=1,row=0)

button_1 = Button(text="Start",highlightthickness=0,command=start_timer).grid(column=0, row=2)

button_2 = Button(text="Reset",highlightthickness=0,command=reset_timer).grid(column=2, row=2)

check_mark = Label(text="", fg=GREEN, bg=YELLOW)
check_mark.grid(column=1, row=3)



window.mainloop()