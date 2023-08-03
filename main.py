import requests
import os
from datetime import datetime

user_api = 'a889a5a6c151cf0282a5335e8d4d688e'
location = input("Enter City Name : ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+user_api
api_link = requests.get(complete_api_link)
api_data = api_link.json()

if api_data['cod'] == '404':
    print("Invalid City : {} Please check your city name ".format(location))
else:
    temp_city = ((api_data['main']['temp']) -273.15)
    weather_desc = api_data['weather'][0]['description']
    hmdt = api_data['main']['humidity']
    wind_spd = api_data['wind']['speed']
    date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

    print("Weather Status For - {} || {}".format(location.upper(), date_time))
    print("Current Temperature : {:.2f} deg C".format(temp_city))
    print("Current Weather Desc : ",weather_desc)
    print("Current Humidity : ",hmdt,"%")
    print("Current Wind Speed : ",wind_spd,"KMPH")