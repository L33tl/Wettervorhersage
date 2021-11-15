import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget

from main_window_ui import Ui_MainWindow
from weather import WeatherWorker


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # uic.loadUi('main_window_ui.ui', self)
        self.setupUi(self)
        self.initUI()

        # self.load_widget_today()

    # noinspection PyAttributeOutsideInit,PyPep8Naming
    def initUI(self):
        self.change_city_form = ChangeCityForm(self)
        self.Btn_today.clicked.connect(self.load_widget_today)
        self.Btn_byDays.clicked.connect(self.load_widget_days)
        self.Btn_byHours.clicked.connect(self.load_widget_hours)
        self.change_city_btn.triggered.connect(self.change_city)

        self.weather = WeatherWorker()
        # self.current_widget = self.widget_today

        print(self.tabWidget.currentWidget())

    def change_city(self):
        self.change_city_form.show()

    def change_widget(self, to_widget):
        self.current_widget.hide()
        # noinspection PyAttributeOutsideInit
        self.current_widget = to_widget
        exec(f'self.load_widget_{to_widget.objectName().split("_")[1]}')

    def load_widget_today(self):
        self.change_widget(self.widget_today)
        weather = self.get_weather()

    def load_widget_days(self):
        self.change_widget(self.widget_days)
        weather = self.get_weather()

    def load_widget_hours(self):
        self.change_widget(self.widget_hours)
        weather = self.get_weather()

    def get_weather(self):
        return self.weather.weather(self.current_widget.objectName().split('_')[1])


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
    ex = MainWindow()
    ex.show()

    sys.exit(app.exec())
