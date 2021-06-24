from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self,quizbrain : QuizBrain):
        self.quiz=quizbrain
        self.windows = Tk()
        self.windows.title("Quizzler")
        self.windows.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score:0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question = self.canvas.create_text( 150, 125,width=280, text="Some qns", fill=THEME_COLOR,
                                                font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2,pady=50)

        true_img=PhotoImage(file="images/true.png")
        self.true_button=Button(image=true_img,highlightthickness=0,command=self.true_pressed , bg=THEME_COLOR,bd=0)
        self.true_button.grid(row=2,column=0)

        false_img=PhotoImage(file="images/false.png")
        self.false_button=Button(image=false_img,highlightthickness=0,command=self.false_pressed,bg=THEME_COLOR,bd=0)
        self.false_button.grid(row=2,column=1)

        self.get_next_qn()

        self.windows.mainloop()

    def get_next_qn(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text=self.quiz.next_question()
            self.canvas.itemconfig(self.question,text=q_text)
        else:
            self.canvas.itemconfig(self.question,text=f"You've reached the end of the quiz.Your Final score was {self.quiz.score}/10")
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.true_button.config(state="disable")
            self.false_button.config(state="disable")



    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        is_right=self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.windows.after(1000, self.get_next_qn)

