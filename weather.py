import pyowm.weatherapi25.observation
from pyowm import OWM
import geocoder
from pyowm.commons.exceptions import NotFoundError
from pyowm.weatherapi25.weather import Weather

from config import API_key
from pyowm.utils.config import get_default_config
from db_Worker import DBWorker

import socket


class WeatherWorker:
    def __init__(self):
        self.weather_server = 'openweathermap.org'
        if not self.has_connected():
            raise ConnectionError

        config_dict = get_default_config()
        config_dict['language'] = 'ru'
        self.owm = OWM(API_key, config_dict)
        self.weather_mgr = self.owm.weather_manager()
        self.city = geocoder.ip('me')
        self.db_worker = DBWorker()

    def has_connected(self) -> bool:
        return bool(socket.create_connection((self.weather_server, 80)))

    # def weather_by_days(self, city: str) -> pyowm.weatherapi25.one_call.OneCall:
    #     loc = geocoder.location(city)
    #     return self.weather_mgr.one_call(lat=loc.latitude, lon=loc.longitude)

    # def get_weather_icon(self) -> str:
    #     return f"{self.weather_server}/img/w/{wt['weather']['weather_icon_name']}.png"

    def weather(self, forecast_type, has_connection):
        if forecast_type == 'today':
            self.weather_today(has_connection)
        elif forecast_type == 'days':
            self.weather_daily(has_connection)
        else:
            self.weather_hourly(has_connection)

    def weather_today(self, has_connection):
        if has_connection:
            return self.weather_mgr.weather_at_place(self.city.city)
        else:
            return self.db_worker.weather_today()

    def weather_daily(self, has_connection):
        if has_connection:
            loc = geocoder.location(self.city)
            return self.weather_mgr.one_call(lat=loc.latitude, lon=loc.longitude).forecast_daily
        else:
            return self.db_worker.weather_daily()

    def weather_hourly(self, has_connection):
        if has_connection:
            loc = geocoder.location(self.city.latlng)
            return self.weather_mgr.one_call(lat=loc.latitude, lon=loc.longitude).forecast_hourly
        else:
            return self.db_worker.weather_hourly()

    def check_city(self, city):
        try:
            self.weather_mgr.weather_at_place(city)
            return True
        except NotFoundError:
            return False

    def change_city(self, city):
        if self.check_city(city):
            self.city = city
            return True
        return False


if __name__ == '__main__':
    w = WeatherWorker()
