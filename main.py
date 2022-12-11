from tkinter import *
import requests
import json


def showCity():
    #CityLabel.config( text = In_City.get())
    #request to the server


    weatherApiKey = 'ae855886b5a048dc9a8e8d9ceecc3171'
    weatherApiKey2 = '578fc598de1f4e5a8dd96fe4b9c9d0be'
    city = In_City.get()
    url = "https://api.weatherbit.io/v2.0/forecast/daily?city=" + city + "&key="+ weatherApiKey
    
    #se la città inserita non esiste lo segnala
    try:
        data = requests.get(url).json()
        json_object = json.dumps(data, indent = 4) 
        #print(json_object)
    except:
        #print("City doesn't exist")
        labelCity.config(text="City doesn't exist or invalid key")
        labelTemperature.config(text="")
        labelPressure.config(text="")
        labelHumidity.config(text="")
    #else:
    #    print("Data ok")

    #la nuova api non ha un codice errore, quindi si deve fare tutto con il try catch
    #se non si trova la citta, la requests (riga 14) da errore
    #le info sui campi della API a questo link:
    #https://www.weatherbit.io/api/weather-forecast-16-day
    """
    if data["cod"] == 404:
        labelCity.config(text="ERROR 404")
        labelTemperature.config(text="")
        labelPressure.config(text="")
        labelHumidity.config(text="")
    elif data["cod"] == 401:
       print("Errore Invalid Key")
    else:
        #y = data["list"]
        print("\n\nSIUUUUM")
    """
    
    #labelCity.config(text=y["temp"])
    """   
    #take and calculate the measures
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
    
    #update the measures
    labelCity.config(text="Currently in " + city.upper())
    labelTemperature.config(text="Temperature: " + temperature + ", " + details)
    labelPressure.config(text="Pressure: " + pressure)
    labelHumidity.config(text="Humidity: " + humidity)
    """
    
#setup the main sceen
root = Tk()
root.geometry('600x500')
root.title("Meteo App")
root.resizable(0,0) 

#create and setup all the labels
Label(root, text="Meteo App from Ramon&Braga o Braga&Ramon").pack(pady=50)
labelCity = Label(root, fg='purple', font="poppins 15 ")
labelTemperature = Label(root, fg='purple', font='poppins 15')
labelPressure = Label(root, fg='purple', font="poppins 15 ")
labelHumidity = Label(root, fg='purple', font="poppins 15 ")

#create the textfield and the submit button
In_City = Entry(root)
In_City.pack(pady=10)
Button(root, command = showCity, text = "Check Weather").pack()
labelCity.pack(pady=10)
#show the labels
labelTemperature.pack()
labelPressure.pack()
labelHumidity.pack()

root.mainloop()

    
