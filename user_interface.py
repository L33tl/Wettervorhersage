import sys

import geocoder
from PyQt5 import uic
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QAction, qApp
from main_window_ui import Ui_MainWindow
from weather import WeatherWorker


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.change_city_form = ChangeCityForm(self)
        uic.loadUi('main_window_ui.ui', self)
        # self.setupUi(self)
        self.buttons_group = {
            'today': self.Btn_today, 'days': self.Btn_byDays, 'hours': self.Btn_byHours
            }
        for btn in self.buttons_group.values():
            btn.clicked.connect(self.group_button_click)
        # self.change_city_btn.clicked.connect(self.change_city)

        self.change_city_btn.triggered.connect(self.change_city)
        self.weather = WeatherWorker()

    def change_city(self):
        self.change_city_form.show()

    def group_button_click(self):
        if self.buttons_group['today'] == self.sender():
            self.__move_to_layout(self.widget_today)
        elif self.buttons_group['days'] == self.sender():
            self.__move_to_layout(self.widget_days)
        elif self.buttons_group['hours'] == self.sender():
            self.__move_to_layout(self.widget_hours)

    def __move_to_layout(self, to_layout: QWidget):
        self.widget_today.hide()
        self.widget_days.hide()
        self.widget_hours.hide()
        # self.update_layout(to_layout)
        to_layout.show()

    def load_layout_today(self, layout):
        pass

    def load_layout_by_days(self, layout):
        pass

    def load_layout_by_hours(self, layout):
        pass

    def get_weather(self):
        has_connection = self.weather.has_connected()
        if self.today_layout.isEnabled():
            self.weather.weather('today', has_connection)
        elif self.days_layout.isEnabled():
            self.weather.weather('days', has_connection)
        else:
            self.weather.weather('hours', has_connection)


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
        answer = WeatherWorker.change_city(self.first_form.weather, city)
        if answer:
            self.close()
        else:
            self.not_found_error_label.setText('Город не найден')

    def cancel(self):
        self.city_edit.setText('')
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())
