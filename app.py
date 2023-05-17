from flask import Flask, render_template, request
import requests
import json
from datetime import timedelta
from datetime import date as d
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
  
    currentDate = d.today()
      
    if request.method == "POST":
        city = request.form['city']
        weatherApiKey = 'ae855886b5a048dc9a8e8d9ceecc3171'
        weatherApiKey2 = '578fc598de1f4e5a8dd96fe4b9c9d0be'


        #la nuova api non ha un codice errore, quindi si deve fare tutto con il try catch
        #se non si trova la citta, la requests (riga 14) da errore
        #le info sui campi della API a questo link:
        #https://www.weatherbit.io/api/weather-forecast-16-day
        try:
            url = "https://api.weatherbit.io/v2.0/forecast/daily?city=" + city + "&key="+ weatherApiKey
            data = requests.get(url).json()
            json_object = json.dumps(data, indent = 4) 
            print(json_object)
        except:
            try:
                url = "https://api.weatherbit.io/v2.0/forecast/daily?city=" + city + "&key="+ weatherApiKey2
                data = requests.get(url).json()
                json_object = json.dumps(data, indent = 4) 
            except:
                print("City doesn't exist or invalid key")

        country_code = data['country_code']
        extractedData = exctractData(data, currentDate)[0]
        temp = extractedData['temp']
        humidity = extractedData['rh']
        wind_speed = extractedData['wind_spd']
        description = extractedData['weather']['description']
        print(city)
        print(temp)
        print(humidity)
        print(wind_speed)


        return render_template("result.html", temp=temp, humidity=humidity, 
                               wind_speed=wind_speed, city=city, country_code=country_code, description=description)

    return render_template("index.html")



def exctractData(dataToExtract, currentDate):
    tmp = dataToExtract["data"]
    return [element for element in tmp if element['datetime'] == currentDate.strftime('%Y-%m-%d')]
    
   
def changeTomorrow(currentDate):
    if((currentDate - d.today()).days >= 6):
        pass
    else:    
        currentDate = currentDate + timedelta(days=1)
    return currentDate

def changeYesterday(currentDate):
    
    if((currentDate - d.today()).days <= 0):
        pass
    else:    
        currentDate = currentDate - timedelta(days=1)
    return currentDate