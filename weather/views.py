from django.shortcuts import render
from flask import Flask, render_template, request, redirect, url_for

# Create your views here.
import requests

from .forms import SearchForCoordinatesByZip
from django.http import HttpResponse

API_KEY="cb6cff5fe5795c157526f3f52eabeb23"
ZIP_URL="http://api.openweathermap.org/geo/1.0/zip"
WEATHER_URL="https://api.openweathermap.org/data/2.5/weather"

def index(request):
    return HttpResponse("Hello, world. You're at the weather index.")

#def search(request):
#    params = {"zip" : "19104", "appid" : API_KEY}
#    r = requests.get(ZIP_URL, params=params)
#    return HttpResponse(r.json())

def search(request):
    if request.method == 'POST':
        user_input = request.form['input_text']

        # Check if the input is exactly 5 characters long
        if len(user_input) == 5:
            # Send GET request to the external API
            params = {"zip" : user_input, "appid" : API_KEY}
            response = requests.get(ZIP_URL, params=params)

            if response.status_code == 200:
                return f"API response: {response.text}"
            else:
                return f"Error: {response.status_code} - {response.text}"
        else:
            error = "Input must be exactly 5 characters long!"
            return render_template('search.html', error=error)
    return render_template('search.html')



def results(request):
    #location = L
    #data = json.loads(locationResponse)
    #params = {"lat" : data["lat"], "lon" : data["lon"], "appid" : API_KEY, "units" : "imperial"}

    params = {"lat" : 39.9597, "lon" : -75.2024, "appid" : API_KEY, "units" : "imperial"}
    r = requests.get(WEATHER_URL, params=params)

    city = r.json()["name"]
    high = r.json()["main"]["temp_max"]
    low = r.json()["main"]["temp_min"]

    outputString = f"Location: {city}, Temp High: {high}°F, Temp Low: {low}°F"

    return HttpResponse(outputString)

#def search(response):
#    if response.method == "GET":
#        form = SearchForCoordinatesByZip(response.GET)
#        if(form.is_valid()):
#            zip = form.cleaned_data["zip"]

#            data = requests.get("http://api.openweathermap.org/geo/1.0/zip?zip={zip}&appid={API_KEY}")
#            lat = data.json()["lat"]
#            lon = data.json()["lon"]
#            return HttpResponse("lat: " + lat + ", lon: " + lon)
            #return a different view
#        else:
#            return HttpResponse("Form is not properly filled!")
#    else:
#        form = SearchForCoordinatesByZip()
#    return HttpResponse("Uhhhh")

###