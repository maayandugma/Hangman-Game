from tkinter import *
from creat_button import Letters
import vocabulary
import screenGame
import hidenLetters


word = vocabulary.the_secret_word

window = screenGame.window

header = Label(
    fg="blue",
    text="Hangman-Game",
    font=("",30)

)
header.place(x=150,y=20)

letter_in_secret_word = hidenLetters.len_secret_letters(word)

button_x_position = 20
button_y_position = 400
button_x2_position = 20
counter = 0

# create the button with letter title
for i in range(26):
    if i < 13:
        l1 = Letters(button_x_position,button_y_position,word,letter_in_secret_word,counter)
        l1.create_btn_object(window,counter) #call to the function that make the button
        l1.button_line(button_x_position,button_y_position) #call the function responsible to place the button in
                                                            # the x&y position
        button_x_position += 40
        counter += 1
    else:
        button_y_position = 500
        l1 = Letters(button_x2_position,button_y_position,word,letter_in_secret_word,counter)
        l1.create_btn_object(window,counter)
        l1.button_line(button_x2_position,button_y_position)
        button_x2_position += 40
        counter += 1


window.mainloop()