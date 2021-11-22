import sqlite3

import pyowm.weatherapi25.weather

from config import (
    NESTED_KEYS, DB_NAME_DAYS, DEL_COLS, table_today_name, DB_NAME_TODAY,
    table_days_name
    )


class DBWorker:
    def __init__(self):
        self.connect_days = sqlite3.connect(DB_NAME_DAYS)
        self.connect_today = sqlite3.connect(DB_NAME_TODAY)

    def weather_today(self):
        cursor = self.connect_today.cursor()
        today = cursor.execute(f'''SELECT * FROM {table_today_name}''').fetchall()[0]
        columns_names = [col[0] for col in cursor.description]
        today = dict(zip(columns_names, today))

        for key, value in today.items():
            try:
                if 'time' in key:
                    today[key] = int(value)
                else:
                    today[key] = float(value)
            except ValueError:
                pass

        for table in NESTED_KEYS:
            data = cursor.execute(f'''SELECT * FROM {table}''').fetchall()[0]
            data_columns_names = [col[0] for col in cursor.description]
            data = list(data)
            for j in range(len(data)):
                try:
                    if data[j] is not None:
                        data[j] = float(data[j])
                except ValueError:
                    pass

            today[table] = dict(zip(data_columns_names, data))
        cursor.close()
        return today

    def weather_daily(self):
        cursor = self.connect_days.cursor()
        days = cursor.execute(f'''SELECT * from {table_days_name}''').fetchall()
        columns_names = [col[0] for col in cursor.description][1:]

        for i in range(len(days)):
            days[i] = dict(zip(columns_names, days[i][1:]))

            for k, v in days[i].items():
                try:
                    if 'time' in k:
                        days[i][k] = int(v)
                    else:
                        days[i][k] = float(v)
                except ValueError:
                    pass

            for table in NESTED_KEYS:
                data = cursor.execute(f'''SELECT * FROM {table} WHERE id={i + 1}''').fetchall()[0][
                       1:]
                data_columns_names = [col[0] for col in cursor.description][1:]

                data = list(data)
                for j in range(len(data)):
                    try:
                        data[j] = float(data[j])
                    except ValueError:
                        pass

                days[i][table] = dict(zip(data_columns_names, data))
        cursor.close()
        return days

    # def weather_hourly(self):
    #     pass

    def write_weather_today(self, today: pyowm.weatherapi25.weather.Weather):
        today = today.to_dict().get('weather')

        normal_keys = []
        dict_keys = []
        for today_key, today_value in today.items():
            if isinstance(today_value, dict):
                dict_keys.append(today_key)
            else:
                normal_keys.append(today_key)

        cursor = self.connect_today.cursor()

        cursor.execute(f'''DELETE FROM {table_today_name}''')
        for table in NESTED_KEYS:
            cursor.execute(f'''DELETE FROM {table}''')

            cursor.execute(
                f'''INSERT INTO {table} ({", ".join([f"'{str(key)}'" for key in today[table].keys()])
                }) VALUES ({', '.join([f"'{str(value)}'" for value in today[table].values()])})''')

        for del_col in DEL_COLS:
            today.pop(del_col)

        cursor.execute(
            f'''INSERT INTO {table_today_name} ({', '.join([key for key in normal_keys])}) 
            VALUES ({', '.join([f"'{str(value)}'"
                                for value in today.values() if not isinstance(value, dict)])})''')

        cursor.close()
        self.connect_today.commit()

    def write_weather_daily(self, days):
        cursor = self.connect_days.cursor()
        cursor.execute('''DELETE from days''')
        for _ in days:
            for k in NESTED_KEYS:
                cursor.execute(f'''DELETE from {k}''')
        for day in days:
            day = day.to_dict()
            for k in NESTED_KEYS:
                cursor.execute(
                    f'''INSERT INTO {k} ({', '.join([f"'{str(kd)}'" for kd in day[k].keys()])}) 
                        VALUES ({', '.join([f"'{str(v)}'" for v in day[k].values()])});''')
                day.pop(k)

            for del_col in DEL_COLS:
                day.pop(del_col)

            cursor.execute(
                f'''insert into {table_days_name} ({', '.join(f"'{str(d)}'" for d in day.keys())}) 
                    VALUES ({', '.join(f"'{str(d)}'" for d in day.values())});''')
        cursor.close()
        self.connect_days.commit()

    # def write_weather_hourly(self, hours):
    #     pass
