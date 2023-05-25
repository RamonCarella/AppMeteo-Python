from flask import Flask, render_template, request
import requests
import json
from datetime import timedelta
from datetime import date as d
app = Flask(__name__)

today = d.today()
day1 = today
day2 = today + timedelta(days=1)
day3 = today + timedelta(days=2)
day4 = today + timedelta(days=3)
day5 = today + timedelta(days=4)
day6 = today + timedelta(days=5)
day7 = today + timedelta(days=6)

@app.route('/', methods=['GET', 'POST'])
def index():
  

   
    if request.method == "POST":
        global city 
        global data 
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
        extractedData = exctractData(data, today)[0]
        temp = extractedData['temp']
        humidity = extractedData['rh']
        wind_speed = extractedData['wind_spd']
        description = extractedData['weather']['description']

        return render_template("result.html", temp=temp, humidity=humidity,wind_speed=wind_speed, city=city, 
                                country_code=country_code, description=description, day1=day1, day2=day2,
                                day3=day3, day4=day4, day5=day5, day6=day6, day7=day7)

    return render_template("index.html")



def exctractData(dataToExtract, currentDate):
    tmp = dataToExtract["data"]
    return [element for element in tmp if element['datetime'] == currentDate.strftime('%Y-%m-%d')]

@app.route("/button", methods=['POST'])
def handle_button():
    print("ciao")

    button_name = request.form['name']

    if button_name == 'day1':
        extractedData = exctractData(data, day1)[0]
        pass
    elif button_name == 'day2':
        extractedData = exctractData(data, day2)[0]
        pass
    elif button_name == 'day3':
        extractedData = exctractData(data, day3)[0]
        pass
    elif button_name == 'day4':
        extractedData = exctractData(data, day4)[0]
        pass
    elif button_name == 'day5':
        extractedData = exctractData(data, day5)[0]
        pass
    elif button_name == 'day6':
        extractedData = exctractData(data, day6)[0]
        pass
    elif button_name == 'day7':
        extractedData = exctractData(data, day7)[0]
        pass
    
    country_code = data['country_code']
    temp = extractedData['temp']
    humidity = extractedData['rh']
    wind_speed = extractedData['wind_spd']
    description = extractedData['weather']['description']

    return render_template("result.html", temp=temp, humidity=humidity,wind_speed=wind_speed, city=city, 
                                country_code=country_code, description=description, day1=day1, day2=day2,
                                day3=day3, day4=day4, day5=day5, day6=day6, day7=day7)

