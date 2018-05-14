"""
This module presents weather using name of the city
from http://openweather.org/ api service
"""

import requests


def weather_right_now(location: str or dict, api_key: str)-> dict:
    """
    Function which request for right now weather using city name

    :param location: city name or dict with location
    :param api_key: api_key from http://openweather.org/
    :return: data
    """
    url = "http://api.openweathermap.org/data/2.5/weather"
    if isinstance(location, str):
        querystring = {"q": location,
                       "appid": api_key
                       }
    elif isinstance(location, dict):
        try:
            querystring = {
                'lat': location['coordinates']['lat'],
                'lon': location['coordinates']['lon'],
                'appid': api_key
            }
        except KeyError:
            raise ValueError(f'Invalid coordinates {location["coordinates"]}')
    else:
        raise TypeError(f'Invalid location: {location}')

    headers = {
        'Cache-Control': "no-cache",
        'Postman-Token': "78d87825-7f55-45bc-a57b-79b71b198875"
    }

    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()
    if data['cod'] >= 401:
        raise requests.RequestException(f'There is a little problem {data["message"]}')
    return data


def weather_forecast_5_days(location: str or dict, api_key: str)-> dict:
    """
    Function for weather forecast using city name

    :param location: city name or dict with location
    :param api_key: api_key from http://openweather.org/
    :return: data
    """
    url = "http://api.openweathermap.org/data/2.5/forecast"

    if isinstance(location, str):
        querystring = {"q": location,
                       "appid": api_key
                       }
    elif isinstance(location, dict):
        try:
            querystring = {
                'lat': location['coordinates']['lat'],
                'lon': location['coordinates']['lon'],
                'appid': api_key
            }
        except KeyError:
            raise ValueError(f'Invalid coordinates {location["coordinates"]}')
    else:
        raise TypeError(f'Invalid location: {location}')

    headers = {
        'Cache-Control': "no-cache",
        'Postman-Token': "1739cee8-9c8b-44e4-91a4-d50d23ebc0d4"
    }

    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()
    if data['cod'] >= 400:
        raise requests.RequestException(f'There is a little problem {data["message"]}')
    return data


def printer_right_now_weather(data: dict)->None:
    """
    Function which print weather data right now

    :param data: data from api
    :return: None
    """
    print('-----------------------')
    print(f'Right now at {data["name"]} is {data["weather"][0]["description"]}')
    print('-----------------------')
    print(f'Temperature is {round(data["main"]["temp"]-273.15, 3)}')
    print(f'Humidity is {data["main"]["humidity"]} %')
    print(f'Pressure is {round(data["main"]["pressure"]*100*0.0075, 3)} in Millimeter of mercury')
    print('-----------------------')


def printer_weather_forecast(data: dict)-> None:
    """
    Function which print weather forecast

    :param data: data from api
    :return: None
    """
    for item in data["list"]:
        print('-----------------------')
        print(f'Weather on {item["dt_txt"]} at {data["city"]["name"]} is {item["weather"][0]["description"]}')
        print('-----------------------')
        print(f'Temperature is {round(item["main"]["temp"]-273.15, 3)}')
        print(f'Humidity is {item["main"]["humidity"]} %')
        print(f'Pressure is {round(item["main"]["pressure"]*100*0.0075, 3)} in Millimeter of mercury')
        print('-----------------------')


if __name__=='__main__': #pragma no cover
    pass