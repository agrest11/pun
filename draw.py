# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from tkinter import *
import random
import codecs

list_of_words = []
with codecs.open('words.txt', 'r', 'utf-8') as f:
    for line in f:
        list_of_words.append(line.strip('\n'))

root = Tk()
root.title('Kalambury')

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

def drawWord():
    for widget in frame.winfo_children():
        widget.destroy()

    word = random.choice(list_of_words)
    list_of_words.remove(word)

    label = Label(frame, text=word, font=('FilmotypePower', 60), bg='cornflowerblue', fg='black')
    label.place(relx=0.5, rely=0.5, anchor='center')

    if not list_of_words:
        comment = 'Game over!'
        label = Label(frame, text=comment, font=('FilmotypePower', 60), bg='cornflowerblue', fg='red')
        label.place(relx=0.5, rely=0.5, anchor='center')

canvas = Canvas(root, height=screen_height-100, width=screen_width, bg='cornflowerblue')
canvas.pack()

frame = Frame(root, bg='cornflowerblue')
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

draw = Button(root, text='Draw', padx=10, pady=5, fg='white', bg='dimgray', command=drawWord)
draw.pack()

root.mainloop()
