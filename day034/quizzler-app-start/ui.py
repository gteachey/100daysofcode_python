from tkinter import *
from tkinter import messagebox

from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20)
        self.score_keeper = self.score_label = Label(text=f"Score: {self.quiz.score}", bg=THEME_COLOR, fg="white")
        self.score_keeper.grid(column=1, row=0, pady=20)
        self.canvas = Canvas()
        self.canvas.config(bg="white", height=250, width=300)
        self.question_text = self.canvas.create_text(150, 125, text="Something",
                                                     font=("Arial", 20, "italic"), width=280)
        self.canvas.grid(columnspan=2, column=0, row=1)
        true_image = PhotoImage(file="images/true.png")
        false_image = PhotoImage(file="images/false.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.guess_false)
        self.true_button.grid(column=0, row=2, pady=20)
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.guess_true)
        self.false_button.grid(column=1, row=2, pady=20)
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.config(bg="white")
        self.canvas.itemconfigure(self.question_text, text=q_text)

    def guess_false(self):
        if self.quiz.check_answer("False"):
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.update_score)

    def guess_true(self):
        if self.quiz.check_answer("True"):
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.update_score)

    def update_score(self):
        self.score_keeper.config(self.score_keeper, text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            self.get_next_question()
        else:
            messagebox.showinfo(title="Quiz Completed", message=f"Your final score was: {self.quiz.score}")
            quit(0)
