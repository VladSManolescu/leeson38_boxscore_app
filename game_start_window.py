# Form implementation generated from reading ui file '.\game_start_window.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(879, 388)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.team_home_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.team_home_label.setGeometry(QtCore.QRect(40, 40, 151, 81))
        self.team_home_label.setObjectName("team_home_label")
        self.team_away_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.team_away_label.setGeometry(QtCore.QRect(560, 40, 151, 81))
        self.team_away_label.setObjectName("team_away_label")
        self.app_title_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.app_title_label.setGeometry(QtCore.QRect(230, 10, 331, 91))
        self.app_title_label.setObjectName("app_title_label")
        self.combo_home = QtWidgets.QComboBox(parent=self.centralwidget)
        self.combo_home.setGeometry(QtCore.QRect(40, 110, 131, 22))
        self.combo_home.setObjectName("combo_home")
        self.combo_away = QtWidgets.QComboBox(parent=self.centralwidget)
        self.combo_away.setGeometry(QtCore.QRect(560, 110, 131, 22))
        self.combo_away.setObjectName("combo_away")
        self.start_game_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.start_game_button.setGeometry(QtCore.QRect(310, 280, 171, 31))
        self.start_game_button.setObjectName("start_game_button")
        self.logo_image = QtWidgets.QLabel(parent=self.centralwidget)
        self.logo_image.setGeometry(QtCore.QRect(280, 90, 261, 221))
        self.logo_image.setText("")
        self.logo_image.setPixmap(QtGui.QPixmap(":/newPrefix/basketball.png"))
        self.logo_image.setScaledContents(True)
        self.logo_image.setObjectName("logo_image")
        self.checkBox_home_1 = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.checkBox_home_1.setGeometry(QtCore.QRect(10, 160, 75, 20))
        self.checkBox_home_1.setObjectName("checkBox_home_1")
        self.checkBox_home_2 = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.checkBox_home_2.setGeometry(QtCore.QRect(100, 190, 75, 20))
        self.checkBox_home_2.setObjectName("checkBox_home_2")
        self.checkBox_home_3 = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.checkBox_home_3.setGeometry(QtCore.QRect(10, 190, 75, 20))
        self.checkBox_home_3.setObjectName("checkBox_home_3")
        self.checkBox_home_4 = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.checkBox_home_4.setGeometry(QtCore.QRect(100, 160, 75, 20))
        self.checkBox_home_4.setObjectName("checkBox_home_4")
        self.checkBox_home_5 = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.checkBox_home_5.setGeometry(QtCore.QRect(200, 160, 75, 20))
        self.checkBox_home_5.setObjectName("checkBox_home_5")
        self.checkBox_home_6 = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.checkBox_home_6.setGeometry(QtCore.QRect(200, 190, 75, 20))
        self.checkBox_home_6.setObjectName("checkBox_home_6")
        self.checkBox_home_7 = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.checkBox_home_7.setGeometry(QtCore.QRect(100, 220, 75, 20))
        self.checkBox_home_7.setObjectName("checkBox_home_7")
        self.checkBox_home_8 = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.checkBox_home_8.setGeometry(QtCore.QRect(200, 220, 75, 20))
        self.checkBox_home_8.setObjectName("checkBox_home_8")
        self.checkBox_home_9 = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.checkBox_home_9.setGeometry(QtCore.QRect(100, 250, 75, 20))
        self.checkBox_home_9.setObjectName("checkBox_home_9")
        self.checkBox_home_10 = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.checkBox_home_10.setGeometry(QtCore.QRect(200, 250, 75, 20))
        self.checkBox_home_10.setObjectName("checkBox_home_10")
        self.checkBox_home_11 = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.checkBox_home_11.setGeometry(QtCore.QRect(10, 250, 75, 20))
        self.checkBox_home_11.setObjectName("checkBox_home_11")
        self.checkBox_home_12 = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.checkBox_home_12.setGeometry(QtCore.QRect(10, 220, 75, 20))
        self.checkBox_home_12.setObjectName("checkBox_home_12")
        self.checkBox_away_2 = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.checkBox_away_2.setGeometry(QtCore.QRect(650, 160, 75, 20))
        self.checkBox_away_2.setObjectName("checkBox_away_2")
        self.checkBox_away_10 = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.checkBox_away_10.setGeometry(QtCore.QRect(560, 250, 75, 20))
        self.checkBox_away_10.setObjectName("checkBox_away_10")
        self.checkBox_away_8 = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.checkBox_away_8.setGeometry(QtCore.QRect(650, 220, 75, 20))
        self.checkBox_away_8.setObjectName("checkBox_away_8")
        self.checkBox_away_9 = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.checkBox_away_9.setGeometry(QtCore.QRect(750, 220, 75, 20))
        self.checkBox_away_9.setObjectName("checkBox_away_9")
        self.checkBox_away_3 = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.checkBox_away_3.setGeometry(QtCore.QRect(750, 160, 75, 20))
        self.checkBox_away_3.setObjectName("checkBox_away_3")
        self.checkBox_away_5 = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.checkBox_away_5.setGeometry(QtCore.QRect(650, 190, 75, 20))
        self.checkBox_away_5.setObjectName("checkBox_away_5")
        self.checkBox_away_12 = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.checkBox_away_12.setGeometry(QtCore.QRect(750, 250, 75, 20))
        self.checkBox_away_12.setObjectName("checkBox_away_12")
        self.checkBox_away_6 = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.checkBox_away_6.setGeometry(QtCore.QRect(750, 190, 75, 20))
        self.checkBox_away_6.setObjectName("checkBox_away_6")
        self.checkBox_away_11 = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.checkBox_away_11.setGeometry(QtCore.QRect(650, 250, 75, 20))
        self.checkBox_away_11.setObjectName("checkBox_away_11")
        self.checkBox_away_4 = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.checkBox_away_4.setGeometry(QtCore.QRect(560, 190, 75, 20))
        self.checkBox_away_4.setObjectName("checkBox_away_4")
        self.checkBox_away_7 = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.checkBox_away_7.setGeometry(QtCore.QRect(560, 220, 75, 20))
        self.checkBox_away_7.setObjectName("checkBox_away_7")
        self.checkBox_away_1 = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.checkBox_away_1.setGeometry(QtCore.QRect(560, 160, 75, 20))
        self.checkBox_away_1.setObjectName("checkBox_away_1")
        self.logo_image.raise_()
        self.team_home_label.raise_()
        self.team_away_label.raise_()
        self.app_title_label.raise_()
        self.combo_home.raise_()
        self.combo_away.raise_()
        self.start_game_button.raise_()
        self.checkBox_home_1.raise_()
        self.checkBox_home_2.raise_()
        self.checkBox_home_3.raise_()
        self.checkBox_home_4.raise_()
        self.checkBox_home_5.raise_()
        self.checkBox_home_6.raise_()
        self.checkBox_home_7.raise_()
        self.checkBox_home_8.raise_()
        self.checkBox_home_9.raise_()
        self.checkBox_home_10.raise_()
        self.checkBox_home_11.raise_()
        self.checkBox_home_12.raise_()
        self.checkBox_away_2.raise_()
        self.checkBox_away_10.raise_()
        self.checkBox_away_8.raise_()
        self.checkBox_away_9.raise_()
        self.checkBox_away_3.raise_()
        self.checkBox_away_5.raise_()
        self.checkBox_away_12.raise_()
        self.checkBox_away_6.raise_()
        self.checkBox_away_11.raise_()
        self.checkBox_away_4.raise_()
        self.checkBox_away_7.raise_()
        self.checkBox_away_1.raise_()

        self.checkbox_home_list = [self.checkBox_home_1, self.checkBox_home_2, self.checkBox_home_3, self.checkBox_home_4,
                                   self.checkBox_home_5, self.checkBox_home_6, self.checkBox_home_7, self.checkBox_home_8,
                                   self.checkBox_home_9, self.checkBox_home_10, self.checkBox_home_11, self.checkBox_home_12]

        self.checkbox_away_list = [self.checkBox_away_1, self.checkBox_away_2, self.checkBox_away_3, self.checkBox_away_4,
                                   self.checkBox_away_12, self.checkBox_away_5, self.checkBox_away_6, self.checkBox_away_7,
                                   self.checkBox_away_8, self.checkBox_away_9, self.checkBox_away_10, self.checkBox_away_11]
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 879, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    @staticmethod
    def hide_elements(list_of_elements: list):
        for item in list_of_elements:
            item.hide()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.team_home_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">Team Home</span></p></body></html>"))
        self.team_away_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">Team Away</span></p></body></html>"))
        self.app_title_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:48pt;\">Scory App</span></p></body></html>"))
        self.start_game_button.setText(_translate("MainWindow", "Start Game"))
        self.checkBox_home_1.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_home_2.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_home_3.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_home_4.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_home_5.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_home_6.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_home_7.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_home_8.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_home_9.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_home_10.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_home_11.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_home_12.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_away_2.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_away_10.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_away_8.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_away_9.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_away_3.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_away_5.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_away_12.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_away_6.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_away_11.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_away_4.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_away_7.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_away_1.setText(_translate("MainWindow", "CheckBox"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
