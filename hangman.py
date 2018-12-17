from tkinter import *
import tkinter
import tkinter.messagebox
from random import *
from PIL import ImageTk, Image

class GUI():
    def __init__(self, window):
        self.window = window
        window.title("Hangman")

        self.label1 = Label(window,text='Hangman parts:')
        self.label1.pack()
        self.label2 = Label(window, text=' ')
        self.label2.pack()
        self.label3 = Label(window, text=' ')
        self.label3.pack()
        self.label4 = Label(window, text='Guess a letter:')
        self.label4.pack()
        self.entry1 = Entry(window, width=5)
        self.entry1.pack()
        self.button1 = Button(window, text='Guess', command=self.game)
        self.button1.pack()
        self.button2 = Button(window, text='Exit',  command=self.window.destroy)
        self.button2.pack()

    def game(self):
        words = ['spock', 'bridge', 'space', 'bones', 'scotty', 'vlucan', 'nexus', 'xenopolycythemia', 'energize',
                 'engineer', 'captain', 'picard', 'frontier']

        wordChoice = words.random()

        missGuess = 0
        guesses = ''

        for char in wordChoice:
            self.label3 = Label.print(char)

            if char in guesses:
                print(char)

            else:
                self.label3 = Label.print("_")
                missGuess += 1

            if missGuess == 1:
                path = ("C:/Users/Marlene/PycharmProjects/Hangman/hangman/01.gif")
                im = Image.open(path)
                tkimage = ImageTk.PhotoImage(im)
                myvar = Label(window, image=tkimage)
                myvar.image = tkimage
                myvar.pack(side="bottom", fill="both", expand="yes")
            if missGuess == 2:
                path = ("C:/Users/Marlene/PycharmProjects/Hangman/hangman/02.gif")
                im = Image.open(path)
                tkimage = ImageTk.PhotoImage(im)
                myvar = Label(window, image=tkimage)
                myvar.image = tkimage
                myvar.pack(side="bottom", fill="both", expand="yes")
            if missGuess == 3:
                path = ("C:/Users/Marlene/PycharmProjects/Hangman/hangman/03.gif")
                im = Image.open(path)
                tkimage = ImageTk.PhotoImage(im)
                myvar = Label(window, image=tkimage)
                myvar.image = tkimage
                myvar.pack(side="bottom", fill="both", expand="yes")
            if missGuess == 4:
                path = ("C:/Users/Marlene/PycharmProjects/Hangman/hangman/04.gif")
                im = Image.open(path)
                tkimage = ImageTk.PhotoImage(im)
                myvar = Label(window, image=tkimage)
                myvar.image = tkimage
                myvar.pack(side="bottom", fill="both", expand="yes")
            if missGuess == 5:
                path = ("C:/Users/Marlene/PycharmProjects/Hangman/hangman/05.gif")
                im = Image.open(path)
                tkimage = ImageTk.PhotoImage(im)
                myvar = Label(window, image=tkimage)
                myvar.image = tkimage
                myvar.pack(side="bottom", fill="both", expand="yes")
            if missGuess == 6:
                path = ("C:/Users/Marlene/PycharmProjects/Hangman/hangman/06.gif")
                im = Image.open(path)
                tkimage = ImageTk.PhotoImage(im)
                myvar = Label(window, image=tkimage)
                myvar.image = tkimage
                myvar.pack(side="bottom", fill="both", expand="yes")
            if missGuess == 7:
                path = ("C:/Users/Marlene/PycharmProjects/Hangman/hangman/07.gif")
                im = Image.open(path)
                tkimage = ImageTk.PhotoImage(im)
                myvar = Label(window, image=tkimage)
                myvar.image = tkimage
                myvar.pack(side="bottom", fill="both", expand="yes")


window = Tk(screenName="Hangman StarTrek Edition")
Hangman = GUI(window)
window.mainloop()
