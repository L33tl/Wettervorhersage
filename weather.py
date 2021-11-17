import pyowm.weatherapi25.observation
from pyowm import OWM
import geocoder
from pyowm.commons.exceptions import NotFoundError
from pyowm.weatherapi25.weather import Weather

from config import WEATHER_SERVER
from sconfig import API_key
from pyowm.utils.config import get_default_config
from db_Worker import DBWorker

import socket


class WeatherParser:
    def __init__(self):
        try:
            self.weather_server = WEATHER_SERVER
            config_dict = get_default_config()
            config_dict['language'] = 'ru'
            self.owm = OWM(API_key, config_dict)
            self.weather_mgr = self.owm.weather_manager()
            self.city = geocoder.ip('me')
        except ConnectionError as ce:
            self.has_connected = False
            print(ce)
        else:
            self.has_connected = True
            # print('Has connection')
        finally:
            self.db_worker = DBWorker()

    # def has_connected(self) -> bool:
    #     return bool(socket.create_connection((self.weather_server, 80)))

    # def weather_by_days(self, city: str) -> pyowm.weatherapi25.one_call.OneCall:
    #     loc = geocoder.location(city)
    #     return self.weather_mgr.one_call(lat=loc.latitude, lon=loc.longitude)

    def weather(self, forecast_type):
        if forecast_type == 'today':
            return self.weather_today()
        elif forecast_type == 'days':
            return self.weather_daily()
        else:
            return self.weather_hourly()

    def weather_today(self):
        if self.has_connected:
            return self.weather_mgr.weather_at_place(self.city.city)
        else:
            return self.db_worker.weather_today()

    def weather_daily(self):
        if self.has_connected:
            loc = geocoder.location(self.city)
            return self.weather_mgr.one_call(lat=loc.latitude, lon=loc.longitude).forecast_daily
        else:
            return self.db_worker.weather_daily()

    def weather_hourly(self):
        if self.has_connected:
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
    w = WeatherParser()
    print(w.weather('today').to_dict()['weather'].keys())
    print(w.weather('today').to_dict()['weather']['precipitation_probability'])
    print()
    print(w.weather('today').to_dict()['weather']['temperature'].keys())
