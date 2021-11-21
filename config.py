HEIGHT = 576
WIDTH = 1024
WEATHER_SERVER = 'openweathermap.org'
NESTED_KEYS = ('wind', 'pressure', 'temperature')
DB_NAME = 'weather_db.sqlite3'
DEL_COLS = ('rain', 'snow')
degree = '°'

weather_keys = {
    'temperature':               ('температура', {
        'day': f't, C{degree}', 'feels_like_day': 'по ощущению', 'morn': 'утром', 'night': 'ночью'
        }),
    'pressure':                  'давление',
    'wind':                      ('ветер', {
        'deg': 'направление', 'speed': 'скорость', 'gust': 'порывы'
        }),
    'humidity':                  'влажность',
    'precipitation_probability': 'вероятность осадков',
    }

HPA_MMHG = 0.750064
K_C = -273.15

city_not_found_string = 'Город не найден'
enter_city_name = 'Введите название города'
