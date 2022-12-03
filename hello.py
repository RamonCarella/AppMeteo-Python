from tkinter import *
import requests
import json

root = Tk()
root.geometry('600x400')

root.title("Meteo App from Ramon&Braga o Braga&Ramon")
root.resizable(0,0) 


headingLabel = Label(root, text="Meteo App from Ramon&Braga o Braga&Ramon")
headingLabel.pack()


myLabel = Label(root, text="rrcamadonna")
myLabel.pack()

canvas1 = Canvas(root, width=600, height=400)
canvas1.pack()
entry1 = Entry(root)
canvas1.create_window(200, 30, window=entry1)


root.mainloop()