import sqlite3


class DBWorker:
    def __init__(self):
        self.db_name = 'weather_db.sqlite3'
        self.connect = sqlite3.connect(self.db_name)

    def weather_today(self):
        pass

    def weather_daily(self):
        pass

    def weather_hourly(self):
        pass
