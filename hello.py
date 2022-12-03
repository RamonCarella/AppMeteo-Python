from tkinter import *
import requests
import json


def showCity():
    cityLabel = Label(root, text="City_Var").pack()

root = Tk()
root.geometry('600x400')

root.title("Meteo App")
root.resizable(0,0) 


headingLabel = Label(root, text="Meteo App from Ramon&Braga o Braga&Ramon").pack(pady=50)



City_Var = StringVar()
In_City = Entry(root, textvariable = City_Var).pack()
Button(root, command = showCity, text = "Check Weather").pack()

root.mainloop()

    
