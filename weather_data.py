# weather_data.py

import requests


class WeatherData:

    def __init__(self, api_key, city):

        self.api_key = api_key
        self.city = city

    def get_weather_data(self):

        url = (
            f"https://api.openweathermap.org/data/2.5/weather?"
            f"q={self.city}&appid={self.api_key}&units=metric"
        )

        response = requests.get(url)

        data = response.json()

        return data

    def get_temperature(self):

        data = self.get_weather_data()

        return data["main"]["temp"]

    def get_humidity(self):

        data = self.get_weather_data()

        return data["main"]["humidity"]

    def get_weather_condition(self):

        data = self.get_weather_data()

        return data["weather"][0]["main"]