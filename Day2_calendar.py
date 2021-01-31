import requests
from datetime import datetime
from pytz import timezone
from bs4 import BeautifulSoup

url = "https://community-open-weather-map.p.rapidapi.com/weather"

querystring = {"q":"","lat":"0","lon":"0","id":"2172797","lang":"null","units":"metric","mode":"xml, html"}
querystring["q"] = input("Choose city: ")

headers = {
    'x-rapidapi-key': "458c8852f8msh4da7f7cf71021bdp177d3fjsn1f3d90436f6c",
    'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com"}

response = requests.request("GET", url, headers=headers, params=querystring).json()

if response['cod'] == 200:
    print("Weather: {}, {}".format(response["weather"][0]['main'], response["weather"][0]['description']))
    print("Temperature: {:.2f} C".format(response["main"]["temp"]))
    print("Pressure: {} hPa".format(response["main"]["pressure"]))
    print("Humidity: {} %".format(response["main"]["humidity"]))
    print("Wind: {} km/h".format(response["wind"]["speed"]))
else:
    print("No data for this city!")
    
fmt = '%Y-%m-%d %H:%M:%S'
print("\nAmsterdam: {}".format(datetime.now(timezone("Europe/Amsterdam")).strftime(fmt)))
print("Singapore: {}".format(datetime.now(timezone("Asia/Singapore")).strftime(fmt)))
print("New York: {}".format(datetime.now(timezone("US/Eastern")).strftime(fmt)))

response = requests.request("GET", "https://imienniczek.pl/widget/js")
soup = BeautifulSoup(response.text, "html.parser")
print("")
for name_day in soup.find_all("a"):
    print(name_day.text)