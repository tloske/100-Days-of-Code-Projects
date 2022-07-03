import tkinter
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
    checkmarks.config(text="")
    title_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    match reps:
        case reps if reps == 7:
            count_down(LONG_BREAK_MIN*60)
            title_label.config(text="Long Break", fg=RED)
        case reps if reps % 2:
            count_down(SHORT_BREAK_MIN*60)
            title_label.config(text="Short Break", fg=PINK)
        case reps if not reps % 2:
            count_down(WORK_MIN*60)
            title_label.config(text="Work", fg=GREEN)
    reps += 1


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    canvas.itemconfig(timer_text, text=f"{count//60:02d}:{count%60:02d}")
    if count > 0:
        global timer
        timer = window.after(10, count_down, count - 1)
    else:
        start_timer()
        checkmark_text = reps//2 * "✔"
        checkmarks.config(text=checkmark_text)

# ---------------------------- UI SETUP ------------------------------- #


window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


title_label = tkinter.Label(text="Timer", fg=GREEN,
                            bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)

canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas.grid(column=1, row=1)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white",
                                font=(FONT_NAME, 35, "bold"))


start_button = tkinter.Button(
    text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

checkmarks = tkinter.Label(fg=GREEN, bg=YELLOW)
checkmarks.grid(column=1, row=3)


reset_button = tkinter.Button(
    text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)


window.mainloop()
