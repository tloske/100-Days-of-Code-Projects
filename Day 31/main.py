import tkinter
from tkinter import messagebox
from random import choice
import pandas
BACKGROUND_COLOR = "#B1DDC6"
TIME = 3
WORDS_FILEPATH = "data/french_words.csv"


def get_next_word():
    if len(words) == 0:
        messagebox.showinfo(
            title="No words", message="No more words remaining.")
        window.destroy()
    global word
    word = choice(words)


def load_word_list():
    try:
        return pandas.read_csv("data/words_to_learn.csv").to_dict(orient='records')
    except FileNotFoundError:
        return pandas.read_csv("data/french_words.csv").to_dict(orient='records')


def start_timer():
    global timer
    timer = window.after(TIME*1000, flip_card)


def flip_card():
    canvas.itemconfig(language_text, text="English", fill="white")
    canvas.itemconfig(canvas_card, image=back_img)
    canvas.itemconfig(word_text, text=word["English"], fill="white")


def next_card():
    canvas.itemconfig(language_text, text="French", fill="black")
    canvas.itemconfig(canvas_card, image=front_img)
    canvas.itemconfig(word_text, text=word["French"], fill="black")


def correct():
    window.after_cancel(timer)
    words.remove(word)
    data = pandas.DataFrame(words, columns=["French", "English"])
    data.to_csv("data/words_to_learn.csv", index=False)
    wrong()


def wrong():
    get_next_word()
    next_card()
    start_timer()


if __name__ == "__main__":

    window = tkinter.Tk()
    window.title("Flash Cards")
    window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
    window.minsize(800, 600)

    # images
    front_img = tkinter.PhotoImage(file="images/card_front.png")
    back_img = tkinter.PhotoImage(file="images/card_back.png")
    wrong_img = tkinter.PhotoImage(file="images/wrong.png")
    right_img = tkinter.PhotoImage(file="images/right.png")

    words = load_word_list()
    get_next_word()

    canvas = tkinter.Canvas(width=800, height=526,
                            bg=BACKGROUND_COLOR, highlightthickness=0)
    canvas_card = canvas.create_image(400, 263, image=front_img)
    language_text = canvas.create_text(
        400, 150, text="French", font=("Ariel", 40))
    word_text = canvas.create_text(
        400, 263, text=word["French"], font=("Ariel", 60, "bold"))
    canvas.grid(column=0, row=0, columnspan=2, sticky="EW")

    wrong_button = tkinter.Button(
        image=wrong_img, highlightthickness=0, command=wrong)
    wrong_button.grid(column=0, row=1)

    right_button = tkinter.Button(
        image=right_img, highlightthickness=0, command=correct)
    right_button.grid(column=1, row=1)

    start_timer()

    window.mainloop()
