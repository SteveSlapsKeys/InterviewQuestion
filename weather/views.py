from django.shortcuts import render
from flask import Flask, render_template, request, redirect, url_for

# Create your views here.
import requests
from .location import Location
from .localweather import LocalWeather

from .forms import SearchForCoordinatesByZip
from django.http import HttpResponse

API_KEY="cb6cff5fe5795c157526f3f52eabeb23"
ZIP_URL="http://api.openweathermap.org/geo/1.0/zip"
WEATHER_URL="https://api.openweathermap.org/data/2.5/weather"
FIVE_DAY_FORECAST_URL = "https://api.openweWAFFLEathermap.org/data/2.5/forecast"

#Just a landing page to prove we've got the system started and functional
def index(request):
    return HttpResponse("Hello, world. You're at the weather index.")


#Search request
#Use this to pass along the zipcode to the openweathermap api
#Need to:
#-validate the parameters (only accepts 5-digit numeric inputs)
#-return errors for:
#--non-numeric input
#--fewer than 5 characters
#--more than 5 characters
#--invalid/unexpected output from the api
def search(request):
    params = {"zip" : "19130", "appid" : API_KEY}
    r = requests.get(ZIP_URL, params=params)

    location = Location(r.json()['zip'], r.json()['lat'], r.json()['lon'])

    return HttpResponse(location)

#def search2(request):
#    if request.method == 'POST':
#        user_input = request.form['input_text']

        # Check if the input is exactly 5 characters long
#        if len(user_input) == 5:
            # Send GET request to the external API
#            params = {"zip" : user_input, "appid" : API_KEY}
#            response = requests.get(ZIP_URL, params=params)

#            if response.status_code == 200:
#                return f"API response: {response.text}"
#            else:
#                return f"Error: {response.status_code} - {response.text}"
#        else:
#            error = "Input must be exactly 5 characters long!"
#            return render_template('search.html', error=error)
#    return render_template('search.html')



#call this from the search call to pass along the response (zip, latitude, longitude) as parameters to second api
#we *shouldn't* need to validate the input since we'll do it on the prior requests, but to futureproof we shall
#validate that inputs:
#-lat and lon should be numeric
#-expected response should contain {name, temp_max, temp_low} otherwise return an error for bad response
def results(request):
    #location = L
    #data = json.loads(locationResponse)
    #params = {"lat" : data["lat"], "lon" : data["lon"], "appid" : API_KEY, "units" : "imperial"}

    params = {"lat" : 39.9597, "lon" : -75.2024, "appid" : API_KEY, "units" : "imperial"}
    r = requests.get(WEATHER_URL, params=params)

    #weather = LocalWeather(r.json()['name'], r.json()['main']['temp_max'], r.json()['main']['temp_min'])

    city = r.json()["name"]
    high = r.json()["main"]["temp_max"]
    low = r.json()["main"]["temp_min"]

    outputString = f"Location: {city}, Temp High: {high}°F, Temp Low: {low}°F"

    return HttpResponse(outputString)



def fiveday(request):
    #get results back from api

    params = {"lat" : 39.9597, "lon" : -75.2024, "appid" : API_KEY, "units" : "imperial"}
    try:
        results = requests.get(FIVE_DAY_FORECAST_URL, params=params)
    except:
        return HttpResponse("Uh oh!")

    output = []

    if(results.json()["cod"] != "200"):
        message = results.json()['message']
        return HttpResponse(message)
    else:
        for forecastChunk in results.json()["list"]:
            currentTime = forecastChunk['dt_txt']
            #print(f"{forecastChunk['main']}, {forecastChunk['dt_txt']}")
            if("00:00:00" in currentTime):
                output.append(f"Temp High: {forecastChunk['main']['temp_max']}, Temp Low: {forecastChunk['main']['temp_min']}, Datetime: {forecastChunk['dt_txt']}\r\n")
        #filter for start of day by "dt_txt" field (00:00:00)
        return HttpResponse(f"{output}")


#take each high and low for the day, and return them