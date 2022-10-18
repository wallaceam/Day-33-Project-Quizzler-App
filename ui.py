from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(
            text=f"Score: {self.quiz.score}",
            fg="white", bg=THEME_COLOR,
            padx=20, pady=20)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(height=250, width=300, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(
            150,
            125,
            text="Test",
            font=FONT,
            fill=THEME_COLOR,
            width=280,
            justify="center"
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_button_img = PhotoImage(file="images/true.png")
        self.true_button = Button(
            image=true_button_img,
            pady=20, padx=20,
            borderwidth=0,
            command=self.true_pressed)
        self.true_button.grid(row=2, column=1)

        false_button_img = PhotoImage(file="images/false.png")
        self.false_button = Button(
            image=false_button_img,
            padx=20, pady=20,
            borderwidth=0,
            command=self.false_pressed)
        self.false_button.grid(row=2, column=0)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,
                                   text=f"You've reached the end of the quiz!\n\nFinal score: {self.quiz.score}/10")
            self.false_button.config(state="disabled")
            self.true_button.config(state="disabled")

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def reset_canvas(self):
        self.canvas.config(bg="white")
        self.canvas.itemconfig(self.question_text, fill=THEME_COLOR)
        self.score_label.config(text=f"Score: {self.quiz.score}")
        self.get_next_question()

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
            self.canvas.itemconfig(self.question_text, fill="white")
            # self.quiz.score += 1
        else:
            self.canvas.config(bg="red")
            self.canvas.itemconfig(self.question_text, fill="white")
        self.window.after(1000, self.reset_canvas)
