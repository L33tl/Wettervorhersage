import sqlite3
from config import NESTED_KEYS, DB_NAME


class DBWorker:
    def __init__(self):
        self.db_name = DB_NAME
        self.connect = sqlite3.connect(self.db_name)

    def weather_today(self):
        pass

    def weather_daily(self):
        cursor = self.connect.cursor()
        days = cursor.execute('''SELECT * from days''').fetchall()
        columns_names = [col[0] for col in cursor.description[:-1]]

        for i in range(len(days)):
            days[i] = dict(zip(columns_names, days[i]))

        cursor.close()
        return days

    def weather_hourly(self):
        pass

    def write_weather_today(self, today):
        pass

    def write_weather_daily(self, days):
        cursor = self.connect.cursor()
        cursor.execute('''DELETE from days''')
        for day in days:
            for k in NESTED_KEYS:
                cursor.execute(f'''DELETE from {k}''')
        for day in days:
            day = day.to_dict()
            for k in NESTED_KEYS:
                if not day[k]:
                    day[k] = {'no_data': 1}
                cursor.execute(
                    f'''INSERT INTO {k} ({', '.join([f"'{str(kd)}'" for kd in day[k].keys()])}) VALUES
                     ({', '.join([f"'{str(v)}'" for v in day[k].values()])});''')
                day.pop(k)

            cursor.execute(
                f'''insert into days ({', '.join(f"'{str(d)}'" for d in day.keys())}) VALUES
                 ({', '.join(f"'{str(d)}'" for d in day.values())});''')
        cursor.close()
        self.connect.commit()

    def write_weather_hourly(self, hours):
        pass


if __name__ == '__main__':
    db = DBWorker()
