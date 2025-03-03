from tkinter import *

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.geometry("400x600")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

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
        self.question_text = self.canvas.create_text(150, 125, text="Question is here", fill="black", font=40)
        self.canvas.grid(column=0, row=1, columnspan=3, pady=50)

        self.true_button = Button(image=self.true_img, highlightthickness=0)
        self.true_button.grid(column=0,row=2,pady=20)

        self.false_button = Button(image=self.false_img, highlightthickness=0)
        self.false_button.grid(column=2, row=2, pady=20)




        self.window.mainloop()

