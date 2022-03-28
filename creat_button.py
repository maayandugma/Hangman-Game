from tkinter import *
import screenGame


class Letters:
    all = []  # contain the x&y position of all letters
    character = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                 "U", "V", "W", "X", "Y", "Z"]
    wrong_letter = []
    correct_letter_guessed = ""

    def __init__(self, x, y, secret_word, letter_in_secret_word, counter):
        self.letter = None
        self.button = None
        self.x = x
        self.y = y
        self.word = secret_word
        self.letter_in_secret_word = letter_in_secret_word
        self.guessed_letter = ""  # the letter that has been guessed
        self.counter = counter
        Letters.all.append(self)
        self.create_hangman()

    def create_btn_object(self, location, counter):
        """
        create the all letters button that the player has to clicked for choose a letter
        for guess the word.
        """
        btn = Button(  # this button get several argument:
            location,  # the area that the button will be
            text=Letters.character[counter],
            width=4,
            height=4,
            command=self.button_clicked
        )
        self.button = btn

    def button_line(self, x, y):
        # that function responsible to place the button in x&y position on the board
        self.button.place(x=x, y=y)

    def button_clicked(self):
        """
        this function get the position of button that has been clicked and add the button value- the letter
        into the guessed_letter list.
        """
        index = 0

        for i in Letters.all:
            if i.x == self.x and i.y == self.y:
                self.guessed_letter = Letters.character[index]
                self.check_letter_guessed()
                break
            else:
                index += 1

    def check_letter_guessed(self):
        if self.guessed_letter not in Letters.wrong_letter:
            if self.guessed_letter in self.letter_in_secret_word.keys():

                place = self.letter_in_secret_word[self.guessed_letter]
                Letters.correct_letter_guessed += self.guessed_letter
                for i in place:
                    lbl = Label(text=self.guessed_letter, font=("Ariel", 15))
                    lbl.place(x=i[0], y=i[1])
                self.check_win()
            else:
                Letters.wrong_letter.append(self.guessed_letter)
                self.create_hangman()

        else:
            self.msg_letter_already_guessed()

    def create_hangman(self):
        """
        This function update the hangman image when the player guess wrong letter
        """
        if len(Letters.wrong_letter) == 0:
            self.canvas = Canvas(width=200, height=300, highlightthickness=0)
            self.canvas_hangman = PhotoImage(file=f"Hangman-{len(Letters.wrong_letter)}.png")
            self.img = self.canvas.create_image(80, 150, image=self.canvas_hangman)
            self.canvas.place(x=0, y=100)
        elif len(Letters.wrong_letter) < 6:
            self.canvas = Canvas(width=200, height=300, highlightthickness=0)
            self.canvas_hangman = PhotoImage(file=f"Hangman-{len(Letters.wrong_letter)}.png")
            self.img = self.canvas.create_image(80, 150, image=self.canvas_hangman)
            self.canvas.place(x=0, y=100)
        else:
            self.canvas = Canvas(width=200, height=300, highlightthickness=0)
            self.canvas_hangman = PhotoImage(file=f"Hangman-6.png")
            self.img = self.canvas.create_image(80, 150, image=self.canvas_hangman)
            self.canvas.place(x=0, y=100)
            self.player_lost()

    def check_win(self):

        if (sorted(set(Letters.correct_letter_guessed))) == sorted(self.letter_in_secret_word.keys()):
            lbl = Label(
                screenGame.window,
                fg="black",
                text="Well done \nYou guess right",
                # width=10,
                # height=10,
                font=("", 30)
                # Font by default accept tuple.the first argument should be the font type. the second will be the size
            )
            lbl.place(x=150, y=150)

    @staticmethod
    def msg_letter_already_guessed():
        # this label is not  need to be belong to each cell, because that is a general information about the game.
        # because of that its not be a instance method
        # we don't want to call this method for each cell object- that's why need to be a static method
        lbl = Label(
            screenGame.window,
            fg="black",
            text="you already choose that letter\n try again",
            width=25,
            height=10,
            font=("", 15)
            # Font by default accept tuple.the first argument should be the font type. the second will be the size
        )
        lbl.place(x=250, y=150)
        screenGame.window.after(1000, lbl.destroy)

    @staticmethod
    def player_lost():
        if len(Letters.wrong_letter) == 6:
            lbl = Label(
                screenGame.window,
                fg="black",
                text="Game-Over\nyou lost",
                font=("", 30)
            )
            lbl.place(x=150, y=150)

    def __repr__(self):
        return f"({self.x},{self.y})"
