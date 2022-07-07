from this import s
import tkinter
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz_brain = quiz_brain
        self.window = tkinter.Tk()
        self.window.title("Quizzler")
        self.window.minsize(width=300, height=300)
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = tkinter.Label(
            text="Score: 0", bg=THEME_COLOR, fg="White")
        self.score_label.grid(column=1, row=0)

        self.canvas = tkinter.Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(
            150, 125, text="Question go over here!!!!!!!!!!!!!!!", fill=THEME_COLOR, width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        true_img = tkinter.PhotoImage(file="images/true.png")
        self.true_button = tkinter.Button(
            image=true_img, highlightthickness=0, command=self.answer_true)
        self.true_button.grid(column=0, row=2)

        false_img = tkinter.PhotoImage(file="images/false.png")
        self.false_button = tkinter.Button(
            image=false_img, highlightthickness=0, command=self.answer_false)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="White")
        self.score_label.config(text=f"Score: {self.quiz_brain.score}")
        if self.quiz_brain.still_has_questions():
            q_text = self.quiz_brain.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(
                self.question_text, text=f"You've completed the quiz.\nYour final score was: {self.quiz_brain.score}/{self.quiz_brain.question_number}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def answer_true(self):
        is_right = self.quiz_brain.check_answer('True')
        self.give_feedback(is_right)

    def answer_false(self):
        is_right = self.quiz_brain.check_answer('False')
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="Green")
        else:
            self.canvas.config(bg="Red")
        self.window.after(1000, self.get_next_question)
