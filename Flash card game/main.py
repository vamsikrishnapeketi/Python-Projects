import pandas
import random
from tkinter import *

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
finally:
    word_dict = data.to_dict(orient="records")
    current_card = {}

BACKGROUND_COLOR = "#B1DDC6"

def displaying_french_cards():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(word_dict)
    canvas.itemconfig(title_canvas, text = "French", fill = "black")
    canvas.itemconfig(word_canvas,text = current_card["French"], fill= "black")
    canvas.itemconfig(card_bg, image= card_front_img)
    flip_timer = window.after(3000, func=displaying_english_cards)

def displaying_english_cards():
    canvas.itemconfig(title_canvas, text= "English",fill = "white")
    canvas.itemconfig(word_canvas, text= current_card["English"], fill = "white")
    canvas.itemconfig(card_bg, image= card_back_img)

def right_button_function():
    try:    
        word_dict.remove(current_card) 
        new_data = pandas.DataFrame(word_dict)
        new_data.to_csv("data/words_to_learn.csv", index=False)   
        displaying_french_cards()
    except ValueError:
        displaying_french_cards()
window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50,bg=BACKGROUND_COLOR)

flip_timer = window.after(3000,func=displaying_english_cards)

canvas = Canvas(width=800,height=526,highlightthickness=0)
card_front_img = PhotoImage(file="./images/card_front.png")
card_bg = canvas.create_image(400,263,image = card_front_img)

title_canvas = canvas.create_text(400,150, text="Title", font=("Ariel",40,"italic"))
word_canvas = canvas.create_text(400,263, text="Word", font=("Ariel",60,"bold"))

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row = 0,column=0,columnspan=2)

wrong_img = PhotoImage("wrong.png")
card_back_img = PhotoImage(file = "images/card_back.png")
wrong_button = Button(image = wrong_img,width=100,height=99,command=displaying_french_cards)
wrong_button.grid(row=1, column=0)

right_img = PhotoImage(file="./images/right.png")
right_button = Button(image=right_img,command=right_button_function)
right_button.grid(row=1, column=1)




window.mainloop()
