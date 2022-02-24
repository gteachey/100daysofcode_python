# icons from: https://www.flaticon.com/

import os
from tkinter import PhotoImage, Button, Tk, Canvas
from tkinter import messagebox
import pandas

BACKGROUND_COLOR = "#B1DDC6"


def change_button_state():
    if (known_image_button['state'] == 'active' or known_image_button['state'] == 'normal') and \
            (need_to_learn_button['state'] == 'active' or need_to_learn_button['state'] == 'normal'):
        known_image_button['state'] = 'disabled'
        need_to_learn_button['state'] = 'disabled'
    else:
        known_image_button['state'] = 'normal'
        need_to_learn_button['state'] = 'normal'


# Set Timer Function
def show_answer():
    canvas.itemconfigure(tagOrId=title, text=flash_card_back_title)
    canvas.itemconfigure(tagOrId=image, image=card_back_image)
    canvas.itemconfigure(tagOrId=text, text=answer_word)
    change_button_state()


# Get the next card
def next_card():
    canvas.itemconfigure(tagOrId=title, text=flash_card_front_title)
    canvas.itemconfigure(tagOrId=image, image=card_front_image)
    canvas.itemconfigure(tagOrId=text, text=challenge_word)
    window.after(ms=3000, func=show_answer)


# Define what happens when the correct button is pressed
def correct_button_pressed():
    global flash_card_data, flash_card_row, challenge_word, answer_word
    flash_card_data = flash_card_data.drop(index=flash_card_row.index.values[0])
    if len(flash_card_data) > 0:
        flash_card_row = flash_card_data.sample()
        challenge_word = flash_card_row[flash_card_front_title].values[0]
        answer_word = flash_card_row[flash_card_back_title].values[0]
        change_button_state()
        next_card()
    else:
        # Quit the program and delete the saved file if we've run out of rows
        # Show message box to the user that they've run out of words
        messagebox.showinfo(title="All Done!",
                            message="You've completed all flash_cards.\n\nRun this program again to start over.")
        if os.path.exists("data/continue_learning.csv"):
            os.remove("data/continue_learning.csv")
        quit(0)


# Define Wrong Button
def need_to_learn_button_pressed():
    global flash_card_data, flash_card_row, challenge_word, answer_word
    flash_card_row = flash_card_data.sample()
    challenge_word = flash_card_row[flash_card_front_title].values[0]
    answer_word = flash_card_row[flash_card_back_title].values[0]
    change_button_state()
    next_card()


# Check for our saved file, use the original if it doesn't exist
if os.path.exists("data/continue_learning.csv"):
    flash_card_data = pandas.read_csv("data/continue_learning.csv")
else:
    flash_card_data = pandas.read_csv("data/french_words.csv")

# Get column headers from DataFrame
flash_card_front_title = flash_card_data.columns[0]
flash_card_back_title = flash_card_data.columns[1]

# Check if there's any row data in the file imported. If not, show a message and quit.
try:
    flash_card_row = flash_card_data.sample()  # Randomly grab a row using sample method
except ValueError as value:
    messagebox.showinfo(title="File Has No Data", message=f"The file provided doesn't have data to use.")
    quit(1)

# Get the challenge and answer words from our random row
challenge_word = flash_card_row[flash_card_front_title].values[0]
answer_word = flash_card_row[flash_card_back_title].values[0]

# Set up the window
window = Tk()
window.config(background=BACKGROUND_COLOR, padx=50, pady=50)
window.title("Flash Card App")

# Set up the Canvas with images and text to use for it
canvas = Canvas(width=800, height=600)
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
image = canvas.create_image(400, 300, image=card_front_image)
title = canvas.create_text(400, 150, text=flash_card_front_title, font=("Arial", 40, "italic"))
text = canvas.create_text(400, 300, text=challenge_word, font=("Arial", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# Set up the buttons
need_to_learn_image = PhotoImage(file="images/need_to_learn.png")
need_to_learn_button = Button(
    image=need_to_learn_image,
    highlightthickness=0,
    command=need_to_learn_button_pressed,
    bg=BACKGROUND_COLOR
)
need_to_learn_button.grid(column=0, row=1)

known_image = PhotoImage(file="images/known.png")
known_image_button = Button(
    image=known_image,
    highlightthickness=0,
    command=correct_button_pressed,
    bg=BACKGROUND_COLOR
)
known_image_button.grid(column=1, row=1)

# Start with buttons disabled
change_button_state()
window.after(ms=3000, func=show_answer)
icon = PhotoImage(file="images/cards.png")
window.iconphoto(False, icon)
window.mainloop()

# Save the words still in the DataFrame when the 'X' button is pressed
flash_card_data.to_csv(path_or_buf="data/continue_learning.csv", index=False)
