from django.shortcuts import render
import requests
from .forms import CityForm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from .models import City
def index(request):
    form = CityForm()

    weather_data = []
    
    

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=52b0b05aefe1272798e5c3cc5aa32669'

    cities = City.objects.all() #return all the cities in the database
    if request.method == 'POST': # only true if form is submitted
        form = CityForm(request.POST) # add actual request data to form for processing
        form.save() # will validate and save if validate

    # form = CityForm()
    # weather_data = []
    context = {'weather_data' : weather_data, 'form' : form}
    for city in cities:
        city_weather = requests.get(url.format(city)).json() #request the API data and convert the JSON to Python data types
        # sheet = requests.get(city_weather)
        j_df = pd.read_json('city_weather.json')
        

        with open(j_df) as jsonfile:
            data = json.load(jsonfile)
    
        weather = {
            'city' : city,
            'temperature' : city_weather['main']['temp'],
            'description' : city_weather['weather'][0]['description'],
            'icon' : city_weather['weather'][0]['icon']
        }
        weather_data.append(weather)
    context = {'weather' : weather, 'df':df}

    print(city_weather)
    
    print(df)
    return render(request, 'weather/index.html',context= context) #returns the index.html template