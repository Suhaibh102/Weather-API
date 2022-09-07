import datetime as dt
import pip._vendor.requests


# Asks user what city they are in and calls Open Weather API

BaseURL = "https://api.openweathermap.org/data/2.5/weather?"
APIKey = "68cf0d663996bb9e61bbdb00c9e5cf0c"
City = input("What city are you in? ")


# Function that converts units to Celsius and Fahrenheit
def UnitConversion(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9/5) +32
    return celsius, fahrenheit


# Calls Individualized API Key
Url = BaseURL + "appid=" + APIKey + "&q=" + City
response = pip._vendor.requests.get(Url).json()


# Defines all variables which will tell user diffrent information based on their city
tempKelvin = response["main"]["temp"]
tempCelsius, tempFahrenheit = UnitConversion(tempKelvin)
feelsLikeKelvin = response["main"]["feels_like"]
feelsLikeCelsius, feelsLikeFahrenheit = UnitConversion(feelsLikeKelvin)
humidity = response["main"]["humidity"]
description = response["weather"][0]["description"]
sunriseTime = dt.datetime.utcfromtimestamp(response["sys"]["sunrise"] + response["timezone"])
sunsetTime = dt.datetime.utcfromtimestamp(response["sys"]["sunset"] + response["timezone"])
windSpeed = response["wind"]["speed"]


# Prints all the variables in a way the user can easily read
print(f"Tempreture in {City}: {tempCelsius:.2f} degrees Celsius or {tempFahrenheit:.2f} degrees Fahrenheit")
print(f"Tempreture in {City} feels like: {feelsLikeCelsius:.2f} degrees Celsius or {feelsLikeFahrenheit:.2f} degrees Fahrenheit")
print(f"Humidity in {City}: {humidity}%")
print(f"Wind speed in {City}: {windSpeed}m/s")
print(f"General Weather in {City}: {description}!")
print(f"The sun will rise at {sunriseTime}")
print(f"The sun will set at {sunsetTime}")




print("Thanks for tuning in!!!")



