import os
from pprint import pprint
import requests
import logging
logger = logging.getLogger(__name__)

class Weather:
    def get_weather_by_city(self, cityname=None):
        logger.debug(f"get_weather_by_city called with params: {cityname}")

        try:
            WEATHER_URI_CITY = "http://127.0.0.1:5000/weather/city"
            response = requests.get(WEATHER_URI_CITY, params={"q": cityname})
            return response.json()
        except Exception as error:
            logger.error(f"get_weather_by_city called with error : {error}")


    def get_weather_by_latlon(self, lat=None, lon=None):
        logger.debug(f"get_weather_by_latlon called with params: {lat}, {lon}")
        try:
            WEATHER_URI_LATLON = "http://127.0.0.1:5000/weather/latlon"
            response = requests.get(WEATHER_URI_LATLON, params={"q": f"{lat},{lon}"})
            return response.json()
        except Exception as error:
            logger.error(f"get_weather_by_latlon called with error : {error}")




if __name__ == "__main__":
    obj = Weather()
    obj.get_weather_by_city(cityname="new york")
