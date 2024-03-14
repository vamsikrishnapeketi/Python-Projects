from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class Quizinterface:

    def __init__(self,quiz_brain: QuizBrain): #this ensures that the quiz_brain variable is of type Quizbrain
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score:0",fg="white",bg=THEME_COLOR)
        self.score_label.grid(row=0,column=1)

        self.canvas = Canvas(width=300, height=250, highlightthickness=0,bg="white")
        self.question_text = self.canvas.create_text(150,125,width= 270,text="Amazon acquired twich", font=("Arial", 20, "italic"))
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)

        true_img = PhotoImage(file="./images/true.png")
        self.right_button = Button(image=true_img,command=self.true_button_command)
        self.right_button.grid(row=2, column=0)

        false_img = PhotoImage(file="./images/false.png")
        self.wrong_button = Button(image=false_img, command=self.false_button_command)
        self.wrong_button.grid(row=2,column=1)
        
        self.get_next_question()

        self.window.mainloop( )

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions(): 
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text= q_text)
        else:
            self.canvas.itemconfig(self.question_text, text= "You have reached the end of the quiz")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")#this will ensure that the button is disabled

    def true_button_command(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)
        
    def false_button_command(self):
        is_right = self.quiz.check_answer("False")    
        self.give_feedback(is_right)

    def give_feedback(self,is_right:bool):
        if is_right:    
            self.canvas.config(self.canvas,bg="green")
        else:
            self.canvas.config(self.canvas,bg="red")

        self.window.after(1000, self.get_next_question)    