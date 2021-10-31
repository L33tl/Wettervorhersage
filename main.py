import pprint

from pyowm import OWM
from pyowm.utils import config, timestamps
from config import API_key
from pyowm.utils.config import get_config_from

from pyowm.owm import OWM
from config import API_key

owm = OWM(API_key)
mgr = owm.weather_manager()

# daily_forecast = mgr.forecast_at_place('Berlin,DE', 'daily').forecast
# three_h_forecast = mgr.forecast_at_place('Berlin,DE', '3h').forecast
#

# вместо строк, начиная с daily_forecaster
reg = owm.city_id_registry()
loc = reg.locations_for(city_name='Yekaterinburg')

one_call = mgr.one_call(loc[0].lat, loc[0].lon)
forecast = one_call.forecast_daily
# получаем список из прогнозов на каждый последующий день
