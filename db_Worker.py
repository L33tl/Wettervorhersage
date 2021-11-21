import sqlite3
from config import NESTED_KEYS, DB_NAME, DEL_COLS


class DBWorker:
    def __init__(self):
        self.db_name = DB_NAME
        self.connect = sqlite3.connect(self.db_name)

    def weather_today(self):
        pass

    def weather_daily(self):
        cursor = self.connect.cursor()
        days = cursor.execute('''SELECT * from days''').fetchall()
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

    def weather_hourly(self):
        pass

    def write_weather_today(self, today):
        pass

    def write_weather_daily(self, days):
        cursor = self.connect.cursor()
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
                f'''insert into days ({', '.join(f"'{str(d)}'" for d in day.keys())}) VALUES
                 ({', '.join(f"'{str(d)}'" for d in day.values())});''')
        cursor.close()
        self.connect.commit()

    def write_weather_hourly(self, hours):
        pass
