HEIGHT = 576
WIDTH = 1024
WEATHER_SERVER = 'openweathermap.org'
NESTED_KEYS = ('wind', 'pressure', 'temperature')
DB_NAME_DAYS = 'weather_days_db.sqlite3'
DB_NAME_TODAY = 'weather_today_db.sqlite3'
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
noimage = 'noimage'

city_not_found_string = 'Город не найден'
enter_city_name = 'Введите название города'

table_today_name = 'today'
table_days_name = 'days'
