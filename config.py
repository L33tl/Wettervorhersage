# app size
HEIGHT = 576
WIDTH = 1024

# api server
WEATHER_SERVER = 'openweathermap.org'

# constants
HPA_MMHG = 0.750064
K_C = -273.15

# strings
city_not_found_string = 'Город не найден'
enter_city_name = 'Введите название города'
changing_city_without_internet_string = 'Нет интернета'
degree = '°'

# tables and dbs names and special columns
table_today_name = 'today'
table_days_name = 'days'
DB_NAME_DAYS = 'weather_days_db.sqlite3'
DB_NAME_TODAY = 'weather_today_db.sqlite3'
NESTED_KEYS = ('wind', 'pressure', 'temperature')
DEL_COLS = ('rain', 'snow')

# paths
circle_path = 'sources/circle.png'
noimage_path = 'sources/noimage.png'

# ru weather keys
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
