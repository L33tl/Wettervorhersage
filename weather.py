from pyowm import OWM
from config import API_key
from pyowm.utils.config import get_default_config


class Weather:
    def __init__(self):
        config_dict = get_default_config()
        config_dict['language'] = 'ru'
        self.owm = OWM(API_key, config_dict)
        self.mgr = self.owm.weather_manager()

    def one_call_at_coords(self, lat, lon):
        return self.mgr.one_call()

    def coords_from_place_name(self, place_name):
        reg = self.owm.city_id_registry()
        list_of_locations = reg.locations_for(place_name)
        return list_of_locations


if __name__ == '__main__':
    w = Weather()
    print(w.owm.city_id_registry().locations_for('Москва'))
