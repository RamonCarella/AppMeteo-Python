from tkinter import *
import requests
import json


def showCity():
    #CityLabel.config( text = In_City.get())

    weatherApiKey = '68f4fa0d68fc858ac5aa55e4524ea24f'
    city = In_City.get()
    url = "http://api.openweathermap.org/data/2.5/weather?appid=" + weatherApiKey + "&q=" + city
    data = requests.get(url).json()
    if data["cod"] != "404":
        y = data["main"]
    current_temperature = y["temp"]
    current_temperature -= 274.04
    current_pressure = y["pressure"]
    current_pressure *= 0.0009869233
    current_humidity = y["humidity"]
    z = data["weather"]
    weather_description = z[0]["description"]
    degree_sign = u"\N{DEGREE SIGN}"
    temperature = "{:.0f}".format(current_temperature) + degree_sign + "C"
    pressure = "{:.0f}".format(current_pressure) + " atm"
    humidity = str(current_humidity) + "%"
    details = weather_description



    labelCity.config(text="Currently in " + city.upper())
    labelTemperature.config(text="Temperature: " + temperature + ", " + details)
    labelPressure.config(text="Pressure: " + pressure)
    labelHumidity.config(text="Humidity: " + humidity)







root = Tk()


root.geometry('600x500')

root.title("Meteo App")
root.resizable(0,0) 


Label(root, text="Meteo App from Ramon&Braga o Braga&Ramon").pack(pady=50)


labelCity = Label(root, fg='purple', font="poppins 15 ")
labelTemperature = Label(root, fg='purple', font='poppins 15')
labelPressure = Label(root, fg='purple', font="poppins 15 ")
labelHumidity = Label(root, fg='purple', font="poppins 15 ")





In_City = Entry(root)
In_City.pack(pady=10)
Button(root, command = showCity, text = "Check Weather").pack()
labelCity.pack(pady=10)
labelTemperature.pack()
labelPressure.pack()
labelHumidity.pack()

root.mainloop()

    
