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
check_mark = "✔"
check_marks = ""


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    canvas.itemconfig(timer_text, text="25:00")
    window.after_cancel(timer)
    pomo_label.config(text="Timer", fg=GREEN, bg=YELLOW)
    check_marks = ""
    check_mark_label.config(text="", fg=GREEN, bg=YELLOW)
    canvas.itemconfig(timer_text, text="25:00")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    global check_marks
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # If it's the 1st/3rd/5th/7th rep
    if reps % 8 == 0:
        reps = 0
        pomo_label.config(text="Long Break Time!", fg=RED, bg=YELLOW)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        # 2nd/4th/6th rep
        pomo_label.config(text="Take A Short Break!", fg=PINK, bg=YELLOW)
        count_down(short_break_sec)
        check_marks += check_mark
        check_mark_label.config(text=check_marks, fg=GREEN, bg=YELLOW)

    else:
        pomo_label.config(text="GET TO WORK SLACKER!", fg=GREEN, bg=YELLOW)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    minutes = math.floor(count / 60)
    seconds = count % 60
    canvas.itemconfig(timer_text, text=f"{minutes:02}:{seconds:02}")
    if count > 0:
        global timer

        timer = window.after(1000, count_down, count - 1)
    elif count == 0:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro App")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=220, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(101, 112, image=tomato_img)
timer_text = canvas.create_text(115, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Create Labels
pomo_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bo

                                                            check_mark_label = Label(text=check_marks, fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
check_mark_label.grid(column=1, row=3)

# Create two buttons
start_button = Button(text="Start", font=(FONT_NAME, 16, "bold"), command=start_timer, highlightthickness=0, bg=YELLOW)
start_button.grid(column=0, row=2)
reset_button = Button(text="Reset", font=(FONT_NAME, 16, "bold"), command=reset_timer, highlightthickness=0, bg=YELLOW)
reset_button.grid(column=2, row=2)
ld
"))
pomo_label.grid(column=1, row=0)

window.mainloop()
