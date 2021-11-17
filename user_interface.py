from datetime import datetime
import sys

import pyowm.weatherapi25.weather
from PyQt5 import uic
from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel

from config import WIDTH, WEATHER_SERVER
from main_window_ui import Ui_MainWindow
from weather import WeatherParser


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # uic.loadUi('main_window_ui.ui', self)
        self.setupUi(self)
        self.initUI()

        self.tabs = ['today', 'days', 'hours']
        self.current_tab_index = 0
        self.load_widget(0)

    # noinspection PyAttributeOutsideInit,PyPep8Naming
    def initUI(self):
        self.change_city_form = ChangeCityForm(self)
        self.change_city_btn.triggered.connect(self.change_city)
        self.tabWidget.tabBarClicked.connect(self.load_widget)

    def load_widget(self, index):
        self.current_tab_index = index
        if not index:
            return self.load_widget_today()
        if index == 1:
            return self.load_widget_days()
        return self.load_widget_hours()

    def change_city(self):
        self.change_city_form.show()

    def load_widget_today(self):
        try:
            weather: pyowm.weatherapi25.weather.Weather = self.get_weather().weather

            self.statusEdit_label.setText(weather.detailed_status.title())
            self.statusEdit_label.setGeometry(
                QRect((WIDTH - self.statusEdit_label.width()) // 2,
                      self.statusEdit_label.y(), self.statusEdit_label.sizeHint().width(),
                      self.statusEdit_label.sizeHint().height()))

            self.set_label(self.temperatureEdit_label,
                           str(weather.temperature('celsius').get('temp')))
            self.set_label(self.feelsLikeEdit_Label,
                           str(weather.temperature('celsius').get('feels_like')))

            timezone = datetime.now() - datetime.utcnow()

            time = weather.sunrise_time('date') + timezone
            self.set_label(self.sunriseEdit_label,
                           f'{time.hour:02d}:{time.minute:02d}:{time.second:02d}')

            time = weather.sunset_time('date') + timezone
            self.set_label(self.sunsetEdit_label,
                           f'{time.hour:02d}:{time.minute:02d}:{time.second:02d}')

            print(self.get_weather_ico(weather.weather_icon_name))

        except Exception as e:
            print(e)

    def get_weather_ico(self, ico_name):
        return f"{WEATHER_SERVER}/img/w/{ico_name}.png"

    def load_widget_days(self):
        weather = self.get_weather()

    def set_label(self, label, text=None):
        if text is not None:
            label.setText(text)
        label.setGeometry(label.x(), label.y(), label.sizeHint().width(), label.sizeHint().height())

    def load_widget_hours(self):
        weather = self.get_weather()

    def get_weather(self):
        weather = WeatherParser()
        return weather.weather(self.tabs[self.current_tab_index])


class ChangeCityForm(QWidget):
    def __init__(self, first_form: MainWindow):
        super().__init__()
        uic.loadUi('change_city_UI.ui', self)
        self.ok_btn.clicked.connect(self.ok)
        self.cancel_btn.clicked.connect(self.cancel)
        self.not_found_error_label.setText('')
        self.first_form = first_form

    def ok(self):
        city = self.city_edit.text().strip()
        if not city:
            return self.not_found_error_label.setText('Введите название города')
        answer = self.first_form.weather.change_city(city)
        if answer:
            self.close()
        else:
            self.not_found_error_label.setText('Город не найден')

    def cancel(self):
        self.city_edit.setText('')
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # app.setStyleSheet(stylesheet)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())
