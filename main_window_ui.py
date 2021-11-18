# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 617)
        MainWindow.setMinimumSize(QtCore.QSize(1024, 617))
        MainWindow.setMaximumSize(QtCore.QSize(1024, 617))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(1024, 576))
        self.centralwidget.setMaximumSize(QtCore.QSize(1024, 576))
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1024, 576))
        self.tabWidget.setStyleSheet("QTabWidget::tab-bar {\n"
"\n"
"\n"
" }\n"
"\n"
"\n"
"\n"
" QTabBar::tab {\n"
"  width:321px;\n"
"  background: gray;\n"
"  color: back;\n"
"  padding: 10px;\n"
"    font: 75 italic 12pt \"Arial\";\n"
" }\n"
"\n"
"\n"
"\n"
" QTabBar::tab:selected {\n"
"  background: lightgray;\n"
" }")
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_today = QtWidgets.QWidget()
        self.tab_today.setObjectName("tab_today")
        self.sunrise_label = QtWidgets.QLabel(self.tab_today)
        self.sunrise_label.setGeometry(QtCore.QRect(50, 90, 85, 27))
        self.sunrise_label.setTextFormat(QtCore.Qt.AutoText)
        self.sunrise_label.setObjectName("sunrise_label")
        self.sunset_label = QtWidgets.QLabel(self.tab_today)
        self.sunset_label.setGeometry(QtCore.QRect(65, 140, 70, 27))
        self.sunset_label.setObjectName("sunset_label")
        self.humidity_label = QtWidgets.QLabel(self.tab_today)
        self.humidity_label.setGeometry(QtCore.QRect(23, 410, 128, 27))
        self.humidity_label.setStyleSheet("")
        self.humidity_label.setObjectName("humidity_label")
        self.precipitationProbability_label = QtWidgets.QLabel(self.tab_today)
        self.precipitationProbability_label.setGeometry(QtCore.QRect(23, 480, 245, 27))
        self.precipitationProbability_label.setObjectName("precipitationProbability_label")
        self.feelsLikeEdit_label = QtWidgets.QLabel(self.tab_today)
        self.feelsLikeEdit_label.setGeometry(QtCore.QRect(610, 70, 151, 151))
        self.feelsLikeEdit_label.setMouseTracking(False)
        self.feelsLikeEdit_label.setStyleSheet("")
        self.feelsLikeEdit_label.setText("")
        self.feelsLikeEdit_label.setObjectName("feelsLikeEdit_label")
        self.feelsLike_label = QtWidgets.QLabel(self.tab_today)
        self.feelsLike_label.setGeometry(QtCore.QRect(630, 240, 122, 22))
        self.feelsLike_label.setStyleSheet("font: 75 14pt \"Arial\";")
        self.feelsLike_label.setObjectName("feelsLike_label")
        self.temperature_label = QtWidgets.QLabel(self.tab_today)
        self.temperature_label.setGeometry(QtCore.QRect(350, 240, 29, 22))
        self.temperature_label.setStyleSheet("font: 75 14pt \"Arial\";")
        self.temperature_label.setObjectName("temperature_label")
        self.humidex_label = QtWidgets.QLabel(self.tab_today)
        self.humidex_label.setGeometry(QtCore.QRect(930, 410, 101, 27))
        self.humidex_label.setObjectName("humidex_label")
        self.statusEdit_label = QtWidgets.QLabel(self.tab_today)
        self.statusEdit_label.setGeometry(QtCore.QRect(630, 361, 55, 27))
        self.statusEdit_label.setObjectName("statusEdit_label")
        self.sunriseEdit_label = QtWidgets.QLabel(self.tab_today)
        self.sunriseEdit_label.setGeometry(QtCore.QRect(150, 90, 85, 27))
        self.sunriseEdit_label.setText("")
        self.sunriseEdit_label.setTextFormat(QtCore.Qt.AutoText)
        self.sunriseEdit_label.setObjectName("sunriseEdit_label")
        self.sunsetEdit_label = QtWidgets.QLabel(self.tab_today)
        self.sunsetEdit_label.setGeometry(QtCore.QRect(150, 140, 85, 27))
        self.sunsetEdit_label.setText("")
        self.sunsetEdit_label.setTextFormat(QtCore.Qt.AutoText)
        self.sunsetEdit_label.setObjectName("sunsetEdit_label")
        self.humidityEdit_label = QtWidgets.QLabel(self.tab_today)
        self.humidityEdit_label.setGeometry(QtCore.QRect(290, 410, 128, 27))
        self.humidityEdit_label.setText("")
        self.humidityEdit_label.setObjectName("humidityEdit_label")
        self.precipitationProbabilityEdit_label = QtWidgets.QLabel(self.tab_today)
        self.precipitationProbabilityEdit_label.setGeometry(QtCore.QRect(290, 480, 245, 27))
        self.precipitationProbabilityEdit_label.setText("")
        self.precipitationProbabilityEdit_label.setObjectName("precipitationProbabilityEdit_label")
        self.humidexEdit_label = QtWidgets.QLabel(self.tab_today)
        self.humidexEdit_label.setGeometry(QtCore.QRect(1050, 410, 101, 27))
        self.humidexEdit_label.setText("")
        self.humidexEdit_label.setObjectName("humidexEdit_label")
        self.temperatureEdit_label = QtWidgets.QLabel(self.tab_today)
        self.temperatureEdit_label.setGeometry(QtCore.QRect(290, 70, 151, 151))
        self.temperatureEdit_label.setMouseTracking(False)
        self.temperatureEdit_label.setStyleSheet("")
        self.temperatureEdit_label.setText("")
        self.temperatureEdit_label.setObjectName("temperatureEdit_label")
        self.tempText_label = QtWidgets.QLabel(self.tab_today)
        self.tempText_label.setGeometry(QtCore.QRect(340, 145, 47, 13))
        self.tempText_label.setText("")
        self.tempText_label.setObjectName("tempText_label")
        self.feelsText_label = QtWidgets.QLabel(self.tab_today)
        self.feelsText_label.setGeometry(QtCore.QRect(665, 145, 47, 13))
        self.feelsText_label.setText("")
        self.feelsText_label.setObjectName("feelsText_label")
        self.tabWidget.addTab(self.tab_today, "")
        self.tab_days = QtWidgets.QWidget()
        self.tab_days.setObjectName("tab_days")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.tab_days)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1021, 541))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.tabWidget.addTab(self.tab_days, "")
        self.tab_hours = QtWidgets.QWidget()
        self.tab_hours.setObjectName("tab_hours")
        self.label_4 = QtWidgets.QLabel(self.tab_hours)
        self.label_4.setGeometry(QtCore.QRect(90, 140, 511, 71))
        self.label_4.setObjectName("label_4")
        self.tabWidget.addTab(self.tab_hours, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 21))
        self.menubar.setObjectName("menubar")
        self.settings_btn = QtWidgets.QMenu(self.menubar)
        self.settings_btn.setObjectName("settings_btn")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionaWD = QtWidgets.QAction(MainWindow)
        self.actionaWD.setObjectName("actionaWD")
        self.change_city_btn = QtWidgets.QAction(MainWindow)
        self.change_city_btn.setObjectName("change_city_btn")
        self.settings_btn.addAction(self.change_city_btn)
        self.menubar.addAction(self.settings_btn.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Главное меню"))
        self.sunrise_label.setText(_translate("MainWindow", "Восход:"))
        self.sunset_label.setText(_translate("MainWindow", "Закат:"))
        self.humidity_label.setText(_translate("MainWindow", "Влажность:"))
        self.precipitationProbability_label.setText(_translate("MainWindow", "Вероятность осадков:"))
        self.feelsLike_label.setText(_translate("MainWindow", "По ощущению"))
        self.temperature_label.setText(_translate("MainWindow", "t, C"))
        self.humidex_label.setText(_translate("MainWindow", "Humidex:"))
        self.statusEdit_label.setText(_translate("MainWindow", "Ясно"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_today), _translate("MainWindow", "Сегодня"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.label_2.setText(_translate("MainWindow", "TextLabel"))
        self.label_3.setText(_translate("MainWindow", "TextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_days), _translate("MainWindow", "3 дня"))
        self.label_4.setText(_translate("MainWindow", "Ведутся технические работы"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_hours), _translate("MainWindow", "24 часа"))
        self.settings_btn.setTitle(_translate("MainWindow", "Настройки"))
        self.actionaWD.setText(_translate("MainWindow", "aWD"))
        self.change_city_btn.setText(_translate("MainWindow", "Сменить город"))
