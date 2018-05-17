import unittest
import requests
from supertool import weather
from supertool import nominatim_geolocation
from io import StringIO
from unittest.mock import patch


class Testing_Nominatim_Geolocation(unittest.TestCase):
    """
    This class for testing nominatim geolocation thing
    """
    def test_get_coordinates_functionality(self):
        """positive testing get coordinates function"""

        result = {'coordinates': {'lat': '46.7323875', 'lon': '-117.0001651'},
                  'display_name': 'Moscow, Latah County, Idaho, United States of America'}

        self.assertDictEqual(result, nominatim_geolocation.get_coordinates('Moscow'))

    def test_get_coordinates_functionality_with_incorrect_adress(self):
        """negative testing get coordinates function"""
        address = 'Lipetsk12344ffas'
        with self.assertRaises(ValueError) as raised_exception:
            nominatim_geolocation.get_coordinates(address)
        self.assertEqual(raised_exception.exception.args[0],
                         f'Incorrect address: {address}')

class Testing_Weather_Module(unittest.TestCase):
    """
    This class for testing weather forecast module
    """

    def test_weather_right_now_functionality_with_str(self):
        url = "http://api.openweathermap.org/data/2.5/weather"

        querystring = {"q": 'Moscow',
                        "appid": 'd5899e7650c659bd4cec287600d52a58'
                    }
        response = requests.get(url, params=querystring)
        result = response.json()
        self.assertDictEqual(result, weather.weather_right_now('Moscow', 'd5899e7650c659bd4cec287600d52a58'))

    def test_weather_right_now_with_with_dict(self):
        url = "http://api.openweathermap.org/data/2.5/weather"

        querystring = {"lat": '35',
                       'lon': '25',
                       "appid": 'd5899e7650c659bd4cec287600d52a58'
                       }
        response = requests.get(url, params=querystring)
        result = response.json()
        self.assertDictEqual(result, weather.weather_right_now({'coordinates': {'lat': "35", 'lon': '25'}},
                                                               'd5899e7650c659bd4cec287600d52a58'))

    def test_weather_right_now_with_keyerror(self):
        with self.assertRaises(ValueError) as raised_exception:
            weather.weather_right_now({'coordinates': {'lart': "35", 'lon': '25'}},
                                      'd5899e7650c659bd4cec287600d52a58')
        self.assertEqual(raised_exception.exception.args[0], "Invalid coordinates {'lart': '35', 'lon': '25'}")

    def test_weather_right_now_with_invalid_location(self):
        with self.assertRaises(TypeError) as raised_exception:
            weather.weather_right_now(123,
                                      'd5899e7650c659bd4cec287600d52a58')
        self.assertEqual(raised_exception.exception.args[0], "Invalid location: 123")

    def test_weather_right_now_with_cod_401(self):
        with self.assertRaises(requests.RequestException) as raised_exception:
            weather.weather_right_now({'coordinates': {'lat': "35", 'lon': '25'}},
                                      'd5899e7650cbd4cec287600d52a58')
        self.assertEqual(raised_exception.exception.args[0], "There is a little problem Invalid API key."
                                                             " Please see http://openweathermap.org/"
                                                             "faq#error401 for more info.")

    def test_weather_5_days_functionality_with_str(self):
        url = "http://api.openweathermap.org/data/2.5/forecast"

        querystring = {"q": 'Moscow',
                        "appid": 'd5899e7650c659bd4cec287600d52a58'
                    }
        response = requests.get(url, params=querystring)
        result = response.json()
        self.assertDictEqual(result, weather.weather_forecast_5_days('Moscow', 'd5899e7650c659bd4cec287600d52a58'))

    def test_weather_5_days_with_dict(self):
        url = "http://api.openweathermap.org/data/2.5/forecast"

        querystring = {"lat": '35',
                       'lon': '25',
                       "appid": 'd5899e7650c659bd4cec287600d52a58'
                       }
        response = requests.get(url, params=querystring)
        result = response.json()
        self.assertDictEqual(result, weather.weather_forecast_5_days({'coordinates': {'lat': "35", 'lon': '25'}},
                                                                     'd5899e7650c659bd4cec287600d52a58'))

    def test_weather_5_days_with_keyerror(self):
        with self.assertRaises(ValueError) as raised_exception:
            weather.weather_forecast_5_days({'coordinates': {'lart': "35", 'lon': '25'}},
                                            'd5899e7650c659bd4cec287600d52a58')
        self.assertEqual(raised_exception.exception.args[0], "Invalid coordinates {'lart': '35', 'lon': '25'}")

    def test_weather_5_days_with_invalid_location(self):
        with self.assertRaises(TypeError) as raised_exception:
            weather.weather_forecast_5_days(123,
                                            'd5899e7650c659bd4cec287600d52a58')
        self.assertEqual(raised_exception.exception.args[0], "Invalid location: 123")

    def test_weather_5_days_with_cod_401(self):
        with self.assertRaises(requests.RequestException) as raised_exception:
            weather.weather_forecast_5_days({'coordinates': {'lat': "35", 'lon': '25'}},
                                            'd5899e7650cbd4cec287600d52a58')
        self.assertEqual(raised_exception.exception.args[0], "There is a little problem Invalid API key."
                                                             " Please see http://openweathermap.org/"
                                                             "faq#error401 for more info.")

    def test_printer_right_now(self):
        data = {
            "coord": {
                "lon": 139.32,
                "lat": 59.92
            },
            "weather": [
                {
                    "id": 804,
                    "main": "Clouds",
                    "description": "overcast clouds",
                    "icon": "04d"
                }
            ],
            "base": "stations",
            "main": {
                "temp": 279.678,
                "pressure": 928.39,
                "humidity": 43,
                "temp_min": 279.678,
                "temp_max": 279.678,
                "sea_level": 1019.51,
                "grnd_level": 928.39
            },
            "wind": {
                "speed": 3.72,
                "deg": 147.001
            },
            "clouds": {
                "all": 88
            },
            "dt": 1526284282,
            "sys": {
                "message": 0.0047,
                "country": "RU",
                "sunrise": 1526234905,
                "sunset": 1526296283
            },
            "id": 2016305,
            "name": "Solnechnyy",
            "cod": 200
        }
        with patch('sys.stdout', new=StringIO()) as fake_out:
            weather.printer_right_now_weather(data)
            self.assertEqual(fake_out.getvalue().strip(), '-----------------------\n'
                                                          'Right now at Solnechnyy is overcast clouds\n'
                                                          '-----------------------\n'
                                                          'Temperature is 6.528\n'
                                                          'Humidity is 43 %\n'
                                                          'Pressure is 696.293 in Millimeter of mercury\n'
                                                          '-----------------------')

    def test_printer_forecast_5_days(self):
        data = {
                "cod": "200",
                "message": 0.0029,
                "cnt": 40,
                "list": [
                        {
                         "dt": 1526299200,
                         "main": {
                                  "temp": 276.95,
                                  "temp_min": 276.95,
                                  "temp_max": 276.95,
                                  "pressure": 928.99,
                                  "sea_level": 1020.94,
                                  "grnd_level": 928.99,
                                  "humidity": 59,
                                  "temp_kf": 0
                         },
                         "weather": [
                          {
                                  "id": 500,
                                  "main": "Rain",
                                  "description": "light rain",
                                  "icon": "10n"
                          }
                          ],
                "clouds": {
                          "all": 92
                          },
                "wind": {
                          "speed": 3.81,
                          "deg": 148
                         },
                "rain": {
                          "3h": 0.0775
                        },
                "sys": {
                           "pod": "n"
                       },
                "dt_txt": "2018-05-14 12:00:00"
                        },
                        {
             "dt": 1526310000,
            "main": {
                "temp": 274.97,
                "temp_min": 274.97,
                "temp_max": 274.974,
                "pressure": 929.09,
                "sea_level": 1021.31,
                "grnd_level": 929.09,
                "humidity": 60,
                "temp_kf": 0
            },
            "weather": [
                {
                    "id": 500,
                    "main": "Rain",
                    "description": "light rain",
                    "icon": "10n"
                }
            ],
            "clouds": {
                "all": 92
            },
            "wind": {
                "speed": 3.62,
                "deg": 139.001
            },
            "rain": {
                "3h": 0.0025
            },
            "snow": {
                "3h": 0.002
            },
            "sys": {
                "pod": "n"
            },
            "dt_txt": "2018-05-14 15:00:00"
        }],
            "city": {
        "id": 2016305,
        "name": "Solnechnyy",
        "coord": {
            "lat": 60.4167,
            "lon": 137.5
        },
        "country": "RU",
        "population": 1230
    }
}
        with patch('sys.stdout', new=StringIO()) as fake_out:
            weather.printer_weather_forecast(data)
            self.assertEqual(fake_out.getvalue().strip(), '-----------------------\n'
                                                          'Weather on 2018-05-14 12:00:00 at Solnechnyy is light rain\n'
                                                          '-----------------------\n'
                                                          'Temperature is 3.8\n'
                                                          'Humidity is 59 %\n'
                                                          'Pressure is 696.742 in Millimeter of mercury\n'
                                                          '-----------------------\n'
                                                          '-----------------------\n'
                                                          'Weather on 2018-05-14 15:00:00 at Solnechnyy is light rain\n'
                                                          '-----------------------\n'
                                                          'Temperature is 1.82\n'
                                                          'Humidity is 60 %\n'
                                                          'Pressure is 696.817 in Millimeter of mercury\n'
                                                          '-----------------------')















