import requests
import datetime

# variables
lat = 39.9389
lon = -8.3152
exclude = "minutely,hourly"
APIKEY = '740b3c7f06c686f5332bd67edab24109'
forecast = {}

# url = 'https://api.openweathermap.org/data/3.0/onecall?lat=39.9389&lon=-8.3152&exclude=hourly&appid=740b3c7f06c686f5332bd67edab24109'
url = f'https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={exclude}&appid={APIKEY}' # with formar

response = requests.get(url)

print("Response status:", response.status_code) # response status code
# print("Response api call:", response.json()) # response json >> all information returned from the api call

# get the variables from the json response
temperature = response.json()['current']['temp'] # current temperature
temperatureCDegrees = temperature - 273.15 # current temperature in Celsius >> from Kevin to Celsius
humidity = response.json()['current']['humidity'] # current humidity
windSpeed = response.json()['current']['wind_speed'] # current wind speed
weatherDescription = response.json()['current']['weather'][0]['description'] # current weather description

daily = response.json()['daily'] # daily informations for the rest of the week
for i in range(len(daily)):

    day = datetime.datetime.fromtimestamp(daily[i]['dt']).strftime('%a, %b %d') # day from dt to day of week,date
    maxTemp = round(daily[i]['temp']['max'] - 273.15) # max tempeature from each day of the week
    minTemp = round(daily[i]['temp']['min'] - 273.15) # min tempeature from each day of the week
    weatherForecast = daily[i]['weather'][0]['description'] # weather description from each day of the week
    
    forecast[day] = {
        'maxTemp' : maxTemp,
        'minTemp' : minTemp,
        'weatherForecast' : weatherForecast
    }
    # print("Forecast", day, ":", forecast[day])

# return some main results about the weather
print()
print("Weather in Aguda, Porto")
print("-----------------------")
print("Temperature: ", temperature, "(kelvin)")
print("Temperature [ºC]: ", round(temperatureCDegrees, 2), "ºC")
print("Humidity: ", humidity, "%")
print("Wind speed: ", windSpeed, "m/s")
print("Current weather description: ", weatherDescription)
print()
print("Forecast for the next 5 days")
print(f"{'week day,date':<20}{'max/min ºC':<21}{'weather description':<20}")
# print(forecast) # table here for the forecast for next 5 days
for day, info in forecast.items():
    
    maxTemp = info['maxTemp']
    minTemp = info['minTemp']
    weatherForecast = info['weatherForecast']

    print(f"{day:<20}{maxTemp:<0}/{minTemp:<0}ºC{'':<15}{weatherForecast}")