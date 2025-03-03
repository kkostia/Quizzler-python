from tkinter import *
<<<<<<< HEAD
=======
from quiz_brain import QuizBrain
>>>>>>> 9bfa458 (Final build)

THEME_COLOR = "#375362"

class QuizInterface:

<<<<<<< HEAD
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.geometry("400x600")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
=======

    def __init__(self,quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.geometry("400x600")
        self.bgcolor = self.window.config(padx=20, pady=20, bg=THEME_COLOR)
>>>>>>> 9bfa458 (Final build)

        #Uploading images
        self.true_img = PhotoImage(file="images/true.png")
        self.false_img = PhotoImage(file="images/false.png")

        # Configure grid columns
        self.window.columnconfigure(0, weight=1)  # Left padding
        self.window.columnconfigure(1, weight=1)  # Center
        self.window.columnconfigure(2, weight=1)  # Right padding

        # Score label (top right)
        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white", font=44)
        self.score_label.grid(column=2, row=0, sticky="e", padx=20, pady=20)

        # Canvas (centered)
        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
<<<<<<< HEAD
        self.question_text = self.canvas.create_text(150, 125, text="Question is here", fill="black", font=40)
        self.canvas.grid(column=0, row=1, columnspan=3, pady=50)

        self.true_button = Button(image=self.true_img, highlightthickness=0)
        self.true_button.grid(column=0,row=2,pady=20)

        self.false_button = Button(image=self.false_img, highlightthickness=0)
        self.false_button.grid(column=2, row=2, pady=20)




        self.window.mainloop()

=======
        self.question_text = self.canvas.create_text(150, 125,width=280, text="Question is here", fill="black", font=40)
        self.canvas.grid(column=0, row=1, columnspan=3, pady=50)

        self.true_button = Button(image=self.true_img, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(column=0, row=2 ,pady=20)

        self.false_button = Button(image=self.false_img, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(column=2, row=2, pady=20)

        self.get_next_question()

        self.window.mainloop()



    def get_next_question(self):
        self.canvas.config(bg="WHITE")
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)
        self.score_label.config(text=f"Score: {self.quiz.score}")


    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="GREEN")
        else:
            self.canvas.config(bg="RED")
        self.window.after(1000, self.get_next_question)






>>>>>>> 9bfa458 (Final build)
