import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QMovie, QPixmap
from bartender_ui import Ui_main
import time
from threading import Event
import threading
import requests
from requests.structures import CaseInsensitiveDict
import json
import yaml
from PIL import Image
import urllib.request
import RPi.GPIO as GPIO
import ssl

ssl._create_default_https_context = ssl._create_unverified_context


class MainWindow:
    def __init__(self):

        self.selected_drink = ""
        self.payment_accepted = False
        self.current_venmo_ID = None
        with open(self.bartender_config_path, "r") as bartender_config:
            config = yaml.safe_load(bartender_config)
            self.passcode = str(config["settings_passcode"])
        # setup
        self.main_win = QMainWindow()
        self.ui = Ui_main()
        self.ui.setupUi(self.main_win)
        # window title and icon
        self.main_win.setWindowTitle("Automatic Bartender")
        # main page
        self.ui.stacked_widg.setCurrentWidget(self.ui.MainScreen)
        self.ui.start_button.clicked.connect(self.showDrinksPage)
        # select drink page
        self.ui.select_drink_back.clicked.connect(self.showMainPage)
        self.ui.make_drink_button.clicked.connect(self.showMakingDrinkPage)
        # making drink page
        self.ui.making_drink_cancel.clicked.connect(self.handleCancelDrink)
        # settings page
        self.ui.home_settings.clicked.connect(self.show_settings_auth_page)
        self.ui.settings_submit.clicked.connect(self.verify_settings_auth)
        self.ui.settings_back.clicked.connect(self.showMainPage)
        self.ui.settings_auth_back.clicked.connect(self.showMainPage)
        # settings start prime
        self.ui.start_prime1.clicked.connect(lambda: self.handle_prime(1, pump_on=True))
        self.ui.start_prime2.clicked.connect(lambda: self.handle_prime(2, pump_on=True))
        self.ui.start_prime3.clicked.connect(lambda: self.handle_prime(3, pump_on=True))
        self.ui.start_prime4.clicked.connect(lambda: self.handle_prime(4, pump_on=True))
        self.ui.start_prime5.clicked.connect(lambda: self.handle_prime(5, pump_on=True))
        self.ui.start_prime6.clicked.connect(lambda: self.handle_prime(6, pump_on=True))
        # settings stop prime
        self.ui.stop_prime1.clicked.connect(lambda: self.handle_prime(1, pump_on=False))
        self.ui.stop_prime2.clicked.connect(lambda: self.handle_prime(2, pump_on=False))
        self.ui.stop_prime3.clicked.connect(lambda: self.handle_prime(3, pump_on=False))
        self.ui.stop_prime4.clicked.connect(lambda: self.handle_prime(4, pump_on=False))
        self.ui.stop_prime5.clicked.connect(lambda: self.handle_prime(5, pump_on=False))
        self.ui.stop_prime6.clicked.connect(lambda: self.handle_prime(6, pump_on=False))
        # settings clean all
        self.ui.clean_system_button.clicked.connect(self.startPumps)
        self.ui.cancel_clean_button.clicked.connect(self.stopPumps)
        # drink levels
        self.ui.drink_levels_button.clicked.connect(self.show_levels_page)
        self.ui.levels_back_button.clicked.connect(self.showSettingsPage)
        # venmo page
        self.ui.venmo_back.clicked.connect(self.handleCancelVenmo)
        # post venmo page
        self.ui.post_venmo_home_button.clicked.connect(self.showMainPage)
        # cancel drink event
        self.drink_event = Event()
        # cancel venmo event
        self.venmo_event = Event()
        # venmo qr init
        qr_code = QPixmap("icons/jimmy_venmo_code.png")
        self.ui.qr_label.setPixmap(qr_code)
        self.ui.qr_label.show()
        # making drink gif
        movie = QMovie("icons/drink_loading_green.gif")
        self.ui.animation_label.setMovie(movie)
        movie.start()
        # gpio init
        self.GPIO = GPIO
        self.GPIO.setmode(GPIO.BOARD)
        self.pump1 = 40
        self.pump2 = 37
        self.pump3 = 35
        self.pump4 = 33
        self.pump5 = 31
        self.pump6 = 29
        self.GPIO.setup(self.pump1, GPIO.OUT)
        self.GPIO.setup(self.pump2, GPIO.OUT)
        self.GPIO.setup(self.pump3, GPIO.OUT)
        self.GPIO.setup(self.pump4, GPIO.OUT)
        self.GPIO.setup(self.pump5, GPIO.OUT)
        self.GPIO.setup(self.pump6, GPIO.OUT)
        self.all_pumps = [
            self.pump1,
            self.pump2,
            self.pump3,
            self.pump4,
            self.pump5,
            self.pump6,
        ]
        # init all pumps to off
        self.stopPumps()
        self.bartender_config_path = ".config_bartender.yaml"

    def show_settings_auth_page(self):
        self.ui.stacked_widg.setCurrentWidget(self.ui.settings_auth)

    def show_levels_page(self):
        self.ui.stacked_widg.setCurrentWidget(self.ui.drink_levels)
        with open(self.bartender_config_path, "r") as bartender_config:
            config = yaml.safe_load(bartender_config)
            self.ui.pump1_level.setText(str(config["pump1"]))
            self.ui.pump2_level.setText(str(config["pump2"]))
            self.ui.pump3_level.setText(str(config["pump3"]))
            self.ui.pump4_level.setText(str(config["pump4"]))
            self.ui.pump5_level.setText(str(config["pump5"]))
            self.ui.pump6_level.setText(str(config["pump6"]))

    def show(self):
        self.main_win.show()

    def showMainPage(self):
        self.ui.stacked_widg.setCurrentWidget(self.ui.MainScreen)
        self.event = Event()

    def showDrinksPage(self):
        self.ui.stacked_widg.setCurrentWidget(self.ui.DrinkSelection)

    def showMakingDrinkPage(self):
        if self.ui.venmo_required_checkbox.isChecked() and not self.payment_accepted:
            # read venmo code id
            with open(self.bartender_config_path, "r") as bartender_config:
                config = yaml.safe_load(bartender_config)
                self.current_venmo_ID = str(config["transaction_id"])
                self.ui.venmo_code_id.setText(self.current_venmo_ID)
            self.ui.stacked_widg.setCurrentWidget(self.ui.venmo)
            transaction_thread = threading.Thread(target=self.check_venmo_transaction)
            transaction_thread.start()
        else:
            self.ui.stacked_widg.setCurrentWidget(self.ui.makingDrink)
            try:
                self.selected_drink = self.ui.drink_list.currentItem().text()
                make_drink_thread = threading.Thread(
                    target=self.makeDrink, args=(self.selected_drink,)
                )
                make_drink_thread.start()
                self.payment_accepted = False
            except AttributeError:
                self.ui.stacked_widg.setCurrentWidget(self.ui.DrinkSelection)

    def making_drink_cancel(self):
        self.ui.stacked_widg.setCurrentWidget(self.ui.MainScreen)

    def showSettingsPage(self):
        self.ui.stacked_widg.setCurrentWidget(self.ui.settings)
        self.ui.settings_back.clicked.connect(self.showMainPage)

    def handleCancelDrink(self):
        self.drink_event.set()
        self.stopPumps()
        if self.ui.venmo_required_checkbox.isChecked():
            self.ui.stacked_widg.setCurrentWidget(self.ui.PostVenmo)
        else:
            self.ui.stacked_widg.setCurrentWidget(self.ui.MainScreen)

    def handleCancelVenmo(self):
        self.venmo_event.set()
        self.ui.stacked_widg.setCurrentWidget(self.ui.MainScreen)

    def check_venmo_transaction(self):
        self.venmo_event = Event()
        with open(self.bartender_config_path) as bartender_config:
            config = yaml.safe_load(bartender_config)
        transaction_id = str(config["transaction_id"])
        while not self.venmo_event.is_set():
            print("checking venmo account")
            if self.check_account(transaction_id) == 1:
                self.showMakingDrinkPage()
                with open(self.bartender_config_path) as bartender_config:
                    config = yaml.safe_load(bartender_config)
                config["transaction_id"] = str(int(self.current_venmo_ID) + 1)
                with open(self.bartender_config_path, "w") as f:
                    yaml.safe_dump(config, f)
                break
            elif self.check_account(transaction_id) == 0:
                with open(self.bartender_config_path) as bartender_config:
                    config = yaml.safe_load(bartender_config)
                config["transaction_id"] = str(int(self.current_venmo_ID) + 1)
                with open(self.bartender_config_path, "w") as f:
                    yaml.safe_dump(config, f)
                self.ui.stacked_widg.setCurrentWidget(self.ui.MainScreen)
                break

    def check_account(self, transaction_id):
        headers = CaseInsensitiveDict()
        with open(self.bartender_config_path) as bartender_config:
            config = yaml.safe_load(bartender_config)
        headers["Authorization"] = str(config["auth_token"])
        headers["User-Agent"] = str(config["user_agent"])
        json_data = json.loads(
            requests.get(str(config["venmo_endpoint"]), headers=headers).text
        )
        venmo_data = json_data["data"]
        for venmo_data_element in venmo_data:
            if venmo_data_element["note"] == transaction_id:
                amount = float(venmo_data_element["payment"]["amount"])
                if amount >= 2:
                    profile_pic_url = venmo_data_element["payment"]["actor"][
                        "profile_picture_url"
                    ]
                    display_name = venmo_data_element["payment"]["actor"][
                        "display_name"
                    ]
                    displayed_name = f"{display_name.split()[0]}!"
                    self.ui.post_venmo_name_label.setText(displayed_name)
                    no_image_url = "https://s3.amazonaws.com/venmo/no-image.gif"
                    if profile_pic_url != no_image_url:
                        temp_profile_pic_path = "temp/temp_profile.png"
                        with urllib.request.urlopen(profile_pic_url) as url:
                            with open(temp_profile_pic_path, "wb") as f:
                                f.write(url.read())
                        img = Image.open(temp_profile_pic_path)
                        new_img = img.resize((311, 221))
                        new_img.save(temp_profile_pic_path, "png", optimize=True)
                        profile_image = QPixmap(temp_profile_pic_path)
                        self.ui.venmo_profile_pic.setPixmap(profile_image)
                        self.ui.qr_label.show()
                    self.payment_accepted = True
                    return 1
                else:
                    return 0

    def verify_settings_auth(self):
        entered_passcode = (
            f"{self.ui.pass_val_1.currentText()}"
            f"{self.ui.pass_val_2.currentText()}"
            f"{self.ui.pass_val_3.currentText()}"
            f"{self.ui.pass_val_4.currentText()}"
        )
        if entered_passcode == self.passcode:
            self.showSettingsPage()
            self.ui.pass_val_1.setCurrentText("1")
            self.ui.pass_val_2.setCurrentText("1")
            self.ui.pass_val_3.setCurrentText("1")
            self.ui.pass_val_4.setCurrentText("1")
        else:
            print(entered_passcode)
            print(self.passcode)
            self.showMainPage()

    def pump_dispense_timer(self, pump_number, duration):
        t_end = time.time() + duration
        while time.time() < t_end:
            self.GPIO.output(pump_number, True)
            if self.drink_event.is_set():
                return
        self.GPIO.output(pump_number, False)

    ############## drink making #############
    def makeDrink(self, drink_selection):
        self.drink_event = Event()
        print(drink_selection)
        is_ice_added = self.ui.ice_in_cup_checkbox.isChecked()
        one_fl_oz = 0.6
        drink_limit = 0.5 if is_ice_added else 1
        print(drink_selection)
        if drink_selection == "Margarita":
            # teq mix
            self.pump_dispense_timer(
                pump_number=self.pump1, duration=10.5 * one_fl_oz * drink_limit
            )
            # teq
            self.pump_dispense_timer(
                pump_number=self.pump3, duration=3.5 * one_fl_oz * drink_limit
            )

        if drink_selection == "Tequila Sunrise":
            # oj
            self.pump_dispense_timer(
                pump_number=self.pump5, duration=8.5 * one_fl_oz * drink_limit
            )
            # cran
            self.pump_dispense_timer(
                pump_number=self.pump2, duration=3.5 * one_fl_oz * drink_limit
            )
            # teq
            self.pump_dispense_timer(
                pump_number=self.pump3, duration=2 * one_fl_oz * drink_limit
            )

        if not self.ui.venmo_required_checkbox.isChecked():
            self.ui.stacked_widg.setCurrentWidget(self.ui.MainScreen)
        else:
            self.ui.stacked_widg.setCurrentWidget(self.ui.PostVenmo)

    def startPumps(self):
        for pump in self.all_pumps:
            self.GPIO.output(pump, True)

    def stopPumps(self):
        for pump in self.all_pumps:
            self.GPIO.output(pump, False)

    def handle_prime(self, pump_number, pump_on):
        if pump_number == 1:
            self.GPIO.output(self.pump1, pump_on)
        elif pump_number == 2:
            self.GPIO.output(self.pump2, pump_on)
        elif pump_number == 3:
            self.GPIO.output(self.pump3, pump_on)
        elif pump_number == 4:
            self.GPIO.output(self.pump4, pump_on)
        elif pump_number == 5:
            self.GPIO.output(self.pump5, pump_on)
        elif pump_number == 6:
            self.GPIO.output(self.pump6, pump_on)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())
