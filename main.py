from tkinter import *
from tkinter import colorchooser
import math


def click():
    color = colorchooser.askcolor()
    code = color[1]
    hexcode = Entry(window, text=code, bg='gray', fg='black', font=('Arial', 15), relief=FLAT, width=7)
    hexcode.pack(pady=3)
    hexcode.insert(1, code)
    rgb = color[0]
    print("Hex: " + code)
    print(f"R: {rgb[0]}\nG: {rgb[1]}\nB: {rgb[2]}")
    # print("Coded & Designed By Mohanad Medhat")


window = Tk()
window.title("Hex Color Picker")
window.config(background='gray')
width = 263
height = 140
screenwidth = window.winfo_screenwidth()
screenheight = window.winfo_screenheight()
window.geometry(f"{width}x{height}+{math.floor((screenwidth / 2) - (width / 2))}+{math.floor((screenheight / 2) - (height / 2) - 30)}")
button = Button(window, text='Pick a Color', relief=RAISED, bd=5, font=('Impact', 30, 'bold', 'underline'), fg='gray', bg='black', activeforeground='black', activebackground='gray', padx=15, pady=10, command=click)
button.pack()
window.mainloop()
