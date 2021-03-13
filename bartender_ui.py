from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_main(object):
    def setupUi(self, main):
        main.setObjectName("main")
        main.resize(1024, 600)
        main.setMinimumSize(QtCore.QSize(800, 480))
        self.stacked_widg = QtWidgets.QStackedWidget(main)
        self.stacked_widg.setGeometry(QtCore.QRect(0, 0, 1024, 600))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.stacked_widg.setFont(font)
        self.stacked_widg.setStyleSheet("background-color:black;")
        self.stacked_widg.setObjectName("stacked_widg")
        self.MainScreen = QtWidgets.QWidget()
        self.MainScreen.setStyleSheet("background-color:rgb(44, 44, 44);")
        self.MainScreen.setObjectName("MainScreen")
        self.welcome_label = QtWidgets.QLabel(self.MainScreen)
        self.welcome_label.setGeometry(QtCore.QRect(240, -30, 711, 141))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(50)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.welcome_label.setFont(font)
        self.welcome_label.setStyleSheet("color: white;")
        self.welcome_label.setWordWrap(True)
        self.welcome_label.setObjectName("welcome_label")
        self.start_button = QtWidgets.QPushButton(self.MainScreen)
        self.start_button.setGeometry(QtCore.QRect(270, 230, 501, 221))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(40)
        self.start_button.setFont(font)
        self.start_button.setStyleSheet(
            "background-color:rgb(85, 239, 196);\n"
            "border-style: solid;\n"
            "border-color: rgb(43, 43, 43);\n"
            "border-width: 5px;\n"
            "border-radius: 10px;\n"
            "color:white;\n"
            ""
        )
        self.start_button.setObjectName("start_button")
        self.home_settings = QtWidgets.QPushButton(self.MainScreen)
        self.home_settings.setGeometry(QtCore.QRect(920, 10, 91, 51))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.home_settings.setFont(font)
        self.home_settings.setStyleSheet(
            "background-color:white;\n"
            "border-style: solid;\n"
            "border-color: rgb(43, 43, 43);\n"
            "border-width: 5px;\n"
            "border-radius: 10px;\n"
            "\n"
            ""
        )
        self.home_settings.setObjectName("home_settings")
        self.bartender_label = QtWidgets.QLabel(self.MainScreen)
        self.bartender_label.setGeometry(QtCore.QRect(150, 90, 841, 61))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(50)
        self.bartender_label.setFont(font)
        self.bartender_label.setStyleSheet("color: white;")
        self.bartender_label.setWordWrap(True)
        self.bartender_label.setObjectName("bartender_label")
        self.stacked_widg.addWidget(self.MainScreen)
        self.DrinkSelection = QtWidgets.QWidget()
        self.DrinkSelection.setStyleSheet("background-color:rgb(44, 44, 44);")
        self.DrinkSelection.setObjectName("DrinkSelection")
        self.select_drink_label = QtWidgets.QLabel(self.DrinkSelection)
        self.select_drink_label.setGeometry(QtCore.QRect(310, 10, 511, 61))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(40)
        self.select_drink_label.setFont(font)
        self.select_drink_label.setStyleSheet("color:rgb(85, 239, 196);")
        self.select_drink_label.setObjectName("select_drink_label")
        self.drink_list = QtWidgets.QListWidget(self.DrinkSelection)
        self.drink_list.setGeometry(QtCore.QRect(300, 80, 501, 281))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(30)
        self.drink_list.setFont(font)
        self.drink_list.setStyleSheet(
            "color:white;\n"
            "border: None;\n"
            "selection-background-color:rgb(85, 239, 196);"
        )
        self.drink_list.setObjectName("drink_list")
        item = QtWidgets.QListWidgetItem()
        self.drink_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.drink_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.drink_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.drink_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.drink_list.addItem(item)
        self.make_drink_button = QtWidgets.QPushButton(self.DrinkSelection)
        self.make_drink_button.setGeometry(QtCore.QRect(270, 430, 491, 131))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(40)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.make_drink_button.setFont(font)
        self.make_drink_button.setStyleSheet(
            "background-color:rgb(85, 239, 196);\n"
            "border-style: solid;\n"
            "border-color: rgb(43, 43, 43);\n"
            "border-width: 5px;\n"
            "border-radius: 10px;\n"
            "color:white;\n"
            ""
        )
        self.make_drink_button.setObjectName("make_drink_button")
        self.select_drink_back = QtWidgets.QPushButton(self.DrinkSelection)
        self.select_drink_back.setGeometry(QtCore.QRect(10, 10, 101, 71))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(25)
        self.select_drink_back.setFont(font)
        self.select_drink_back.setStyleSheet(
            "background-color:white;\n"
            "border-style: solid;\n"
            "border-color: rgb(43, 43, 43);\n"
            "border-width: 5px;\n"
            "border-radius: 10px;"
        )
        self.select_drink_back.setObjectName("select_drink_back")
        self.ice_in_cup_checkbox = QtWidgets.QCheckBox(self.DrinkSelection)
        self.ice_in_cup_checkbox.setGeometry(QtCore.QRect(390, 370, 361, 41))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.ice_in_cup_checkbox.setFont(font)
        self.ice_in_cup_checkbox.setStyleSheet("color:rgb(85, 239, 196);")
        self.ice_in_cup_checkbox.setObjectName("ice_in_cup_checkbox")
        self.stacked_widg.addWidget(self.DrinkSelection)
        self.makingDrink = QtWidgets.QWidget()
        self.makingDrink.setStyleSheet("background-color:rgb(44, 44, 44);")
        self.makingDrink.setObjectName("makingDrink")
        self.making_drink_label = QtWidgets.QLabel(self.makingDrink)
        self.making_drink_label.setGeometry(QtCore.QRect(250, 0, 711, 91))
        font = QtGui.QFont()
        font.setPointSize(50)
        self.making_drink_label.setFont(font)
        self.making_drink_label.setStyleSheet("color:rgb(85, 239, 196);")
        self.making_drink_label.setObjectName("making_drink_label")
        self.making_drink_cancel = QtWidgets.QPushButton(self.makingDrink)
        self.making_drink_cancel.setGeometry(QtCore.QRect(400, 410, 251, 111))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(40)
        self.making_drink_cancel.setFont(font)
        self.making_drink_cancel.setStyleSheet(
            "background-color:rgb(255, 118, 117);\n"
            "border-style: solid;\n"
            "border-color: rgb(43, 43, 43);\n"
            "border-width: 5px;\n"
            "border-radius: 10px;\n"
            "color:white;\n"
            "\n"
            ""
        )
        self.making_drink_cancel.setObjectName("making_drink_cancel")
        self.animation_label = QtWidgets.QLabel(self.makingDrink)
        self.animation_label.setGeometry(QtCore.QRect(370, 130, 301, 241))
        self.animation_label.setText("")
        self.animation_label.setObjectName("animation_label")
        self.stacked_widg.addWidget(self.makingDrink)
        self.settings_auth = QtWidgets.QWidget()
        self.settings_auth.setStyleSheet("background-color:rgb(42, 42, 42);")
        self.settings_auth.setObjectName("settings_auth")
        self.enter_passcode_label = QtWidgets.QLabel(self.settings_auth)
        self.enter_passcode_label.setGeometry(QtCore.QRect(290, 0, 471, 91))
        font = QtGui.QFont()
        font.setPointSize(50)
        self.enter_passcode_label.setFont(font)
        self.enter_passcode_label.setStyleSheet("color:rgb(85, 239, 196);")
        self.enter_passcode_label.setObjectName("enter_passcode_label")
        self.pass_val_1 = QtWidgets.QComboBox(self.settings_auth)
        self.pass_val_1.setGeometry(QtCore.QRect(200, 170, 121, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pass_val_1.setFont(font)
        self.pass_val_1.setStyleSheet("color:rgb(85, 239, 196);")
        self.pass_val_1.setObjectName("pass_val_1")
        self.pass_val_1.addItem("")
        self.pass_val_1.addItem("")
        self.pass_val_1.addItem("")
        self.pass_val_1.addItem("")
        self.pass_val_1.addItem("")
        self.pass_val_1.addItem("")
        self.pass_val_1.addItem("")
        self.pass_val_1.addItem("")
        self.pass_val_1.addItem("")
        self.pass_val_1.addItem("")
        self.pass_val_2 = QtWidgets.QComboBox(self.settings_auth)
        self.pass_val_2.setGeometry(QtCore.QRect(370, 170, 121, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pass_val_2.setFont(font)
        self.pass_val_2.setStyleSheet("color:rgb(85, 239, 196);")
        self.pass_val_2.setObjectName("pass_val_2")
        self.pass_val_2.addItem("")
        self.pass_val_2.addItem("")
        self.pass_val_2.addItem("")
        self.pass_val_2.addItem("")
        self.pass_val_2.addItem("")
        self.pass_val_2.addItem("")
        self.pass_val_2.addItem("")
        self.pass_val_2.addItem("")
        self.pass_val_2.addItem("")
        self.pass_val_2.addItem("")
        self.pass_val_3 = QtWidgets.QComboBox(self.settings_auth)
        self.pass_val_3.setGeometry(QtCore.QRect(540, 170, 121, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pass_val_3.setFont(font)
        self.pass_val_3.setStyleSheet("color:rgb(85, 239, 196);")
        self.pass_val_3.setObjectName("pass_val_3")
        self.pass_val_3.addItem("")
        self.pass_val_3.addItem("")
        self.pass_val_3.addItem("")
        self.pass_val_3.addItem("")
        self.pass_val_3.addItem("")
        self.pass_val_3.addItem("")
        self.pass_val_3.addItem("")
        self.pass_val_3.addItem("")
        self.pass_val_3.addItem("")
        self.pass_val_3.addItem("")
        self.pass_val_4 = QtWidgets.QComboBox(self.settings_auth)
        self.pass_val_4.setGeometry(QtCore.QRect(710, 170, 121, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pass_val_4.setFont(font)
        self.pass_val_4.setStyleSheet("color:rgb(85, 239, 196);")
        self.pass_val_4.setObjectName("pass_val_4")
        self.pass_val_4.addItem("")
        self.pass_val_4.addItem("")
        self.pass_val_4.addItem("")
        self.pass_val_4.addItem("")
        self.pass_val_4.addItem("")
        self.pass_val_4.addItem("")
        self.pass_val_4.addItem("")
        self.pass_val_4.addItem("")
        self.pass_val_4.addItem("")
        self.pass_val_4.addItem("")
        self.settings_submit = QtWidgets.QPushButton(self.settings_auth)
        self.settings_submit.setGeometry(QtCore.QRect(300, 350, 451, 121))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(40)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.settings_submit.setFont(font)
        self.settings_submit.setStyleSheet(
            "background-color:rgb(85, 239, 196);\n"
            "border-style: solid;\n"
            "border-color: rgb(43, 43, 43);\n"
            "border-width: 5px;\n"
            "border-radius: 10px;\n"
            "color:white;\n"
            ""
        )
        self.settings_submit.setObjectName("settings_submit")
        self.settings_auth_back = QtWidgets.QPushButton(self.settings_auth)
        self.settings_auth_back.setGeometry(QtCore.QRect(10, 10, 101, 71))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(25)
        self.settings_auth_back.setFont(font)
        self.settings_auth_back.setStyleSheet(
            "background-color:white;\n"
            "border-style: solid;\n"
            "border-color: rgb(43, 43, 43);\n"
            "border-width: 5px;\n"
            "border-radius: 10px;\n"
            ""
        )
        self.settings_auth_back.setObjectName("settings_auth_back")
        self.stacked_widg.addWidget(self.settings_auth)
        self.settings = QtWidgets.QWidget()
        self.settings.setStyleSheet("background-color:rgb(42, 42, 42);")
        self.settings.setObjectName("settings")
        self.settings_label = QtWidgets.QLabel(self.settings)
        self.settings_label.setGeometry(QtCore.QRect(390, -10, 261, 91))
        font = QtGui.QFont()
        font.setPointSize(50)
        self.settings_label.setFont(font)
        self.settings_label.setStyleSheet("color:rgb(85, 239, 196);")
        self.settings_label.setObjectName("settings_label")
        self.clean_system_button = QtWidgets.QPushButton(self.settings)
        self.clean_system_button.setGeometry(QtCore.QRect(830, 60, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.clean_system_button.setFont(font)
        self.clean_system_button.setStyleSheet(
            "background-color:rgb(85, 239, 196);\n"
            "border-style: solid;\n"
            "border-color: rgb(43, 43, 43);\n"
            "border-width: 5px;\n"
            "border-radius: 10px;\n"
            "color:white;"
        )
        self.clean_system_button.setObjectName("clean_system_button")
        self.settings_back = QtWidgets.QPushButton(self.settings)
        self.settings_back.setGeometry(QtCore.QRect(10, 10, 101, 71))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(25)
        self.settings_back.setFont(font)
        self.settings_back.setStyleSheet(
            "background-color:white;\n"
            "border-style: solid;\n"
            "border-color: rgb(43, 43, 43);\n"
            "border-width: 5px;\n"
            "border-radius: 10px;\n"
            ""
        )
        self.settings_back.setObjectName("settings_back")
        self.cancel_clean_button = QtWidgets.QPushButton(self.settings)
        self.cancel_clean_button.setGeometry(QtCore.QRect(830, 110, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.cancel_clean_button.setFont(font)
        self.cancel_clean_button.setStyleSheet(
            "background-color:rgb(255, 118, 117);\n"
            "border-style: solid;\n"
            "border-color: rgb(43, 43, 43);\n"
            "border-width: 5px;\n"
            "border-radius: 10px;\n"
            "color:white;\n"
            "\n"
            ""
        )
        self.cancel_clean_button.setObjectName("cancel_clean_button")
        self.drink_levels_button = QtWidgets.QPushButton(self.settings)
        self.drink_levels_button.setGeometry(QtCore.QRect(830, 10, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.drink_levels_button.setFont(font)
        self.drink_levels_button.setStyleSheet(
            "background-color:rgb(116, 185, 255);\n"
            "border-style: solid;\n"
            "border-color: rgb(43, 43, 43);\n"
            "border-width: 5px;\n"
            "border-radius: 10px;\n"
            "color:white;\n"
            "\n"
            ""
        )
        self.drink_levels_button.setObjectName("drink_levels_button")
        self.venmo_required_checkbox = QtWidgets.QCheckBox(self.settings)
        self.venmo_required_checkbox.setGeometry(QtCore.QRect(390, 90, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(20)
        self.venmo_required_checkbox.setFont(font)
        self.venmo_required_checkbox.setStyleSheet("color:rgb(85, 239, 196);")
        self.venmo_required_checkbox.setObjectName("venmo_required_checkbox")
        self.start_prime1 = QtWidgets.QPushButton(self.settings)
        self.start_prime1.setGeometry(QtCore.QRect(150, 210, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.start_prime1.setFont(font)
        self.start_prime1.setStyleSheet(
            "background-color:rgb(85, 239, 196);\n"
            "border-style: solid;\n"
            "border-color: rgb(43, 43, 43);\n"
            "border-width: 5px;\n"
            "border-radius: 10px;\n"
            "color:white;"
        )
        self.start_prime1.setObjectName("start_prime1")
        self.stop_prime1 = QtWidgets.QPushButton(self.settings)
        self.stop_prime1.setGeometry(QtCore.QRect(320, 210, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.stop_prime1.setFont(font)
        self.stop_prime1.setStyleSheet(
            "background-color:rgb(255, 118, 117);\n"
            "border-style: solid;\n"
            "border-color: rgb(43, 43, 43);\n"
            "border-width: 5px;\n"
            "border-radius: 10px;\n"
            "color:white;\n"
            "\n"
            ""
        )
        self.stop_prime1.setObjectName("stop_prime1")
        self.start_prime2 = QtWidgets.QPushButton(self.settings)
        self.start_prime2.setGeometry(QtCore.QRect(150, 290, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.start_prime2.setFont(font)
        self.start_prime2.setStyleSheet(
            "background-color:rgb(85, 239, 196);\n"
            "border-style: solid;\n"
            "border-color: rgb(43, 43, 43);\n"
            "border-width: 5px;\n"
            "border-radius: 10px;\n"
            "color:white;"
        )
        self.start_prime2.setObjectName("start_prime2")
        self.stop_prime2 = QtWidgets.QPushButton(self.settings)
        self.stop_prime2.setGeometry(QtCore.QRect(320, 290, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.stop_prime2.setFont(font)
        self.stop_prime2.setStyleSheet(
            "background-color:rgb(255, 118, 117);\n"
            "border-style: solid;\n"
            "border-color: rgb(43, 43, 43);\n"
            "border-width: 5px;\n"
            "border-radius: 10px;\n"
            "color:white;\n"
            "\n"
            ""
        )
        self.stop_prime2.setObjectName("stop_prime2")
        self.start_prime4 = QtWidgets.QPushButton(self.settings)
        self.start_prime4.setGeometry(QtCore.QRect(550, 210, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.start_prime4.setFont(font)
        self.start_prime4.setStyleSheet(
            "background-color:rgb(85, 239, 196);\n"
            "border-style: solid;\n"
            "border-color: rgb(43, 43, 43);\n"
            "border-width: 5px;\n"
            "border-radius: 10px;\n"
            "color:white;"
        )
        self.start_prime4.setObjectName("start_prime4")
        self.stop_prime4 = QtWidgets.QPushButton(self.settings)
        self.stop_prime4.setGeometry(QtCore.QRect(710, 210, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.stop_prime4.setFont(font)
        self.stop_prime4.setStyleSheet(
            "background-color:rgb(255, 118, 117);\n"
            "border-style: solid;\n"
            "border-color: rgb(43, 43, 43);\n"
            "border-width: 5px;\n"
            "border-radius: 10px;\n"
            "color:white;\n"
            "\n"
            ""
        )
        self.stop_prime4.setObjectName("stop_prime4")
        self.start_prime5 = QtWidgets.QPushButton(self.settings)
        self.start_prime5.setGeometry(QtCore.QRect(550, 290, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.start_prime5.setFont(font)
        self.start_prime5.setStyleSheet(
            "background-color:rgb(85, 239, 196);\n"
            "border-style: solid;\n"
            "border-color: rgb(43, 43, 43);\n"
            "border-width: 5px;\n"
            "border-radius: 10px;\n"
            "color:white;"
        )
        self.start_prime5.setObjectName("start_prime5")
        self.stop_prime5 = QtWidgets.QPushButton(self.settings)
        self.stop_prime5.setGeometry(QtCore.QRect(710, 290, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.stop_prime5.setFont(font)
        self.stop_prime5.setStyleSheet(
            "background-color:rgb(255, 118, 117);\n"
            "border-style: solid;\n"
            "border-color: rgb(43, 43, 43);\n"
            "border-width: 5px;\n"
            "border-radius: 10px;\n"
            "color:white;\n"
            "\n"
            ""
        )
        self.stop_prime5.setObjectName("stop_prime5")
        self.start_prime3 = QtWidgets.QPushButton(self.settings)
        self.start_prime3.setGeometry(QtCore.QRect(150, 370, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.start_prime3.setFont(font)
        self.start_prime3.setStyleSheet(
            "background-color:rgb(85, 239, 196);\n"
            "border-style: solid;\n"
            "border-color: rgb(43, 43, 43);\n"
            "border-width: 5px;\n"
            "border-radius: 10px;\n"
            "color:white;"
        )
        self.start_prime3.setObjectName("start_prime3")
        self.stop_prime3 = QtWidgets.QPushButton(self.settings)
        self.stop_prime3.setGeometry(QtCore.QRect(320, 370, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.stop_prime3.setFont(font)
        self.stop_prime3.setStyleSheet(
            "background-color:rgb(255, 118, 117);\n"
            "border-style: solid;\n"
            "border-color: rgb(43, 43, 43);\n"
            "border-width: 5px;\n"
            "border-radius: 10px;\n"
            "color:white;\n"
            "\n"
            ""
        )
        self.stop_prime3.setObjectName("stop_prime3")
        self.start_prime6 = QtWidgets.QPushButton(self.settings)
        self.start_prime6.setGeometry(QtCore.QRect(550, 370, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.start_prime6.setFont(font)
        self.start_prime6.setStyleSheet(
            "background-color:rgb(85, 239, 196);\n"
            "border-style: solid;\n"
            "border-color: rgb(43, 43, 43);\n"
            "border-width: 5px;\n"
            "border-radius: 10px;\n"
            "color:white;"
        )
        self.start_prime6.setObjectName("start_prime6")
        self.stop_prime6 = QtWidgets.QPushButton(self.settings)
        self.stop_prime6.setGeometry(QtCore.QRect(710, 370, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.stop_prime6.setFont(font)
        self.stop_prime6.setStyleSheet(
            "background-color:rgb(255, 118, 117);\n"
            "border-style: solid;\n"
            "border-color: rgb(43, 43, 43);\n"
            "border-width: 5px;\n"
            "border-radius: 10px;\n"
            "color:white;\n"
            "\n"
            ""
        )
        self.stop_prime6.setObjectName("stop_prime6")
        self.stacked_widg.addWidget(self.settings)
        self.drink_levels = QtWidgets.QWidget()
        self.drink_levels.setStyleSheet("background-color:rgb(42, 42, 42);")
        self.drink_levels.setObjectName("drink_levels")
        self.drink_level_title = QtWidgets.QLabel(self.drink_levels)
        self.drink_level_title.setGeometry(QtCore.QRect(360, 0, 411, 91))
        font = QtGui.QFont()
        font.setPointSize(50)
        self.drink_level_title.setFont(font)
        self.drink_level_title.setStyleSheet("color:rgb(85, 239, 196);")
        self.drink_level_title.setObjectName("drink_level_title")
        self.pump1_label = QtWidgets.QLabel(self.drink_levels)
        self.pump1_label.setGeometry(QtCore.QRect(30, 110, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.pump1_label.setFont(font)
        self.pump1_label.setStyleSheet("color:rgb(85, 239, 196);")
        self.pump1_label.setObjectName("pump1_label")
        self.pump2_label = QtWidgets.QLabel(self.drink_levels)
        self.pump2_label.setGeometry(QtCore.QRect(30, 170, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.pump2_label.setFont(font)
        self.pump2_label.setStyleSheet("color:rgb(85, 239, 196);")
        self.pump2_label.setObjectName("pump2_label")
        self.pump3_label = QtWidgets.QLabel(self.drink_levels)
        self.pump3_label.setGeometry(QtCore.QRect(30, 230, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.pump3_label.setFont(font)
        self.pump3_label.setStyleSheet("color:rgb(85, 239, 196);")
        self.pump3_label.setObjectName("pump3_label")
        self.pump4_label = QtWidgets.QLabel(self.drink_levels)
        self.pump4_label.setGeometry(QtCore.QRect(30, 290, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.pump4_label.setFont(font)
        self.pump4_label.setStyleSheet("color:rgb(85, 239, 196);")
        self.pump4_label.setObjectName("pump4_label")
        self.pump5_label = QtWidgets.QLabel(self.drink_levels)
        self.pump5_label.setGeometry(QtCore.QRect(30, 350, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.pump5_label.setFont(font)
        self.pump5_label.setStyleSheet("color:rgb(85, 239, 196);")
        self.pump5_label.setObjectName("pump5_label")
        self.pump6_label = QtWidgets.QLabel(self.drink_levels)
        self.pump6_label.setGeometry(QtCore.QRect(30, 410, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.pump6_label.setFont(font)
        self.pump6_label.setStyleSheet("color:rgb(85, 239, 196);")
        self.pump6_label.setObjectName("pump6_label")
        self.pump1_level = QtWidgets.QLabel(self.drink_levels)
        self.pump1_level.setGeometry(QtCore.QRect(190, 110, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.pump1_level.setFont(font)
        self.pump1_level.setStyleSheet("color:rgb(85, 239, 196);")
        self.pump1_level.setText("")
        self.pump1_level.setObjectName("pump1_level")
        self.pump2_level = QtWidgets.QLabel(self.drink_levels)
        self.pump2_level.setGeometry(QtCore.QRect(190, 170, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.pump2_level.setFont(font)
        self.pump2_level.setStyleSheet("color:rgb(85, 239, 196);")
        self.pump2_level.setText("")
        self.pump2_level.setObjectName("pump2_level")
        self.pump3_level = QtWidgets.QLabel(self.drink_levels)
        self.pump3_level.setGeometry(QtCore.QRect(190, 230, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.pump3_level.setFont(font)
        self.pump3_level.setStyleSheet("color:rgb(85, 239, 196);")
        self.pump3_level.setText("")
        self.pump3_level.setObjectName("pump3_level")
        self.pump4_level = QtWidgets.QLabel(self.drink_levels)
        self.pump4_level.setGeometry(QtCore.QRect(190, 290, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.pump4_level.setFont(font)
        self.pump4_level.setStyleSheet("color:rgb(85, 239, 196);")
        self.pump4_level.setText("")
        self.pump4_level.setObjectName("pump4_level")
        self.pump5_level = QtWidgets.QLabel(self.drink_levels)
        self.pump5_level.setGeometry(QtCore.QRect(190, 350, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.pump5_level.setFont(font)
        self.pump5_level.setStyleSheet("color:rgb(85, 239, 196);")
        self.pump5_level.setText("")
        self.pump5_level.setObjectName("pump5_level")
        self.pump6_level = QtWidgets.QLabel(self.drink_levels)
        self.pump6_level.setGeometry(QtCore.QRect(190, 410, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.pump6_level.setFont(font)
        self.pump6_level.setStyleSheet("color:rgb(85, 239, 196);")
        self.pump6_level.setText("")
        self.pump6_level.setObjectName("pump6_level")
        self.levels_back_button = QtWidgets.QPushButton(self.drink_levels)
        self.levels_back_button.setGeometry(QtCore.QRect(10, 10, 101, 71))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(25)
        self.levels_back_button.setFont(font)
        self.levels_back_button.setStyleSheet(
            "background-color:white;\n"
            "border-style: solid;\n"
            "border-color: rgb(43, 43, 43);\n"
            "border-width: 5px;\n"
            "border-radius: 10px;\n"
            ""
        )
        self.levels_back_button.setObjectName("levels_back_button")
        self.stacked_widg.addWidget(self.drink_levels)
        self.venmo = QtWidgets.QWidget()
        self.venmo.setStyleSheet("background-color:rgb(42, 42, 42);")
        self.venmo.setObjectName("venmo")
        self.venmo_main_label = QtWidgets.QLabel(self.venmo)
        self.venmo_main_label.setGeometry(QtCore.QRect(270, 10, 751, 71))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(35)
        self.venmo_main_label.setFont(font)
        self.venmo_main_label.setStyleSheet("color:rgb(85, 239, 196);")
        self.venmo_main_label.setObjectName("venmo_main_label")
        self.venmo_price = QtWidgets.QLabel(self.venmo)
        self.venmo_price.setGeometry(QtCore.QRect(400, 70, 281, 71))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(30)
        self.venmo_price.setFont(font)
        self.venmo_price.setStyleSheet("color:rgb(255, 118, 117);")
        self.venmo_price.setObjectName("venmo_price")
        self.qr_label = QtWidgets.QLabel(self.venmo)
        self.qr_label.setGeometry(QtCore.QRect(400, 170, 241, 233))
        self.qr_label.setText("")
        self.qr_label.setObjectName("qr_label")
        self.venmo_back = QtWidgets.QPushButton(self.venmo)
        self.venmo_back.setGeometry(QtCore.QRect(10, 10, 101, 71))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(25)
        self.venmo_back.setFont(font)
        self.venmo_back.setStyleSheet(
            "background-color:white;\n"
            "border-style: solid;\n"
            "border-color: rgb(43, 43, 43);\n"
            "border-width: 5px;\n"
            "border-radius: 10px;\n"
            ""
        )
        self.venmo_back.setObjectName("venmo_back")
        self.venmo_label_type = QtWidgets.QLabel(self.venmo)
        self.venmo_label_type.setGeometry(QtCore.QRect(130, 480, 111, 71))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(30)
        self.venmo_label_type.setFont(font)
        self.venmo_label_type.setStyleSheet("color:rgb(85, 239, 196);")
        self.venmo_label_type.setObjectName("venmo_label_type")
        self.venmo_code_id = QtWidgets.QLabel(self.venmo)
        self.venmo_code_id.setGeometry(QtCore.QRect(270, 460, 141, 101))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(50)
        self.venmo_code_id.setFont(font)
        self.venmo_code_id.setStyleSheet("color:rgb(255, 118, 117);")
        self.venmo_code_id.setText("")
        self.venmo_code_id.setObjectName("venmo_code_id")
        self.venmo_whats_it_for_label = QtWidgets.QLabel(self.venmo)
        self.venmo_whats_it_for_label.setGeometry(QtCore.QRect(420, 480, 541, 71))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(30)
        self.venmo_whats_it_for_label.setFont(font)
        self.venmo_whats_it_for_label.setStyleSheet("color:rgb(85, 239, 196);")
        self.venmo_whats_it_for_label.setObjectName("venmo_whats_it_for_label")
        self.stacked_widg.addWidget(self.venmo)
        self.PostVenmo = QtWidgets.QWidget()
        self.PostVenmo.setStyleSheet("background-color:rgb(42, 42, 42);")
        self.PostVenmo.setObjectName("PostVenmo")
        self.thanks_label = QtWidgets.QLabel(self.PostVenmo)
        self.thanks_label.setGeometry(QtCore.QRect(290, 20, 241, 71))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(50)
        self.thanks_label.setFont(font)
        self.thanks_label.setStyleSheet("color:rgb(85, 239, 196);")
        self.thanks_label.setObjectName("thanks_label")
        self.post_venmo_name_label = QtWidgets.QLabel(self.PostVenmo)
        self.post_venmo_name_label.setGeometry(QtCore.QRect(550, 20, 361, 71))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(50)
        self.post_venmo_name_label.setFont(font)
        self.post_venmo_name_label.setStyleSheet("color:rgb(85, 239, 196);")
        self.post_venmo_name_label.setText("")
        self.post_venmo_name_label.setObjectName("post_venmo_name_label")
        self.post_venmo_home_button = QtWidgets.QPushButton(self.PostVenmo)
        self.post_venmo_home_button.setGeometry(QtCore.QRect(290, 400, 471, 161))
        font = QtGui.QFont()
        font.setPointSize(50)
        self.post_venmo_home_button.setFont(font)
        self.post_venmo_home_button.setStyleSheet(
            "background-color:rgb(85, 239, 196);\n"
            "border-style: solid;\n"
            "border-color: rgb(43, 43, 43);\n"
            "border-width: 5px;\n"
            "border-radius: 10px;\n"
            "color:white;"
        )
        self.post_venmo_home_button.setObjectName("post_venmo_home_button")
        self.venmo_profile_pic = QtWidgets.QLabel(self.PostVenmo)
        self.venmo_profile_pic.setGeometry(QtCore.QRect(370, 140, 311, 221))
        self.venmo_profile_pic.setText("")
        self.venmo_profile_pic.setObjectName("venmo_profile_pic")
        self.stacked_widg.addWidget(self.PostVenmo)

        self.retranslateUi(main)
        self.stacked_widg.setCurrentIndex(6)
        QtCore.QMetaObject.connectSlotsByName(main)

    def retranslateUi(self, main):
        _translate = QtCore.QCoreApplication.translate
        main.setWindowTitle(_translate("main", "drink"))
        self.welcome_label.setText(_translate("main", "Welcome To The"))
        self.start_button.setText(_translate("main", "Make a Drink"))
        self.home_settings.setText(_translate("main", "Settings"))
        self.bartender_label.setText(_translate("main", "Automated Bartender"))
        self.select_drink_label.setText(_translate("main", "Select a Drink:"))
        __sortingEnabled = self.drink_list.isSortingEnabled()
        self.drink_list.setSortingEnabled(False)
        item = self.drink_list.item(0)
        item.setText(_translate("main", "Margarita"))
        item = self.drink_list.item(1)
        item.setText(_translate("main", "Long Island Iced Tea"))
        item = self.drink_list.item(2)
        item.setText(_translate("main", "Tequila Sunrise"))
        item = self.drink_list.item(3)
        item.setText(_translate("main", "Rum & Coke"))
        item = self.drink_list.item(4)
        item.setText(_translate("main", "Mystery"))
        self.drink_list.setSortingEnabled(__sortingEnabled)
        self.make_drink_button.setText(_translate("main", "Make My Drink!"))
        self.select_drink_back.setText(_translate("main", "Back"))
        self.ice_in_cup_checkbox.setText(_translate("main", "Ice in cup?"))
        self.making_drink_label.setText(_translate("main", "Making Your Drink!"))
        self.making_drink_cancel.setText(_translate("main", "Cancel"))
        self.enter_passcode_label.setText(_translate("main", "Enter Passcode"))
        self.pass_val_1.setItemText(0, _translate("main", "1"))
        self.pass_val_1.setItemText(1, _translate("main", "2"))
        self.pass_val_1.setItemText(2, _translate("main", "3"))
        self.pass_val_1.setItemText(3, _translate("main", "4"))
        self.pass_val_1.setItemText(4, _translate("main", "5"))
        self.pass_val_1.setItemText(5, _translate("main", "6"))
        self.pass_val_1.setItemText(6, _translate("main", "7"))
        self.pass_val_1.setItemText(7, _translate("main", "8"))
        self.pass_val_1.setItemText(8, _translate("main", "9"))
        self.pass_val_1.setItemText(9, _translate("main", "10"))
        self.pass_val_2.setItemText(0, _translate("main", "1"))
        self.pass_val_2.setItemText(1, _translate("main", "2"))
        self.pass_val_2.setItemText(2, _translate("main", "3"))
        self.pass_val_2.setItemText(3, _translate("main", "4"))
        self.pass_val_2.setItemText(4, _translate("main", "5"))
        self.pass_val_2.setItemText(5, _translate("main", "6"))
        self.pass_val_2.setItemText(6, _translate("main", "7"))
        self.pass_val_2.setItemText(7, _translate("main", "8"))
        self.pass_val_2.setItemText(8, _translate("main", "9"))
        self.pass_val_2.setItemText(9, _translate("main", "10"))
        self.pass_val_3.setItemText(0, _translate("main", "1"))
        self.pass_val_3.setItemText(1, _translate("main", "2"))
        self.pass_val_3.setItemText(2, _translate("main", "3"))
        self.pass_val_3.setItemText(3, _translate("main", "4"))
        self.pass_val_3.setItemText(4, _translate("main", "5"))
        self.pass_val_3.setItemText(5, _translate("main", "6"))
        self.pass_val_3.setItemText(6, _translate("main", "7"))
        self.pass_val_3.setItemText(7, _translate("main", "8"))
        self.pass_val_3.setItemText(8, _translate("main", "9"))
        self.pass_val_3.setItemText(9, _translate("main", "10"))
        self.pass_val_4.setItemText(0, _translate("main", "1"))
        self.pass_val_4.setItemText(1, _translate("main", "2"))
        self.pass_val_4.setItemText(2, _translate("main", "3"))
        self.pass_val_4.setItemText(3, _translate("main", "4"))
        self.pass_val_4.setItemText(4, _translate("main", "5"))
        self.pass_val_4.setItemText(5, _translate("main", "6"))
        self.pass_val_4.setItemText(6, _translate("main", "7"))
        self.pass_val_4.setItemText(7, _translate("main", "8"))
        self.pass_val_4.setItemText(8, _translate("main", "9"))
        self.pass_val_4.setItemText(9, _translate("main", "10"))
        self.settings_submit.setText(_translate("main", "Submit"))
        self.settings_auth_back.setText(_translate("main", "Back"))
        self.settings_label.setText(_translate("main", "Settings"))
        self.clean_system_button.setText(_translate("main", "Clean System"))
        self.settings_back.setText(_translate("main", "Back"))
        self.cancel_clean_button.setText(_translate("main", "Cancel Clean"))
        self.drink_levels_button.setText(_translate("main", "Levels"))
        self.venmo_required_checkbox.setText(_translate("main", "Require Venmo"))
        self.start_prime1.setText(_translate("main", "Prime 1"))
        self.stop_prime1.setText(_translate("main", "Stop 1"))
        self.start_prime2.setText(_translate("main", "Prime 2"))
        self.stop_prime2.setText(_translate("main", "Stop 2"))
        self.start_prime4.setText(_translate("main", "Prime 4"))
        self.stop_prime4.setText(_translate("main", "Stop 4"))
        self.start_prime5.setText(_translate("main", "Prime 5"))
        self.stop_prime5.setText(_translate("main", "Stop 5"))
        self.start_prime3.setText(_translate("main", "Prime 3"))
        self.stop_prime3.setText(_translate("main", "Stop 3"))
        self.start_prime6.setText(_translate("main", "Prime 6"))
        self.stop_prime6.setText(_translate("main", "Stop 6"))
        self.drink_level_title.setText(_translate("main", "Drink Levels"))
        self.pump1_label.setText(_translate("main", "Pump 1:"))
        self.pump2_label.setText(_translate("main", "Pump 2:"))
        self.pump3_label.setText(_translate("main", "Pump 3:"))
        self.pump4_label.setText(_translate("main", "Pump 4:"))
        self.pump5_label.setText(_translate("main", "Pump 5:"))
        self.pump6_label.setText(_translate("main", "Pump 6:"))
        self.levels_back_button.setText(_translate("main", "Back"))
        self.venmo_main_label.setText(_translate("main", "Venmo The Code Below"))
        self.venmo_price.setText(_translate("main", "Price: $2.00"))
        self.venmo_back.setText(_translate("main", "Back"))
        self.venmo_label_type.setText(_translate("main", "Type:"))
        self.venmo_whats_it_for_label.setText(
            _translate("main", "in the 'What's it for?' field.")
        )
        self.thanks_label.setText(_translate("main", "Thanks"))
        self.post_venmo_home_button.setText(_translate("main", "Home"))
