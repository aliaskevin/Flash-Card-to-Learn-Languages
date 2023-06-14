from tkinter import *
import pandas
from random import choice

# ---------------------------- CONSTANTS ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"
FONT = "Ariel"

timer = None
new_word = {}

# ---------------------------- BUTTON FUNCTION ------------------------------- #
def right_click():
    word_list.remove(new_word)
    new_dataframe = pandas.DataFrame(word_list)
    new_dataframe.to_csv("words_to_learn.csv", index=False)
    button_click()


def button_click():
    global timer, new_word
    window.after_cancel(timer)
    new_word = choice(word_list)
    canvas.itemconfig(canvas_image, image=card_front)
    canvas.itemconfig(word, fill="black", text=new_word["French"])
    canvas.itemconfig(title, fill="black", text="French")
    timer = window.after(3000, func=english_card)


def english_card():
    global new_word
    canvas.itemconfig(word, fill="white", text=new_word["English"])
    canvas.itemconfig(title, fill="white", text="English")
    canvas.itemconfig(canvas_image, image=card_back)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="./card_front.png")
card_back = PhotoImage(file="./card_back.png")
canvas_image = canvas.create_image(400, 263)
word = canvas.create_text(400, 263, text="", font=(FONT, 60, "bold"))
title = canvas.create_text(400, 150, text="", font=(FONT, 40, "italic"))
canvas.grid(column=0, row=0, columnspan=2)

wrong_image = PhotoImage(file="./wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=button_click)
wrong_button.grid(column=0, row=1)
right_image = PhotoImage(file="./right.png")
right_button = Button(image=right_image, highlightthickness=0, command=right_click)
right_button.grid(column=1, row=1)

try:
    word_data = pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
    word_data = pandas.read_csv("french_words.csv")
word_list = word_data.to_dict(orient="records")

timer = window.after(3000, func=english_card)
button_click()

window.mainloop()
