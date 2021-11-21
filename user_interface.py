import os
import shutil
import sys
import urllib.request
from datetime import datetime

import pyowm.weatherapi25.weather
from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QLabel, QDialog
    )

from change_city_UI import Ui_Dialog
from config import WIDTH, HEIGHT, weather_keys, degree, K_C
from main_window_ui import Ui_MainWindow
from weather import WeatherParser

stylesheet = open('style.css', 'r').read()


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # uic.loadUi('main_window_ui.ui', self)
        self.setupUi(self)
        self.initUI()

        self.weather = WeatherParser()
        self.tabs = ['today', 'days', 'hours']
        self.current_tab_index = 0

        self.load_widget(0)

    # noinspection PyAttributeOutsideInit,PyPep8Naming
    def initUI(self):
        self.change_city_dialog = ChangeCityDialog(self)
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
        self.change_city_dialog.show()

    def load_widget_today(self):
        try:
            weather: pyowm.weatherapi25.weather.Weather = self.get_weather().weather

            self.statusEdit_label.setText(weather.detailed_status.title())
            self.statusEdit_label.setGeometry(
                QRect((WIDTH - self.statusEdit_label.sizeHint().width()) // 2,
                      HEIGHT // 2,
                      self.statusEdit_label.sizeHint().width(),
                      self.statusEdit_label.sizeHint().height()))

            pixmap = QPixmap('sources/circle.png')

            # self.temperatureEdit_label.setText(str(weather.temperature('celsius').get('temp')))
            # self.feelsLikeEdit_label.setText(str(weather.temperature('celsius').get('feels_like')))
            self.temperatureEdit_label.setPixmap(pixmap)
            self.feelsLikeEdit_label.setPixmap(pixmap)

            # self.tempText_label.setText(str(weather.temperature('celsius').get('temp')))
            # self.feelsText_label.setText(str(weather.temperature('celsius').get('feels_like')))

            self.set_label(self.tempText_label,
                           str(round(weather.temperature('celsius').get('temp'), 1)) + degree)
            self.set_label(self.feelsText_label,
                           str(round(weather.temperature('celsius').get('feels_like'), 1)) + degree)

            timezone = datetime.now() - datetime.utcnow()

            time = weather.sunrise_time('date') + timezone
            self.set_label(self.sunriseEdit_label,
                           f'{time.hour:02d}:{time.minute:02d}:{time.second:02d}')

            time = weather.sunset_time('date') + timezone
            self.set_label(self.sunsetEdit_label,
                           f'{time.hour:02d}:{time.minute:02d}:{time.second:02d}')

            self.humidityEdit_label.setText(f'{weather.humidity}%')
            if weather.precipitation_probability is not None:
                self.precipitationProbabilityEdit_label.setText(
                    f'{weather.precipitation_probability}%')

                self.precipitationProbability_label.show()
            else:
                self.precipitationProbability_label.hide()

            if weather.humidex is not None:
                self.set_label(self.humidexEdit_label, weather.humidex)
                self.humidex_label.show()
            else:
                self.humidex_label.hide()

            pressure = self.weather.hPa_to_mmHg(weather.barometric_pressure().get('press'))
            self.pressureEdit_label.setText(str(round(pressure, 2)))

            self.download_img(weather)
            pixmap = QPixmap(f'images/{weather.weather_icon_name}.png')
            self.status_img.setPixmap(pixmap)
            self.status_img.resize(self.status_img.sizeHint().width(),
                                   self.status_img.sizeHint().height())

            self.set_day_info(self.temp_info)

        except Exception as e:
            print(e)

    def load_widget_days(self):
        try:
            weather = self.get_weather()[:3]
            days = [[self.img_1, self.status_1, self.info_1, self.sunsettime_1, self.sunrisetime_1,
                     self.date_1],
                    [self.img_2, self.status_2, self.info_2, self.sunsettime_2, self.sunrisetime_2,
                     self.date_2],
                    [self.img_3, self.status_3, self.info_3, self.sunsettime_3, self.sunrisetime_3,
                     self.date_3]]
            images = [self.download_img(w) for w in weather]

            for day in days:
                while not day[2].isEmpty():
                    day[2].removeRow(0)

            for i, day in enumerate(days):

                day[5].setText(
                    f'{weather[i].sunrise_time("date").day}.{weather[i].sunrise_time("date").month}')

                day_weather = weather[i]
                pixmap = QPixmap(f'images/{images[i]}.png')
                day[0].setPixmap(pixmap)

                status = day[1]
                status.setText(day_weather.detailed_status)
                status.setStyleSheet('QLabel{font: 14pt "Arial"}')
                status.resize(status.sizeHint().width(), status.sizeHint().height())

                timezone = datetime.now() - datetime.utcnow()

                time = day_weather.sunrise_time('date') + timezone
                day[4].setText(f'{time.hour:02d}:{time.minute:02d}:{time.second:02d}')
                time = day_weather.sunset_time('date') + timezone
                day[3].setText(f'{time.hour:02d}:{time.minute:02d}:{time.second:02d}')

                dict_weather = day_weather.to_dict()
                for en_key, ru_key in weather_keys.items():
                    value = dict_weather[en_key]
                    if value is not None:
                        if isinstance(ru_key, str):
                            if en_key == 'precipitation_probability':
                                value = f'{int(value * 100)}%'
                            elif en_key == 'humidity':
                                value = f'{int(value)}%'
                            elif en_key == 'pressure':
                                pressure = self.weather.hPa_to_mmHg(
                                    day_weather.barometric_pressure().get('press'))
                                value = round(pressure, 2)
                            # elif en_key == 'temperature':
                            #     value = str(
                            #         round(day_weather.temperature('celsius').get('day'), 1)) + degree
                            # elif en_key == 'feels_like':
                            #     print(day_weather.temperature('celsius'))
                            #     value = str(round(
                            #         day_weather.temperature('celsius').get('feels_like_day'),
                            #         1)) + degree

                            row = (QLabel(ru_key), QLabel(str(value)))
                            row[0].setStyleSheet("QLabel{font-size: 12pt;}")
                            row[1].setStyleSheet("QLabel{font-size: 12pt;}")
                            self.set_row(row, day[2])
                        else:
                            inner_weather = value
                            value = ru_key[0]
                            row = (QLabel(value), QLabel(''))
                            row[0].setStyleSheet("QLabel{font-size: 12pt;}")
                            row[1].setStyleSheet("QLabel{font-size: 12pt;}")
                            self.set_row(row, day[2])

                            print(inner_weather)
                            for inner_en_key, inner_ru_key in weather_keys[en_key][1].items():
                                if en_key == 'temperature':
                                    value = round(inner_weather.get(inner_en_key) + K_C, 1)
                                elif en_key == 'wind':
                                    value = str(inner_weather.get(inner_en_key))
                                    if inner_en_key == 'deg':
                                        value += degree
                                    elif inner_en_key == 'speed':
                                        value += ' м/c'
                                    elif inner_en_key == 'gust':
                                        value += ' м/с'

                                row = QLabel(' ' * 5 + inner_ru_key), QLabel(str(value))
                                row[0].setStyleSheet("QLabel{font-size: 12pt;}")
                                row[1].setStyleSheet("QLabel{font-size: 12pt;}")
                                self.set_row(row, day[2])
        except Exception as e:
            print(e)

    def load_widget_hours(self):
        weather = self.get_weather()

    def set_day_info(self, label):
        date = datetime.today()
        city = self.weather.get_city()
        if city == 'Yekaterinburg':
            city = 'екатеринбург'
        self.set_label(label, f'Погода в г. {city.title()} на {date.day}.{date.month}')

    def set_label(self, label, text=None):
        if text is not None:
            label.setText(str(text))
        label.setGeometry(label.x(), label.y(), label.sizeHint().width(), label.sizeHint().height())

    def set_row(self, row, day):
        row[0].setAlignment(Qt.AlignRight)
        row[1].setAlignment(Qt.AlignRight)
        day.addRow(*row)

    def get_weather(self):
        return self.weather.weather(self.tabs[self.current_tab_index])

    def download_img(self, weather):
        res = urllib.request.urlopen(self.get_weather_ico(weather))
        out = open(f'images/{weather.weather_icon_name}.png', 'wb')
        out.write(res.read())
        out.close()
        return weather.weather_icon_name

    def get_weather_ico(self, weather):
        return weather.weather_icon_url("2x")

    def closeEvent(self, event):
        shutil.rmtree('images')
        os.mkdir('images')


class ChangeCityDialog(QDialog, Ui_Dialog):
    def __init__(self, first_form: MainWindow):
        super().__init__()
        self.setupUi(self)
        self.ok_btn.clicked.connect(self.ok)
        self.cancel_btn.clicked.connect(self.cancel)
        self.not_found_error_label.setText('')
        self.first_form = first_form

    def ok(self):
        city = self.city_edit.text().strip()
        if not city or not city.isalpha():
            return self.not_found_error_label.setText('Введите название города')
        answer = self.first_form.weather.change_city(city)
        if answer:
            self.first_form.load_widget(self.first_form.current_tab_index)
            self.close()
        else:
            self.not_found_error_label.setText('Город не найден')

    def cancel(self):
        self.city_edit.setText('')
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(stylesheet)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())
