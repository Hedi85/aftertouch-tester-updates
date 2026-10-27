import math
import os
import sys
from PySide2 import QtCore, QtGui
from PySide2.QtCore import QPropertyAnimation
from PySide2.QtWidgets import QSizeGrip, QMessageBox
from interfaceAffichage import *
from fileini import MidiApp
from midi_listener import MidiListener
from MidiSender import Midisender
from qt_material import apply_stylesheet

from PySide2.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton
from PySide2.QtCore import Qt
import pandas as pd
import datetime
import serial
import openpyxl
from openpyxl.styles import Alignment
from functools import partial
from updater import check_for_updates

BAUD_RATE = 9600

class SerialScannerDialog(QDialog):
    """Serial scanner window to capture the QR code via COM port."""

    def __init__(self, main_window, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Scan QR Code (Serial Scanner)")
        self.setFixedSize(400, 200)
        self.setWindowFlags(Qt.WindowTitleHint | Qt.CustomizeWindowHint)  # Disable Close Button (X)

        layout = QVBoxLayout()

        self.label = QLabel("Waiting for scan...")
        layout.addWidget(self.label)

        self.qr_code_input = QLineEdit(self)
        self.qr_code_input.setPlaceholderText("Waiting for scanner input...")
        self.qr_code_input.setAlignment(Qt.AlignCenter)
        self.qr_code_input.setReadOnly(True)  # User can't type manually
        layout.addWidget(self.qr_code_input)

        self.setLayout(layout)

        # Get the MainWindow instance and Serial Port
        self.main_window = main_window
        self.serial_port = self.main_window.serial_port  #  Load port from MainWindow

        # Use or create a serial connection in MainWindow
        if self.main_window.serial_conn and self.main_window.serial_conn.is_open:
            self.serial_conn = self.main_window.serial_conn  # Use existing connection
            print(f" Using existing serial connection on {self.serial_port}.")
        else:
            try:
                self.serial_conn = serial.Serial(self.serial_port, BAUD_RATE, timeout=1)
                self.main_window.serial_conn = self.serial_conn  # Store in MainWindow
                print(f" Serial connection opened on {self.serial_port}.")
            except serial.SerialException as e:
                self.label.setText(f"Serial Error: {e}")
                self.label.setStyleSheet("color: red; font-weight: bold;")
                self.serial_conn = None

        # Timer to check the scanner every 500ms
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.read_serial_data)
        self.timer.start(500)

        # Variable to store scanned serial number
        self.serial_number = None

    def read_serial_data(self):
        """Reads serial input from the scanner and automatically closes when scanned."""
        if self.serial_conn and self.serial_conn.is_open:
            scanned_data = self.serial_conn.readline().decode("utf-8").strip()
            if scanned_data:
                print(f"Scanned: {scanned_data}")
                self.qr_code_input.setText(scanned_data)
                self.serial_number = scanned_data  # Store the serial number
                self.timer.stop()
                self.serial_conn.close()
                self.accept()  # Automatically close window

    def get_serial_number(self):
        """Return the scanned serial number."""
        return self.serial_number

class BackgroundLoader(QThread):
    """Thread to load the UI in the background."""
    loading_finished = Signal(Ui_MainWindow)

    def __init__(self, midi_app):
        super().__init__()
        self.midi_app = midi_app  # Pass MIDI settings

    def run(self):
        ui = Ui_MainWindow()
        self.loading_finished.emit(ui)  # Send the loaded UI


class LoadingScreen(QDialog):
    """Loading screen with a progress indicator."""

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Loading...")
        self.setFixedSize(400, 200)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowTitleHint)

        layout = QVBoxLayout()

        self.label = QLabel("Initializing Application...", self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("font-size: 18px; font-weight: bold; color: white;")

        self.progress = QProgressBar(self)
        self.progress.setRange(0, 100)
        self.progress.setAlignment(Qt.AlignCenter)
        self.progress.setStyleSheet("""
            QProgressBar {
                border: 2px solid #FF9800;
                border-radius: 5px;
                background-color: #303030;
            }
            QProgressBar::chunk {
                background-color: #FFC107;
                width: 20px;
            }
        """)

        layout.addWidget(self.label)
        layout.addWidget(self.progress)
        self.setLayout(layout)

        # Simulate loading process
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_progress)
        self.progress_value = 0
        self.timer.start(10)  # Adjust speed if necessary

        # Dark theme background
        self.setStyleSheet("background-color: #1E1E1E;")

    def update_progress(self):
        """Increment progress bar and close when finished."""
        self.progress_value += 5
        self.progress.setValue(self.progress_value)

        if self.progress_value >= 100:
            self.timer.stop()
            self.accept()  # Close the loading screen

class MainWindow(QMainWindow):
    update_sliders_signal = Signal(float, float)
    def __init__(self, midi_app):
        super().__init__()

        self.midi_app = midi_app  # Store MIDI settings

        # Show loading screen while loading
        self.loading_screen = LoadingScreen()
        self.loading_screen.show()
        QApplication.processEvents()  # Prevent UI freeze

        # Initialize the background loader
        self.loader_thread = BackgroundLoader(self.midi_app)
        self.loader_thread.loading_finished.connect(self.on_loading_finished)

        # Start the loading process in the background
        self.loader_thread.start()

        # Show a simple loading indicator to user
        self.show_loading_screen()

        self.pending_updates = []  # Store messages for batch processing
        self.update_timer = QTimer(self)
        self.update_timer.timeout.connect(self.apply_pending_updates)
        self.update_timer.start(5)  # Update GUI every 15ms

        if hasattr(self, 'loader_thread'):
            self.loader_thread.setPriority(QThread.HighPriority)

        self.ui.sys_btn.clicked.connect(self.go_to_cmemory_page)
        self.ui.encoder_bnt.clicked.connect(self.go_to_main_page)

    def go_to_cmemory_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.cmemory)

    def go_to_main_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.encoders_buttons)

    def collect_midi_message(self, msg_type, channel, control, value):
        """Collect individual MIDI messages for processing."""
        self.pending_updates.append((msg_type, channel, control, value))

    def apply_pending_updates(self):
        """Optimize message processing."""
        if not self.pending_updates:
            return

        # Process in chunks to avoid UI freeze
        messages = self.pending_updates[:100]  # Process up to 100 messages at once
        del self.pending_updates[:100]

        # Process messages
        for msg_type, channel, control, value in messages:
            if msg_type == "note":
                self.handle_note_on(channel, control, value)
            elif msg_type == "note_off":
                self.handle_note_off(channel, control, value)
            elif msg_type == "aftertouch":
                self.update_aftertouch_value(channel, value)
            elif msg_type == "switch":
                self.update_switch_boxes(channel, control)

    def closeEvent(self, event):
        """Ensure MIDI listener and serial scanner are stopped on exit."""

        self.midi_listener.stop()

        if not self.serial_number:
            event.ignore()  # Prevent closing if no scan
            self.label.setText(" You must scan a QR code first!")
            self.label.setStyleSheet("color: red; font-weight: bold;")
        else:
            event.accept()

        super().closeEvent(event)

    def show_loading_screen(self):
        """Show loading screen while the UI loads."""
        self.loading_screen = LoadingScreen()
        self.loading_screen.exec_()  # Blocks until loading is done

    def on_loading_finished(self, ui):
        # Store the UI and setup it up in the main thread
        self.ui = ui
        self.ui.setupUi(self)  # Setup UI in main thread (SAFE)
        self.loading_screen.close()  # Close loading screen
        #FROM HERE the thread of loading (HEDI)

        self.ui.file_name.setText(f"Config: {self.midi_app.config_filename}")

        self.setFixedSize(self.size())
        #self.midi_app = MidiApp()  # Initialize MidiApp instance
        # Start MIDI listener

        self.midi_listener = MidiListener(self.midi_app.tinyusb_port, buffer_size=512)
        self.midi_listener.midi_signal.connect(self.collect_midi_message)
        self.midi_listener.start()

        self.midi_app.midi_sender = Midisender()

        self.serial_port = self.midi_app.get_serial_port()
        self.serial_conn = None
        # Apply styles
        apply_stylesheet(app, theme='light_yellow.xml')
        # Window flags and shadow effect for translucent, frameless window
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        #self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Set window icon and title
        #self.setWindowIcon(QtGui.QIcon("./icons/airplay-svgrepo-com.svg"))
        self.setWindowTitle("StudioLogic")

        QTimer.singleShot(2000, self.run_update_check)

        # Allow window resizing with size grip
        #QSizeGrip(self.ui.size_grip)

        self.ALL_NOTES = set(self.midi_app.selected_notes)

        # Create velocity sliders dynamically for keys (x from 110 to 1640)
        self.sliders_velocity = {}
        x_pos = 120
        slider_style = """
           QSlider::groove:vertical {
                background: #DCDCDC; /* Very light blue for the groove */
                border: 1px solid #D3D3D3; /* Light grey border */
                width: 10px;
                border-radius: 4px;
            }
            QSlider::handle:vertical {
                background: none; /* No handle */
                border: none;
                height: 0px;
                margin: -10px 0;
            }
            QSlider::sub-page:vertical {
                background: #DCDCDC; /* Same color as the groove (invisible at value 0) */
                height: 1px; /* Minimize the height */
                border: none;
            }
            QSlider::add-page:vertical {
                background: #4682B4; /* Darker blue for the inactive area */
                border: none;  
            }
        """

        self.switch_boxes = {}

        for note in range(21, 109):  # 88-key keyboard
            # === VELOCITY SLIDER ===
            slider_name = f"slider_velocity_{note}"
            slider = QSlider(self.ui.encoders_buttons)
            slider.setObjectName(slider_name)
            slider.setOrientation(QtCore.Qt.Vertical)
            slider.setGeometry(x_pos-3, 142, 50, 160)
            slider.setMinimum(0)
            slider.setMaximum(127)
            slider.setValue(0)
            slider.setStyleSheet(slider_style)
            slider.show()
            self.sliders_velocity[note] = slider

            # --- Switch Boxes Above ---
            self.switch_boxes[note] = []
            box_height = 40
            box_spacing = 2
            top_y = 140 - (box_height + box_spacing) * 3  # Place 3 boxes above the slider

            for i in range(3):  # 3 switches
                box = QLabel(self.ui.encoders_buttons)
                box.setFixedSize(15, box_height)  # Match slider width (35)
                box.move(x_pos, top_y + i * (box_height + box_spacing))
                box.setStyleSheet("background-color: white; border: 1px solid black; border-radius: 3px;")
                box.show()
                self.switch_boxes[note].append(box)

            x_pos += 17.5

        # Create min and max velocity indicator lines (only 2 global lines)
        self.min_vel_line = QFrame(self.ui.encoders_buttons)
        self.min_vel_line.setFrameShape(QFrame.HLine)
        self.min_vel_line.setStyleSheet("background-color: black; height: 2px;")

        self.max_vel_line = QFrame(self.ui.encoders_buttons)
        self.max_vel_line.setFrameShape(QFrame.HLine)
        self.max_vel_line.setStyleSheet("background-color: black; height: 2px;")

        # Position the lines initially
        self.update_velocity_lines()

        self.ui.lineEdit_min_vel.textChanged.connect(self.update_velocity_lines)
        self.ui.lineEdit_max_vel.textChanged.connect(self.update_velocity_lines)

        # Window control buttons
        self.ui.min_window_button.clicked.connect(lambda: self.showMinimized())
        self.ui.close_window_button.clicked.connect(lambda: self.close())
        self.ui.max_window_button.clicked.connect(
            lambda: self.showNormal() if self.isMaximized() else self.showMaximized())

        # Apply black border using stylesheet
        self.ui.reset_pushButton.setStyleSheet("""
                                QPushButton {
                                    height: 50px;
                                    width: 200px;
                                    background-color: transparent;
                                    border: 2px solid #252525;
                                    border-radius: 25px;
                                    color: #333;
                                    font-weight: 800;
                                    letter-spacing: 3px;
                                    transition: all 200ms ease-in-out;
                                }
                                
                                QPushButton:hover {
                                    background-color: #333;
                                    color: white;
                                    border: none;
                                }
                                
                                QPushButton:pressed {
                                    background-color: #555;
                                    color: #fff;
                                    transform: scale(0.97);
                                }

               """)
        self.ui.newdevice2.setStyleSheet("""
                           QPushButton {
                                height: 50px;
                                width: 200px;
                                background-color: transparent;
                                border: 2px solid #252525;
                                border-radius: 25px;
                                color: #333;
                                font-weight: 800;
                                letter-spacing: 3px;
                                transition: all 200ms ease-in-out;
                            }
                            
                            QPushButton:hover {
                                background-color: #333;
                                color: white;
                                border: none;
                            }
                            
                            QPushButton:pressed {
                                background-color: #555;
                                color: #fff;
                                transform: scale(0.97);
                            }

                       """)

        self.ui.new_file_ini.setStyleSheet("""
                                   QPushButton {
                                        height: 50px;
                                        width: 200px;
                                        background-color: transparent;
                                        border: 2px solid #252525;
                                        border-radius: 25px;
                                        color: #333;
                                        font-weight: 800;
                                        letter-spacing: 3px;
                                        transition: all 200ms ease-in-out;
                                    }
                                    
                                    QPushButton:hover {
                                        background-color: #333;
                                        color: white;
                                        border: none;
                                    }
                                    
                                    QPushButton:pressed {
                                        background-color: #555;
                                        color: #fff;
                                        transform: scale(0.97);
                                    }

                               """)

        # Set the initial widget in the stackedWidget
        self.ui.stackedWidget.setCurrentWidget(self.ui.encoders_buttons)

        self.ui.newdevice.clicked.connect(self.load_new_device_config)
        self.ui.new_file_ini.clicked.connect(self.load_new_device_config)
        self.ui.newdevice2.clicked.connect(self.restart_device)
        self.ui.reset_pushButton.clicked.connect(self.reset_device)

        self.ui.radioAcoustic.toggled.connect(self.on_radio_acoustic_toggled)
        self.ui.radioElectrical.toggled.connect(self.on_radio_electrical_toggled)

        self.ui.two_sw.toggled.connect(self.on_two_sw_toggled)
        self.ui.three_sw.toggled.connect(self.on_three_sw_toggled)

        #        self.midi_app.start_midi_listener(self.update_midi_controls)
        self.key_number = self.midi_app.key_number  # Retrieve key number from MidiApp
        self.cached_vmin = self.voltage_to_8bit_range(self.midi_app.at_vmin)
        self.cached_vmax = self.voltage_to_8bit_range(self.midi_app.at_vmax)
        self.cached_exp = self.midi_app.at_exp
        self.black_gain = self.midi_app.black_gain
        self.white_gain = self.midi_app.white_gain

        # Set values from .ini into the UI fields
        self.ui.lineEdit_ratio.setText(str(self.midi_app.ratio))
        self.ui.lineEdit_ratio_black.setText(str(self.midi_app.ratio_black))
        self.ui.lineEdit_ratio_white.setText(str(self.midi_app.ratio_white))
        self.ui.lineEdit_min_vel.setText(str(self.midi_app.min_velocity))
        self.ui.lineEdit_max_vel.setText(str(self.midi_app.max_velocity))
        self.ui.lineEdit_min_RES.setText(str(self.midi_app.min_resistance))
        self.ui.lineEdit_max_RES.setText(str(self.midi_app.max_resistance))
        self.ui.lineEdit_counter_period.setText(str(self.midi_app.counter))
        self.ui.label_weight.setText(str(self.midi_app.weight) + " g")

        self.ui.checkBoxresplit.setChecked(self.midi_app.split_enabled)
        self.ui.scan_nogoodkeyboards.setChecked(self.midi_app.scan_no_good_enabled)
        self.ui.checkBox_notimer.setChecked(self.midi_app.notimer_enabled)

        self.ui.lineEdit_user_max.setText(str(self.midi_app.at_vmax))
        self.ui.lineEdit_user_min.setText(str(self.midi_app.at_vmin))

        if self.midi_app.mode == "acoustic":
            self.ui.radioAcoustic.setChecked(True)
        elif self.midi_app.mode == "electrical":
            self.ui.radioElectrical.setChecked(True)

        if self.midi_app.switches == 2:
            self.ui.two_sw.setChecked(True)
        elif self.midi_app.switches == 3:
            self.ui.three_sw.setChecked(True)

        # --- Load test mode from INI file ---
        mode = self.midi_app.test_mode.lower()

        if mode == "dynamic":
            self.ui.dynamic_radio.setChecked(True)
        elif mode == "aft":
            self.ui.aft_radio.setChecked(True)
        elif mode == "full":
            self.ui.full_radio.setChecked(True)
        else:
            # fallback if invalid
            self.ui.dynamic_radio.setChecked(True)

        # Store internal state
        self.mode = mode

        self.ui.dynamic_radio.toggled.connect(self.on_dynamic_mode)
        self.ui.aft_radio.toggled.connect(self.on_aft_mode)
        self.ui.full_radio.toggled.connect(self.on_full_mode)
        #self.ui.lineEdit_user_max.setText(f" {self.midi_app.at_vmax:.2f}")
        #self.ui.lineEdit_user_min.setText(f" {self.midi_app.at_vmin:.2f}")

        #self.ui.radioElectrical.setChecked(True)

        self.retry_mode = False
        self.test_passed = True
        self.resistance_timers = {}
        self.note_remaining_times = {}
        self.note_retry_mode = {}
        self.current_display_note = None

        self.last_resistance_per_key = {}
        self.latest_resistance_values = {}
        self.resistance_values = {}
        self.global_min_resistance = None
        self.processed_keys = set()
        self.total_keys = 88
        self.resistance_timer = None

        self.slider_max_values = {}
        self.note_to_label_map = self.create_note_to_label_map()
        self.note_to_editline_map = self.create_note_to_editline_map()
        #self.display_output_level()
        self.all_tests_passed_notified = False
        self.notes_test_passed_notified = False

        self.note_pressed = False
        self.current_slider = None

        self.ui.exponent_slider.valueChanged.connect(self.update_exponent)
        self.ui.v_gain_slider.valueChanged.connect(self.update_curve_value_white)
        self.ui.v_gain_slider_2.valueChanged.connect(self.update_curve_value_black)
        self.curve_value = self.ui.v_gain_slider.value()
        self.curve_value_2 = self.ui.v_gain_slider_2.value()
        self.exponent_value = 1.0

        self.test_started = False

        self.no_timer_min_values = {}

        self.ui.lineEdit_ratio.textChanged.connect(self.compare_resistances)

        self.note_to_buttons_map = self.create_note_to_buttons_map()
        for note, button in self.note_to_buttons_map.items():
            if note in self.ALL_NOTES:
                button.setChecked(True)
            else:
                button.setChecked(False)
        self.update_button_styles_based_on_selection()
        self.update_aftertouch_slider_borders_based_on_selection()
        self.save_selected_notes()
        for note, button in self.note_to_buttons_map.items():
            button.toggled.connect(partial(self.handle_note_toggle, note=note))

        # Restore selected keys from .ini file
        self.selected_notes = set(self.midi_app.selected_notes)  # Loaded from ini
        for note in self.selected_notes:
            btn = self.note_to_buttons_map.get(note)
            if btn:
                btn.setChecked(True)

        # Also update ALL_NOTES to match
        if self.selected_notes:
            self.ALL_NOTES = self.selected_notes.copy()
        else:
            self.ALL_NOTES = set(self.note_to_buttons_map.keys())

        # Initialize ALL_NOTES based on key_number
        self.ALL_NOTES = set(self.note_to_label_map.keys())
        self.played_notes = set()
        self.slider_good = {}
        self.velocity_ok = {}
        self.full_velocity_ok = {}

        #self.selected_notes = set()

        #self.ui.save_notes.clicked.connect(self.save_selected_notes)
        self.ui.clear_notes.clicked.connect(self.clear_selected_notes)
        self.ui.select_all.clicked.connect(self.select_all_notes)

        def moveWindow(e):
            if not self.isMaximized():
                if e.buttons() == QtCore.Qt.LeftButton:
                    self.move(self.pos() + e.globalPos() - self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()

        self.ui.heade_frame.mouseMoveEvent = moveWindow
        self.ui.open_close_side_bar_btn.clicked.connect(self.slideLeftMenu)

        #self.populate_midi_ports()
        #self.ui.connect_btn.clicked.connect(self.start_midi_listener)
        self.midi_listener_thread = None
        # Show the window
        self.show()

    # Mouse press event to capture initial click position
    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()

    # Slide left menu animation
    def slideLeftMenu(self):
        width = self.ui.left_menu_frame.width()

        # Determine new width
        newWidth = 200 if width == 50 else 50

        # Set up animation for sliding menu
        self.animation = QPropertyAnimation(self.ui.left_menu_frame, b"minimumWidth")
        self.animation.setDuration(250)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()


    def get_start_note_for_format(self):
        """Return the start note based on the keyboard format."""
        if self.key_number == 88:
            return 21  # Standard for 88-key keyboards (A0)
        elif self.key_number == 73:
            return 28  # Common starting note for 73 keys (E1)
        elif self.key_number == 61:
            return 36  # Common starting note for 61 keys (C2)
        else:
            raise ValueError("Unsupported key number.")

    def create_note_to_label_map(self):
        """Create a note-to-label map based on the selected key range."""
        # Full 88-key mapping
        full_note_to_label_map = {
            21: self.ui.verticalSlider,
            22: self.ui.verticalSlider_3,
            23: self.ui.verticalSlider_2,
            24: self.ui.verticalSlider_4,
            25: self.ui.verticalSlider_54,
            26: self.ui.verticalSlider_5,
            27: self.ui.verticalSlider_55,
            28: self.ui.verticalSlider_6,
            29: self.ui.verticalSlider_7,
            30: self.ui.verticalSlider_56,
            31: self.ui.verticalSlider_8,
            32: self.ui.verticalSlider_57,
            33: self.ui.verticalSlider_9,
            34: self.ui.verticalSlider_58,
            35: self.ui.verticalSlider_10,
            36: self.ui.verticalSlider_11,
            37: self.ui.verticalSlider_59,
            38: self.ui.verticalSlider_12,
            39: self.ui.verticalSlider_60,
            40: self.ui.verticalSlider_13,
            41: self.ui.verticalSlider_14,
            42: self.ui.verticalSlider_61,
            43: self.ui.verticalSlider_15,
            44: self.ui.verticalSlider_62,
            45: self.ui.verticalSlider_16,
            46: self.ui.verticalSlider_63,
            47: self.ui.verticalSlider_17,
            48: self.ui.verticalSlider_18,
            49: self.ui.verticalSlider_64,
            50: self.ui.verticalSlider_19,
            51: self.ui.verticalSlider_65,
            52: self.ui.verticalSlider_20,
            53: self.ui.verticalSlider_21,
            54: self.ui.verticalSlider_66,
            55: self.ui.verticalSlider_22,
            56: self.ui.verticalSlider_67,
            57: self.ui.verticalSlider_23,
            58: self.ui.verticalSlider_68,
            59: self.ui.verticalSlider_24,
            60: self.ui.verticalSlider_25,
            61: self.ui.verticalSlider_69,
            62: self.ui.verticalSlider_26,
            63: self.ui.verticalSlider_70,
            64: self.ui.verticalSlider_27,
            65: self.ui.verticalSlider_28,
            66: self.ui.verticalSlider_71,
            67: self.ui.verticalSlider_29,
            68: self.ui.verticalSlider_72,
            69: self.ui.verticalSlider_30,
            70: self.ui.verticalSlider_73,
            71: self.ui.verticalSlider_31,
            72: self.ui.verticalSlider_32,
            73: self.ui.verticalSlider_74,
            74: self.ui.verticalSlider_33,
            75: self.ui.verticalSlider_75,
            76: self.ui.verticalSlider_34,
            77: self.ui.verticalSlider_35,
            78: self.ui.verticalSlider_76,
            79: self.ui.verticalSlider_36,
            80: self.ui.verticalSlider_77,
            81: self.ui.verticalSlider_37,
            82: self.ui.verticalSlider_78,
            83: self.ui.verticalSlider_38,
            84: self.ui.verticalSlider_39,
            85: self.ui.verticalSlider_79,
            86: self.ui.verticalSlider_40,
            87: self.ui.verticalSlider_80,
            88: self.ui.verticalSlider_41,
            89: self.ui.verticalSlider_42,
            90: self.ui.verticalSlider_81,
            91: self.ui.verticalSlider_43,
            92: self.ui.verticalSlider_82,
            93: self.ui.verticalSlider_44,
            94: self.ui.verticalSlider_83,
            95: self.ui.verticalSlider_45,
            96: self.ui.verticalSlider_46,
            97: self.ui.verticalSlider_84,
            98: self.ui.verticalSlider_47,
            99: self.ui.verticalSlider_85,
            100: self.ui.verticalSlider_48,
            101: self.ui.verticalSlider_49,
            102: self.ui.verticalSlider_86,
            103: self.ui.verticalSlider_50,
            104: self.ui.verticalSlider_87,
            105: self.ui.verticalSlider_51,
            106: self.ui.verticalSlider_88,
            107: self.ui.verticalSlider_52,
            108: self.ui.verticalSlider_53
        }

        # Get the start and end note for the selected key range
        start_note = self.get_start_note_for_format()
        end_note = start_note + self.key_number - 1

        # Slice the dictionary to only include the required range
        return {note: label for note, label in full_note_to_label_map.items() if start_note <= note <= end_note}

    def create_note_to_editline_map(self):
        """Create a note-to-editline map based on the selected key range."""
        # Full 88-key mapping for edit lines
        full_note_to_editline_map = {
            21: self.ui.lineEdit_3,
            22: self.ui.lineEdit_58,
            23: self.ui.lineEdit_7,
            24: self.ui.lineEdit_8,
            25: self.ui.lineEdit_59,
            26: self.ui.lineEdit_9,
            27: self.ui.lineEdit_60,
            28: self.ui.lineEdit_10,
            29: self.ui.lineEdit_11,
            30: self.ui.lineEdit_61,
            31: self.ui.lineEdit_12,
            32: self.ui.lineEdit_62,
            33: self.ui.lineEdit_13,
            34: self.ui.lineEdit_63,
            35: self.ui.lineEdit_14,
            36: self.ui.lineEdit_15,
            37: self.ui.lineEdit_64,
            38: self.ui.lineEdit_16,
            39: self.ui.lineEdit_65,
            40: self.ui.lineEdit_17,
            41: self.ui.lineEdit_18,
            42: self.ui.lineEdit_66,
            43: self.ui.lineEdit_19,
            44: self.ui.lineEdit_67,
            45: self.ui.lineEdit_20,
            46: self.ui.lineEdit_68,
            47: self.ui.lineEdit_21,
            48: self.ui.lineEdit_22,
            49: self.ui.lineEdit_69,
            50: self.ui.lineEdit_23,
            51: self.ui.lineEdit_70,
            52: self.ui.lineEdit_24,
            53: self.ui.lineEdit_25,
            54: self.ui.lineEdit_71,
            55: self.ui.lineEdit_26,
            56: self.ui.lineEdit_72,
            57: self.ui.lineEdit_27,
            58: self.ui.lineEdit_73,
            59: self.ui.lineEdit_28,
            60: self.ui.lineEdit_29,
            61: self.ui.lineEdit_74,
            62: self.ui.lineEdit_30,
            63: self.ui.lineEdit_75,
            64: self.ui.lineEdit_31,
            65: self.ui.lineEdit_32,
            66: self.ui.lineEdit_76,
            67: self.ui.lineEdit_33,
            68: self.ui.lineEdit_77,
            69: self.ui.lineEdit_34,
            70: self.ui.lineEdit_78,
            71: self.ui.lineEdit_35,
            72: self.ui.lineEdit_36,
            73: self.ui.lineEdit_79,
            74: self.ui.lineEdit_37,
            75: self.ui.lineEdit_80,
            76: self.ui.lineEdit_38,
            77: self.ui.lineEdit_39,
            78: self.ui.lineEdit_81,
            79: self.ui.lineEdit_40,
            80: self.ui.lineEdit_82,
            81: self.ui.lineEdit_41,
            82: self.ui.lineEdit_83,
            83: self.ui.lineEdit_42,
            84: self.ui.lineEdit_43,
            85: self.ui.lineEdit_84,
            86: self.ui.lineEdit_44,
            87: self.ui.lineEdit_85,
            88: self.ui.lineEdit_45,
            89: self.ui.lineEdit_46,
            90: self.ui.lineEdit_86,
            91: self.ui.lineEdit_47,
            92: self.ui.lineEdit_87,
            93: self.ui.lineEdit_48,
            94: self.ui.lineEdit_88,
            95: self.ui.lineEdit_49,
            96: self.ui.lineEdit_50,
            97: self.ui.lineEdit_89,
            98: self.ui.lineEdit_51,
            99: self.ui.lineEdit_90,
            100: self.ui.lineEdit_52,
            101: self.ui.lineEdit_53,
            102: self.ui.lineEdit_91,
            103: self.ui.lineEdit_54,
            104: self.ui.lineEdit_92,
            105: self.ui.lineEdit_55,
            106: self.ui.lineEdit_93,
            107: self.ui.lineEdit_56,
            108: self.ui.lineEdit_57
        }
        # Get the start and end note for the selected key range
        start_note = self.get_start_note_for_format()
        end_note = start_note + self.key_number - 1

        # Slice the dictionary to only include the required range
        return {note: editline for note, editline in full_note_to_editline_map.items() if
                start_note <= note <= end_note}


    def create_note_to_buttons_map(self):
        """Create a note-to-editline map based on the selected key range."""
        # Full 88-key mapping for buttons
        full_note_to_buttons_map = {
            21: self.ui.a4_21,
            22: self.ui.a40_21,
            23: self.ui.b4_21,
            24: self.ui.c4_18,
            25: self.ui.c40_18,
            26: self.ui.d4_18,
            27: self.ui.d40_18,
            28: self.ui.e4_18,
            29: self.ui.f4_18,
            30: self.ui.f40_18,
            31: self.ui.g4_18,
            32: self.ui.g40_18,
            33: self.ui.a4_20,
            34: self.ui.a40_20,
            35: self.ui.b4_20,
            36: self.ui.c4_17,
            37: self.ui.c40_17,
            38: self.ui.d4_17,
            39: self.ui.d40_17,
            40: self.ui.e4_17,
            41: self.ui.f4_17,
            42: self.ui.f40_17,
            43: self.ui.g4_17,
            44: self.ui.g40_17,
            45: self.ui.a4_19,
            46: self.ui.a40_19,
            47: self.ui.b4_19,
            48: self.ui.c4_16,
            49: self.ui.c40_16,
            50: self.ui.d4_16,
            51: self.ui.d40_16,
            52: self.ui.e4_16,
            53: self.ui.f4_16,
            54: self.ui.f40_16,
            55: self.ui.g4_16,
            56: self.ui.g40_16,
            57: self.ui.a4_18,
            58: self.ui.a40_18,
            59: self.ui.b4_18,
            60: self.ui.c4_15,
            61: self.ui.c40_15,
            62: self.ui.d4_15,
            63: self.ui.d40_15,
            64: self.ui.e4_15,
            65: self.ui.f4_15,
            66: self.ui.f40_15,
            67: self.ui.g4_15,
            68: self.ui.g40_15,
            69: self.ui.a4_17,
            70: self.ui.a40_17,
            71: self.ui.b4_17,
            72: self.ui.c4_14,
            73: self.ui.c40_14,
            74: self.ui.d4_14,
            75: self.ui.d40_14,
            76: self.ui.e4_14,
            77: self.ui.f4_14,
            78: self.ui.f40_14,
            79: self.ui.g4_14,
            80: self.ui.g40_14,
            81: self.ui.a4_16,
            82: self.ui.a40_16,
            83: self.ui.b4_16,
            84: self.ui.c4_13,
            85: self.ui.c40_13,
            86: self.ui.d4_13,
            87: self.ui.d40_13,
            88: self.ui.e4_13,
            89: self.ui.f4_13,
            90: self.ui.f40_13,
            91: self.ui.g4_13,
            92: self.ui.g40_13,
            93: self.ui.a4_15,
            94: self.ui.a40_15,
            95: self.ui.b4_15,
            96: self.ui.c5_3,
            97: self.ui.c50_3,
            98: self.ui.d5_3,
            99: self.ui.d50_3,
            100: self.ui.e5_3,
            101: self.ui.f5_3,
            102: self.ui.f50_3,
            103: self.ui.g5_3,
            104: self.ui.g50_3,
            105: self.ui.a5_3,
            106: self.ui.a50_3,
            107: self.ui.b5_3,
            108: self.ui.c6_3
        }
        start_note = self.get_start_note_for_format()
        end_note = start_note + self.key_number - 1

        return {
            note: button
            for note, button in full_note_to_buttons_map.items()
            if start_note <= note <= end_note
        }

    def save_selected_notes(self):
        selected_notes = [note for note, button in self.note_to_buttons_map.items() if button.isChecked()]
        self.midi_app.save_selected_keys(selected_notes)
        print(f"Saved selected notes: {selected_notes}")
        self.update_button_styles_based_on_selection()

    def clear_selected_notes(self):
        for button in self.note_to_buttons_map.values():
            button.setChecked(False)  # Uncheck everything
        self.ALL_NOTES = set()  # Empty set means no keys selected
        self.midi_app.save_selected_keys([])  # Save empty list
        self.update_button_styles_based_on_selection()
        print("Cleared all selected keys.")

    def select_all_notes(self):
        for button in self.note_to_buttons_map.values():
            button.setChecked(True)  # Select everything
        self.ALL_NOTES = set(self.note_to_buttons_map.keys())  # Include all keys
        self.midi_app.save_selected_keys(list(self.ALL_NOTES))
        self.update_button_styles_based_on_selection()
        print("All keys selected.")

    def get_aftertouch_slider_style(self, note, is_selected):
        if note % 12 in [1, 3, 6, 8, 10]:  # Black keys
            if is_selected:
                return """
                QSlider::groove:vertical {
                    border: 1px solid black;
                    width: 20px;
                    margin: 0px;
                    background: transparent;
                }
                QSlider::handle:vertical {
                    background: none;
                    width: 20px;
                    height: 0px;
                    margin: -10px 0;
                    border: 1px solid black;
                }
                QSlider::add-page:vertical {
                    background: qlineargradient(
                        spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494,
                        stop:0.85 rgba(0, 150, 0, 250),
                        stop:1 rgba(255, 255, 255, 255)
                    );
                    border: 1px solid black;
                }
                QSlider::sub-page:vertical {
                    background: black;
                    border: 1px solid black;
                }
                """
            else:  # Grey foncé for black key (not selected)
                return """
                QSlider::groove:vertical {
                    border: 1px solid #888888;
                    width: 20px;
                    margin: 0px;
                    background: transparent;
                }
                QSlider::handle:vertical {
                    background: none;
                    width: 20px;
                    height: 0px;
                    margin: -10px 0;
                    border: 1px solid #888888;
                }
                QSlider::add-page:vertical {
                    background: #666666;
                    border: 1px solid #888888;
                }
                QSlider::sub-page:vertical {
                    background: #aaaaaa;
                    border: 1px solid #888888;
                }
                """

        else:  # White keys
            if is_selected:
                return """
                QSlider::groove:vertical {
                    border: 1px solid black;
                    width: 22px;
                    margin: 0px;
                    background-color: transparent;
                }
                QSlider::handle:vertical {
                    background: none;
                    width: 22px;
                    height: 0px;
                    margin: -10px 0;
                    border: 1px solid black;
                }
                QSlider::add-page:vertical {
                    background: qlineargradient(
                        spread:pad, x1:0, y1:1, x2:1, y2:0,
                        stop:0 rgba(255, 200, 0, 255),
                        stop:1 rgba(180, 120, 0, 255)
                    );
                    border: 1px solid black;
                }
                QSlider::sub-page:vertical {
                    background: qlineargradient(
                        spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711,
                        stop:0 rgba(0, 0, 0, 255),
                        stop:1 rgba(255, 255, 255, 255)
                    );
                    border: 1px solid black;
                }
                """
            else:  # Grey clair for white key (not selected)
                return """
                QSlider::groove:vertical {
                    border: 1px solid #BBBBBB;
                    width: 22px;
                    margin: 0px;
                    background: transparent;
                }
                QSlider::handle:vertical {
                    background: none;
                    width: 22px;
                    height: 0px;
                    margin: -10px 0;
                    border: 1px solid #BBBBBB;
                }
                QSlider::add-page:vertical {
                    background: #DDDDDD;
                    border: 1px solid #BBBBBB;
                }
                QSlider::sub-page:vertical {
                    background: #c0c0c0;
                    border: 1px solid #BBBBBB;
                }
                """

    def update_aftertouch_slider_borders_based_on_selection(self):
        for note, slider in self.note_to_label_map.items():
            is_selected = note in self.ALL_NOTES
            slider.setStyleSheet(self.get_aftertouch_slider_style(note, is_selected))

    def update_button_styles_based_on_selection(self):
        """Update button appearance: keep default for selected, greyed out for unselected."""
        for note, button in self.note_to_buttons_map.items():
            if note in self.ALL_NOTES:
                # Restore the original style based on key type
                if note % 12 in [1, 3, 6, 8, 10]:  # black keys
                    button.setStyleSheet("""
                        QPushButton {
                            background-color: rgb(0, 0, 0);
                            background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494,
                                                              stop:0.852273 rgba(0, 0, 0, 250),
                                                              stop:1 rgba(255, 255, 255, 255));
                            border: 1px solid black;
                        }
                        QPushButton:pressed {
                            background-color: rgb(0, 0, 0);
                        }
                    """)
                else:  # white keys
                    button.setStyleSheet("""
                        QPushButton {
                            background-color: rgb(242, 242, 242);
                            background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711,
                                                              stop:0 rgba(0, 0, 0, 255),
                                                              stop:1 rgba(255, 255, 255, 255));
                            border: 1px solid black;
                        }
                        QPushButton:pressed {
                            background-color: rgb(250, 250, 250);
                        }
                    """)
            else:
                # Greyed-out for unselected
                button.setStyleSheet("""
                    QPushButton {
                        background-color: rgba(128, 128, 128, 100);
                        border: 1px solid black;
                        color: #666;
                    }
                """)

    def update_switch_boxes(self, status, note):
        if note not in self.switch_boxes:
            return

        index = status & 0x0F  # Extract 0–5
        color_map = {0: "red", 1: "#005aff", 2: "green"}

        if index in color_map:
            self.switch_boxes[note][index].setStyleSheet(
                f"background-color: {color_map[index]}; border: 1px solid black;")
        elif index in [3, 4, 5]:  # OFFs
            self.switch_boxes[note][index - 3].setStyleSheet("background-color: white; border: 1px solid black;")

    def handle_note_toggle(self, checked, note):
        if checked:
            self.ALL_NOTES.add(note)
        else:
            self.ALL_NOTES.discard(note)

        self.midi_app.save_selected_keys(list(self.ALL_NOTES))
        self.update_button_styles_based_on_selection()
        self.update_aftertouch_slider_borders_based_on_selection()


    def stop_listener_safely(self):
        """Stop MIDI listener completely, ensuring no signals remain."""
        if hasattr(self, 'midi_listener') and self.midi_listener:
            try:
                self.midi_listener.midi_signal.disconnect(self.collect_midi_message)
            except Exception:
                pass

            try:
                self.midi_listener.stop()
            except Exception as e:
                print(f"Error stopping listener: {e}")

            # If it's a threading.Thread, block until finished
            if hasattr(self.midi_listener, "join"):
                try:
                    self.midi_listener.join(timeout=2.0)
                except Exception as e:
                    print(f"Error joining listener: {e}")

            # Remove reference to ensure GC cleans it
            self.midi_listener = None

            # Flush any queued Qt events for midi_signal
            QApplication.processEvents()
            print("Listener fully stopped.")

    def run_update_check(self):
        try:
            check_for_updates()
        except Exception as e:
            print("Update check failed:", e)

    def load_new_device_config(self):
        print(" Selecting New Config File...")

        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Select Configuration File", "", "INI Files (*.ini);;All Files (*)", options=options
        )

        if not file_path:
            print(" No File Selected. Skipping...")
            return

        print(f"Loading Config File: {file_path}")

        # Step 1: Close Serial Connection only (leave MIDI listener running!)
        if hasattr(self, 'serial_conn') and self.serial_conn and self.serial_conn.is_open:
            print("Closing Serial Connection...")
            self.serial_conn.close()
            self.serial_conn = None
            print("Serial Connection Closed.")

        # Step 2: Load Configuration
        self.midi_app.load_config(file_path)

        filename = os.path.basename(file_path)
        self.ui.file_name.setText(f"Config: {filename}")

        # Clear and restore selected keys from INI
        for btn in self.note_to_buttons_map.values():
            btn.blockSignals(True)
            btn.setChecked(False)
            btn.blockSignals(False)

        self.selected_notes = set(self.midi_app.selected_notes)
        for note in self.selected_notes:
            btn = self.note_to_buttons_map.get(note)
            if btn:
                btn.blockSignals(True)
                btn.setChecked(True)
                btn.blockSignals(False)

        self.ALL_NOTES = self.selected_notes.copy() if self.selected_notes else set(self.note_to_buttons_map.keys())

        self.update_button_styles_based_on_selection()
        self.update_aftertouch_slider_borders_based_on_selection()

        # Update key settings from INI
        self.key_number = self.midi_app.key_number
        self.cached_vmin = self.voltage_to_8bit_range(self.midi_app.at_vmin)
        self.cached_vmax = self.voltage_to_8bit_range(self.midi_app.at_vmax)
        self.cached_exp = self.midi_app.at_exp
        self.black_gain = self.midi_app.black_gain
        self.white_gain = self.midi_app.white_gain

        # Update UI fields
        self.ui.lineEdit_ratio.setText(str(self.midi_app.ratio))
        self.ui.lineEdit_ratio_black.setText(str(self.midi_app.ratio_black))
        self.ui.lineEdit_ratio_white.setText(str(self.midi_app.ratio_white))
        self.ui.lineEdit_min_vel.setText(str(self.midi_app.min_velocity))
        self.ui.lineEdit_max_vel.setText(str(self.midi_app.max_velocity))
        self.ui.lineEdit_min_RES.setText(str(self.midi_app.min_resistance))
        self.ui.lineEdit_max_RES.setText(str(self.midi_app.max_resistance))
        self.ui.lineEdit_counter_period.setText(str(self.midi_app.counter))
        self.ui.label_weight.setText(str(self.midi_app.weight) + " g")

        self.ui.checkBoxresplit.setChecked(self.midi_app.split_enabled)
        self.ui.scan_nogoodkeyboards.setChecked(self.midi_app.scan_no_good_enabled)
        self.ui.checkBox_notimer.setChecked(self.midi_app.notimer_enabled)

        # Reset all stored values
        self.last_resistance_per_key.clear()
        self.latest_resistance_values.clear()
        self.resistance_values.clear()
        self.processed_keys.clear()
        self.global_min_resistance = None

        # Reset UI safely
        self.note_to_label_map = self.create_note_to_label_map()
        self.note_to_editline_map = self.create_note_to_editline_map()
        for slider in self.note_to_label_map.values():
            slider.setValue(0)
        for slider in self.sliders_velocity.values():
            slider.setValue(0)
        for note, boxes in self.switch_boxes.items():
            for box in boxes:
                box.setStyleSheet("background-color: white; border: 1px solid black;")
        for editline in self.note_to_editline_map.values():
            if editline:
                editline.setText("")
                editline.setStyleSheet("")

        self.ui.lineEdit_counter_display.setText("")
        self.ui.lineEdit_aftertouch.setText("")
        self.ui.lineEdit_velocity.setText("")
        self.ui.lineEdit_resistance.setText("")
        self.ui.lineEdit_velo.setText("")
        self.ui.lineEdit_note.setText("")
        self.ui.label_message.setText("")

        self.ui.lineEdit_user_max.setText(str(self.midi_app.at_vmax))
        self.ui.lineEdit_user_min.setText(str(self.midi_app.at_vmin))

        QMessageBox.information(self, "New Device Loaded", f"Configuration loaded from {file_path}")
        print("Configuration Reloaded Successfully!")

    def restart_device(self):
        """Restart the MIDI settings and test progress with the current configuration."""

        print("Restarting Device...")

        #  Stop MIDI listeners safely
        if hasattr(self, 'midi_listener') and self.midi_listener.is_running():
            print(" Stopping MIDI Listener...")
            self.midi_listener.stop()
            print(" MIDI Listener Stopped.")

        self.key_number = self.midi_app.key_number  # Ensure the key_number is up-to-date
        self.cached_vmin = self.voltage_to_8bit_range(self.midi_app.at_vmin)
        self.cached_vmax = self.voltage_to_8bit_range(self.midi_app.at_vmax)
        self.cached_exp = self.midi_app.at_exp
        self.black_gain = self.midi_app.black_gain
        self.white_gain = self.midi_app.white_gain

        # Stop & Close Serial Connection (Prevents Blocking Issues)
        if hasattr(self, 'serial_conn') and self.serial_conn and self.serial_conn.is_open:
            print("Closing Serial Connection...")
            self.serial_conn.close()
            self.serial_conn = None
            print(" Serial Connection Closed.")

        # Reset All Stored Resistance Values
        self.last_resistance_per_key.clear()
        self.latest_resistance_values.clear()
        self.resistance_values.clear()
        self.processed_keys.clear()
        self.global_min_resistance = None  # Reset global minimum

        # Restart MIDI Listener Properly
        print(" Restarting MIDI Listener...")
        self.midi_listener = MidiListener(self.midi_app.tinyusb_port, buffer_size=512)
        self.midi_listener.midi_signal.connect(self.collect_midi_message)
        self.midi_listener.start()
        print("MIDI Listener Restarted.")

        # Reset UI Elements
        note_to_label_map = self.create_note_to_label_map()
        for slider in note_to_label_map.values():
            slider.setValue(0)

        for slider in self.sliders_velocity.values():
            slider.setValue(0)

        # Reset switch boxes for each key
        for note, boxes in self.switch_boxes.items():
            for box in boxes:
                box.setStyleSheet("background-color: white; border: 1px solid black;")

        note_to_editline_map = self.create_note_to_editline_map()
        for editline in note_to_editline_map.values():
            if editline:
                editline.setText("")
                editline.setStyleSheet("")

        for timer in self.resistance_timers.values():
            timer.stop()
        self.resistance_timers.clear()
        self.note_remaining_times.clear()
        self.retry_mode = False
        self.test_passed = True
        self.current_display_note = None

        self.ui.lineEdit_counter_display.setText("")
        self.ui.lineEdit_aftertouch.setText('')
        self.ui.lineEdit_velocity.setText('')
        self.ui.lineEdit_resistance.setText('')
        self.ui.lineEdit_velo.setText('')
        self.ui.lineEdit_note.setText('')
        self.ui.label_message.setText('')

        #self.ui.lineEdit_maxtresh.setText(f" {self.midi_app.at_vmax:.2f}")
        #self.ui.lineEdit_mintresh.setText(f" {self.midi_app.at_vmin:.2f}")

        print("Device Restarted Successfully!")

    def reset_device(self):
        """Restart the MIDI settings and test progress with the current configuration."""

        # Reload current configuration settings
        self.key_number = self.midi_app.key_number
        self.cached_vmin = self.voltage_to_8bit_range(self.midi_app.at_vmin)
        self.cached_vmax = self.voltage_to_8bit_range(self.midi_app.at_vmax)
        self.cached_exp = self.midi_app.at_exp
        self.black_gain = self.midi_app.black_gain
        self.white_gain = self.midi_app.white_gain

        self.test_started = False

        # Reset all stored resistance values
        self.last_resistance_per_key.clear()
        self.latest_resistance_values.clear()
        self.resistance_values.clear()
        self.processed_keys.clear()
        self.global_min_resistance = None

        # Stop timers
        for timer in self.resistance_timers.values():
            timer.stop()
        self.resistance_timers.clear()
        self.note_remaining_times.clear()

        # Reset state flags
        self.retry_mode = False
        self.test_passed = True
        self.current_display_note = None

        # Block UI updates for speed
        self.setUpdatesEnabled(False)

        # Reset sliders
        for slider in self.create_note_to_label_map().values():
            slider.setValue(0)
        for slider in self.sliders_velocity.values():
            slider.setValue(0)

        # Reset switch boxes
        default_box_style = "background-color: white; border: 1px solid black;"
        for note, boxes in self.switch_boxes.items():
            for box in boxes:
                box.setStyleSheet(default_box_style)

        # Reset editlines
        default_editline_style = "QLineEdit { font-size: 12px; background-color: none; }"
        for editline in self.create_note_to_editline_map().values():
            if editline:
                editline.setText("")
                editline.setStyleSheet(default_editline_style)

        self.played_notes = set()
        self.slider_good = {}
        self.dynamic_pass_in_full = False
        self.velocity_ok = {}
        self.full_velocity_ok = {}

        # Reset UI fields
        self.ui.lineEdit_counter_display.setText("")
        self.ui.lineEdit_aftertouch.setText("")
        self.ui.lineEdit_velocity.setText("")
        self.ui.lineEdit_resistance.setText("")
        self.ui.lineEdit_velo.setText("")
        self.ui.lineEdit_note.setText("")
        self.ui.label_message.setText("")
        self.ui.lineEdit_maxtresh.setText(f" {self.midi_app.at_vmax:.2f}")
        self.ui.lineEdit_mintresh.setText(f" {self.midi_app.at_vmin:.2f}")

        # Re-enable updates
        self.setUpdatesEnabled(True)
        self.repaint()

    def on_radio_acoustic_toggled(self, checked):
        if not checked:
            return

        sender = self.midi_app.midi_sender
        if sender and sender.tinyusb_outport:
            sender.send_control_change_tinyusb(
                channel=0,
                control=64,
                value=127
            )
            print("Acoustic mode CC sent")
            self.midi_app.mode = "acoustic"
        else:
            print("TinyUSB MIDI output not available")
        self.update_velocity_lines()

    def on_radio_electrical_toggled(self, checked):
        if not checked:
            return

        sender = self.midi_app.midi_sender
        if sender and sender.tinyusb_outport:
            sender.send_control_change_tinyusb(
                channel=0,
                control=63,
                value=127
            )
            print("Electrical mode CC sent")
            self.midi_app.mode = "electrical"
        else:
            print("TinyUSB MIDI output not available")
        self.update_velocity_lines()

    def on_two_sw_toggled(self, checked):
        if not checked:
            return

        sender = self.midi_app.midi_sender
        if sender and sender.tinyusb_outport:
            sender.send_control_change_tinyusb(
                channel=0,
                control=70,
                value=127
            )
            print("Electrical mode CC sent")
        else:
            print("TinyUSB MIDI output not available")

    def on_three_sw_toggled(self, checked):
        if not checked:
            return

        sender = self.midi_app.midi_sender
        if sender and sender.tinyusb_outport:
            sender.send_control_change_tinyusb(
                channel=0,
                control=71,
                value=127
            )
            print("Electrical mode CC sent")
        else:
            print("TinyUSB MIDI output not available")

    def on_dynamic_mode(self, checked):
        if checked:
            self.mode = "dynamic"
            print("Mode switched to DYNAMIC")

    def on_aft_mode(self, checked):
        if checked:
            self.mode = "aft"
            print("Mode switched to AFT")

    def on_full_mode(self, checked):
        if checked:
            self.mode = "full"
            print("Mode switched to FULL")

        """ ----------------------------------------- NOTE_ON --------------------------------------------- """

    def update_curve_value_white(self, value):
        """Update the curve value and display it in v_gain_lineEdit."""
        # Update the lineEdit with the curve value
        self.ui.v_gain_lineEdit.setText(f"{value}")
        self.curve_value = value

    def update_curve_value_black(self, value):
        """Update the curve value and display it in v_gain_lineEdit."""
        # Update the lineEdit with the curve value
        self.ui.v_gain_lineEdit_2.setText(f"{value}")
        self.curve_value_2 = value

    def update_exponent(self, value):
        """Update the exponent based on the slider's position."""
        # Map the slider value (100 to 500) to the exponent range (1.0 to 5.0)
        self.exponent_value = value / 100.0
        self.ui.lineEdit_exponent.setText(f"{self.exponent_value:.2f}")

    def reconstruct_8bit_value(self, status, data):
        """Reconstructs an 8-bit value from a status and data byte using the LSB of status."""
        return ((status & 0x01) << 7) | data  # Inline high bit extraction and bitwise OR

    def voltage_to_8bit_range(self, voltage):
        """Convert a voltage value (0 to 3.3V) to a value within 0 to 2047."""
        return float((voltage / 3.3) * 2047)

    def linear_map(self, x):
        """
        Map a value x from self.cached_vmin to self.cached_vmax to a range of [0, 1],
        then apply exponential scaling and multiply by 127 for the final range.
        """
        # Check if user-defined min/max values are provided
        if self.ui.lineEdit_user_min.text():
            self.cached_vmin = self.voltage_to_8bit_range(float(self.ui.lineEdit_user_min.text()))
        if self.ui.lineEdit_user_max.text():
            self.cached_vmax = self.voltage_to_8bit_range(float(self.ui.lineEdit_user_max.text()))
        if self.ui.lineEdit_exponent.text() != "1.0":
            self.cached_exp = self.exponent_value

        if self.cached_vmax == self.cached_vmin:
            print("Warning: cached_vmin and cached_vmax are equal; adjusting vmax.")
            self.cached_vmax += 0.01

        # Ensure x is within the source range
        if x < self.cached_vmin:
            x = self.cached_vmin
        elif x > self.cached_vmax:
            x = self.cached_vmax

        # Normalize x to the range [0, 1]
        normalized_x = (-(x - self.cached_vmin) / (self.cached_vmax - self.cached_vmin)) + 1
        # Apply exponential scaling
        normalized_x = math.pow(normalized_x, self.cached_exp)

        # Scale to the final range [0, 127]
        return normalized_x * 127
    def calculate_resistance(self, voltage):
        if voltage >= 3.3:
            print("Warning: Voltage too high for resistance calculation; capping resistance.")
            return 1e6  # Cap resistance at 1,000,000 ohms (example)
        return ((1000 * voltage) / (3.3 - voltage))

    def midi_to_note_name(self, midi_number):
        """Convert a MIDI note number to its corresponding musical note name."""
        note_names = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
        octave = (midi_number // 12) - 1
        note = note_names[midi_number % 12]
        return f"{note}{octave}"

    def handle_note_on(self, channel, note, velocity):
        """Handle Note-On, velocity processing, and start timers depending on mode."""

        # ==========================================================
        #  ACOUSTIC MODE → raw velocity only
        # ==========================================================
        if self.midi_app.mode == "acoustic":
            if note in self.sliders_velocity:
                slider = self.sliders_velocity[note]
                slider.setValue(velocity)
                slider.setStyleSheet("""
                    QSlider::groove:vertical { background: #DCDCDC; border: 1px solid #D3D3D3; width: 10px; border-radius: 4px; }
                    QSlider::handle:vertical { background: none; border: none; height: 0px; margin: -10px 0; }
                    QSlider::sub-page:vertical { background: #DCDCDC; height: 1px; border: none; }
                    QSlider::add-page:vertical { background: #4CAF50; border: none; }  /* GREEN */
                """)

            self.update_real_velo_display(velocity)
            self.update_note_display(self.midi_to_note_name(note))

            self.current_slider = self.note_to_label_map.get(note)
            self.note_pressed = True
            return  # Acoustic mode ends here

        # ==========================================================
        #  NORMAL ELECTRICAL VELOCITY CALCULATION
        # ==========================================================
        if self.ui.v_gain_lineEdit_2.text() != "40":
            self.black_gain = self.curve_value_2
        if self.ui.v_gain_lineEdit.text() != "40":
            self.white_gain = self.curve_value

        kCurve1 = self.white_gain if note % 12 in [0, 2, 4, 5, 7, 9, 11] else self.black_gain
        flytime = ((channel & 0x0F) << 7) + velocity
        offsetCurve1 = (-1 + 127 * kCurve1 / 1023)
        temp = (127 * kCurve1 / flytime) - offsetCurve1
        midi_out = max(0, min(int(temp), 127))

        if not self.test_started:
            self.test_started = True

        # UI range
        try:
            min_vel = int(self.ui.lineEdit_min_vel.text() or 55)
            max_vel = int(self.ui.lineEdit_max_vel.text() or 107)
        except:
            min_vel, max_vel = 55, 107

        # Update Slider
        if note in self.sliders_velocity:
            slider = self.sliders_velocity[note]
            slider.setValue(midi_out)

            if min_vel <= midi_out <= max_vel:
                slider.setStyleSheet("""
                    QSlider::groove:vertical { background: #DCDCDC; border: 1px solid #D3D3D3; width: 10px; border-radius: 4px; }
                    QSlider::handle:vertical { background: none; border: none; height: 0px; margin: -10px 0; }
                    QSlider::sub-page:vertical { background: #DCDCDC; height: 1px; border: none; }
                    QSlider::add-page:vertical { background: #4682B4; border: none; }
                """)
            else:
                slider.setStyleSheet("""
                    QSlider::groove:vertical { background: #DCDCDC; border: 1px solid #D3D3D3; width: 10px; border-radius: 4px; }
                    QSlider::handle:vertical { background: none; border: none; height: 0px; margin: -10px 0; }
                    QSlider::sub-page:vertical { background: #DCDCDC; height: 1px; border: none; }
                    QSlider::add-page:vertical { background: red; border: none; }
                """)

        self.update_real_velo_display(midi_out)
        self.update_note_display(self.midi_to_note_name(note))

        # ==========================================================
        #  MODE: DYNAMIC (velocity only)
        # ==========================================================
        if self.mode == "dynamic":
            self.played_notes.add(note)
            self.velocity_ok[note] = (min_vel <= midi_out <= max_vel)

            all_pressed = self.selected_notes.issubset(self.played_notes)
            all_ok = all(self.velocity_ok.get(n, False) for n in self.selected_notes)

            if all_pressed:
                if all_ok:
                    self.ui.label_message.setText("TEST PASSED")
                    self.ui.label_message.setStyleSheet("color: green; font-size: 50px; font-weight: bold;")
                else:
                    self.ui.label_message.setText("TEST NOT PASSED")
                    self.ui.label_message.setStyleSheet("color: red; font-size: 50px; font-weight: bold;")

            return  # STOP → no resistance

        # ==========================================================
        #  MODE: FULL (velocity now, aftertouch later)
        # ==========================================================
        if self.mode == "full":
            self.played_notes.add(note)
            self.full_velocity_ok[note] = (min_vel <= midi_out <= max_vel)

        # ==========================================================
        #  AFTERTOUCH START
        # ==========================================================
        self.note_pressed = True
        self.current_slider = self.note_to_label_map.get(note)
        self.latest_resistance_values[note] = float('inf')

        if not self.ui.checkBox_notimer.isChecked():
            self.start_resistance_timer(note)

    def update_aftertouch_value(self, status, data):
        """Capture resistance and update aftertouch slider + store min resistance."""
        # Acoustic mode → ignore aftertouch completely
        if self.midi_app.mode == "acoustic":
            return

        # Dynamic mode → ignore aftertouch completely
        if self.mode == "dynamic":
            return

        try:
            # Decode raw 11-bit aftertouch value
            aftertouch_value = ((status & 0x0F) << 7) | data
            aftertouch_voltage = min((aftertouch_value / 2047) * 3.3, 3.29)
            resistance = int(self.calculate_resistance(aftertouch_voltage))
            mapped_value = int(self.linear_map(aftertouch_value))
        except Exception as e:
            print(f"Error decoding aftertouch value: {e}")
            return

        # ----------------------------------------------
        # CASE 1 → Key is currently pressed (normal case)
        # ----------------------------------------------
        if self.note_pressed and self.current_slider:

            note = next((n for n, s in self.note_to_label_map.items()
                         if s == self.current_slider), None)

            if note is None:
                return

            # -------- STORE RESISTANCE --------
            if self.ui.checkBox_notimer.isChecked():
                # no-timer → keep MIN value
                prev = self.latest_resistance_values.get(note, float('inf'))
                self.latest_resistance_values[note] = min(prev, resistance)
            else:
                # normal mode → overwrite
                self.latest_resistance_values[note] = resistance

            # -------- UPDATE AT SLIDER --------
            self.current_slider.setValue(mapped_value)

            # -------- UPDATE UI DISPLAYS --------
            self.update_resistance_display(resistance)
            self.update_velocity_display(aftertouch_voltage)
            self.update_aftertouch_display(mapped_value)

            # ==========================================
            # FULL TEST: resistance part is stored here
            # we do NOT evaluate full test here
            # evaluation is done in compare_resistances()
            # ==========================================

            return

        # ----------------------------------------------
        # CASE 2 → No key pressed (safety)
        # Used for short-circuit detection
        # ----------------------------------------------
        try:
            if not self.test_started and resistance < 10000:
                self.ui.label_message.setText("SHORT CIRCUIT!")
                self.ui.label_message.setStyleSheet(
                    "QLabel { color: red; font-size: 30px; font-weight: bold; }"
                )
                print(f"Short Circuit Detected! Resistance: {resistance} Ω")
        except Exception as e:
            print(f"Error detecting short circuit: {e}")

    def handle_note_off(self, channel, note, velocity):
        """Track processed keys, but do not update resistance immediately."""
        if self.midi_app.mode == "acoustic":
            return

        if self.mode == "dynamic":
            return

        if not hasattr(self, 'last_resistance_per_key'):
            self.last_resistance_per_key = {}

        self.processed_keys.add(note)

        self.note_pressed = False
        if self.current_slider and not getattr(self, 'slider_fixed', False):
            self.current_slider.setValue(0)
        self.current_slider = None

        self.ui.lineEdit_counter_display.setStyleSheet("""
                           QLineEdit {
                               border: 2px solid orange;
                               border-radius: 5px;
                               padding: 2px;
                               font-size: 30px;
                               background-color: #fff8e1;
                               font-weight: bold;
                               color: orange;
                               qproperty-alignment: 'AlignCenter';
                           }
                       """)

        if self.ui.checkBox_notimer.isChecked():
            if note in self.latest_resistance_values:
                self.store_resistance_values(note)  # Directly save min value

        #if len(self.processed_keys) >= self.total_keys:
        #    self.compare_resistances()

    def start_resistance_timer(self, note):
        retry_mode = not self.test_passed
        duration = 10 if retry_mode else 2

        if not retry_mode and hasattr(self.ui, "lineEdit_counter_period"):
            try:
                duration = int(self.ui.lineEdit_counter_period.text())
                if duration < 1:
                    duration = 1
            except ValueError:
                pass

        self.note_remaining_times[note] = duration
        self.note_retry_mode[note] = retry_mode
        self.current_display_note = note
        self.ui.lineEdit_counter_display.setText(str(duration))

        if note not in self.resistance_timers:
            timer = QTimer(self)
            timer.timeout.connect(lambda n=note: self.update_resistance_check(n))
            self.resistance_timers[note] = timer

        self.resistance_timers[note].start(1000)

    def update_resistance_check(self, note):

        if self.ui.checkBox_notimer.isChecked():
            return

        if note not in self.note_remaining_times:
            return

        self.note_remaining_times[note] -= 1
        remaining = self.note_remaining_times[note]

        if self.current_display_note == note:
            self.ui.lineEdit_counter_display.setText(str(remaining))

        retry_mode = self.note_retry_mode.get(note, False)
        editline = self.note_to_editline_map.get(note)
        if not editline:
            return

        # === Retry Mode Logic ===
        if retry_mode:
            # Get the current resistance
            resistance = self.latest_resistance_values.get(note)
            try:
                min_res = int(self.ui.lineEdit_min_RES.text())
            except ValueError:
                min_res = 100
            try:
                max_res = int(self.ui.lineEdit_max_RES.text())
            except ValueError:
                max_res = 600

            # Check if current value is valid (in range)
            if resistance and min_res <= resistance <= max_res:
                self.last_resistance_per_key[note] = resistance
                editline.setText(str(int(resistance)))
                if resistance > 999:
                    editline.setStyleSheet("QLineEdit { font-size: 8px; background-color: none; }")
                else:
                    editline.setStyleSheet("QLineEdit { font-size: 12px; background-color: none; }")

                print(f"Retry mode: Note {note} value {resistance} is valid. Timer stopped early.")

                timer = self.resistance_timers.pop(note, None)
                if timer:
                    timer.stop()

                self.compare_resistances()

                self.note_remaining_times.pop(note, None)
                self.note_retry_mode.pop(note, None)
                return
            if remaining <= 0:
                print(f" Retry expired: Note {note} did not pass in time.")
                timer = self.resistance_timers.pop(note, None)
                if timer:
                    timer.stop()
                self.note_remaining_times.pop(note, None)
                self.note_retry_mode.pop(note, None)
                self.ui.lineEdit_counter_display.setText("0")
                return

        # === First Test Logic ===
        else:
            if remaining > 0:
                # Wipe previous value each second
                self.latest_resistance_values[note] = float('inf')

            if remaining <= 0:
                print(f"First test complete for note {note}.")
                self.store_resistance_values(note)

                timer = self.resistance_timers.pop(note, None)
                if timer:
                    timer.stop()

                self.resistance_timers.pop(note, None)
                self.note_remaining_times.pop(note, None)
                self.note_retry_mode.pop(note, None)

    def store_resistance_values(self, note):
        """Store the lowest resistance detected per key press after the timer expires."""
        if note not in self.latest_resistance_values:
            return  # Skip if no new values

        resistance = self.latest_resistance_values[note]

        # **Always update the last recorded resistance per key press**
        self.last_resistance_per_key[note] = resistance

        editline = self.note_to_editline_map.get(note)
        if editline:
            editline.setText(f"{self.last_resistance_per_key[note]}")

        if resistance > 999:
            editline.setStyleSheet("QLineEdit { font-size: 8px; }")  # Smaller font for large numbers
        else:
            editline.setStyleSheet("QLineEdit { font-size: 12px; }")

        self.processed_keys.add(note)
        self.latest_resistance_values.pop(note, None)  # Clear for next key press

        selected_notes = {note for note, btn in self.note_to_buttons_map.items() if btn.isChecked()}
        active_notes = selected_notes if selected_notes else set(self.note_to_buttons_map.keys())
        if active_notes.issubset(self.processed_keys):
            self.compare_resistances()


    def compare_resistances(self):
        """Evaluate resistances per key with optional black/white ratio split and range filtering."""
        # ----------------------------
        # 1) Dynamic mode → skip
        # ----------------------------
        if self.mode == "dynamic":
            return

        # ----------------------------
        # 2) Pick selected notes
        # ----------------------------
        selected_notes = set(self.midi_app.selected_notes)
        if not selected_notes:
            selected_notes = set(self.last_resistance_per_key.keys())

        # Filter resistances only for tested notes
        filtered = {
            n: self.last_resistance_per_key[n]
            for n in selected_notes
            if n in self.last_resistance_per_key
        }

        if not filtered:
            return

        # ----------------------------
        # 3) Read min/max resistance
        # ----------------------------
        try:
            min_res = int(self.ui.lineEdit_min_RES.text())
        except:
            min_res = 100

        try:
            max_res = int(self.ui.lineEdit_max_RES.text())
        except:
            max_res = 600

        # ----------------------------
        # 4) Black/white split
        # ----------------------------
        use_split = self.ui.checkBoxresplit.isChecked()

        black_notes = {n: r for n, r in filtered.items() if n % 12 not in [0, 2, 4, 5, 7, 9, 11]}
        white_notes = {n: r for n, r in filtered.items() if n % 12 in [0, 2, 4, 5, 7, 9, 11]}

        self.test_passed = True
        self.retry_mode = False

        def get_ratio(field, default):
            try:
                return float(field.text()) if field.text() else default
            except:
                return default

        def evaluate_group(group, ratio):
            """Apply ratio + min/max rule to each key."""
            nonlocal global_res_ok

            if not group:
                return

            group_min = min(group.values())

            for note, res in group.items():
                edit = self.note_to_editline_map.get(note)
                if not edit:
                    continue

                style = edit.styleSheet()

                # Ratio check
                if res > ratio * group_min:
                    edit.setStyleSheet(style + " QLineEdit { background-color: red; }")
                    self.test_passed = False
                    global_res_ok = False
                    continue

                # Min/max check
                if res < min_res or res > max_res:
                    edit.setStyleSheet(style + " QLineEdit { background-color: orange; }")
                    self.test_passed = False
                    global_res_ok = False
                    continue

                # OK
                edit.setStyleSheet(style + " QLineEdit { background-color: none; }")

        # GLOBAL flag
        global_res_ok = True

        # ----------------------------
        # 5) Apply resistance logic
        # ----------------------------
        if use_split:
            black_ratio = get_ratio(self.ui.lineEdit_ratio_black, 3.0)
            white_ratio = get_ratio(self.ui.lineEdit_ratio_white, 3.0)
            evaluate_group(black_notes, black_ratio)
            evaluate_group(white_notes, white_ratio)
        else:
            ratio = get_ratio(self.ui.lineEdit_ratio, 3.0)
            evaluate_group(filtered, ratio)

        # ----------------------------
        # 6) FULL MODE MUST check velocity also
        # ----------------------------
        if self.mode == "full":

            # Velocity reported?
            vel_reported = all(n in self.full_velocity_ok for n in selected_notes)
            vel_ok = all(self.full_velocity_ok.get(n, False) for n in selected_notes)

            aft_ok = global_res_ok  # from resistance evaluation

            # ============================
            #         FULL TEST PASS
            # ============================
            if vel_reported and vel_ok and aft_ok:

                self.test_passed = True
                self.ui.label_message.setText("TEST PASSED")
                self.ui.label_message.setStyleSheet("color: green; font-size: 50px; font-weight: bold;")

                print("Full test PASSED — prompting QR scan...")

                qr_dialog = SerialScannerDialog(self)
                if qr_dialog.exec_():
                    serial_number = qr_dialog.get_serial_number()
                    if serial_number:
                        print(f"Serial Number Scanned: {serial_number}")
                        self.save_resistances_to_excel(serial_number)  # <-- save in GOOD folder
                        self.reset_device()
                    else:
                        print("Invalid Serial Number — please scan again.")

                return  # Prevent normal PASS/FAIL from overriding

            # ============================
            #         FULL TEST FAIL
            # ============================
            else:
                self.test_passed = False
                self.ui.label_message.setText("TEST NOT PASSED")
                self.ui.label_message.setStyleSheet("color: red; font-size: 50px; font-weight: bold;")

                print("Full test FAILED")

                if self.ui.scan_nogoodkeyboards.isChecked():
                    print("Saving FAILED result into NO GOOD folder...")

                    qr_dialog = SerialScannerDialog(self)
                    if qr_dialog.exec_():
                        serial_number = qr_dialog.get_serial_number()
                        if serial_number:
                            print(f"Serial Scanned (FAILED): {serial_number}")
                            self.save_resistances_to_excel(serial_number)  # <-- saved in NO GOOD folder
                        else:
                            print("Invalid Serial Number! Scan again.")
                else:
                    print("scan_nogoodkeyboards unchecked → NOT saving failed test.")

                return  # FULL TEST handling done

        # ----------------------------
        # 7) AFTERTOUCH-ONLY MODE
        # ----------------------------
        if global_res_ok:
            self.ui.label_message.setText("PASSED")
            self.ui.label_message.setStyleSheet("color: green; font-size: 50px; font-weight: bold;")
        else:
            self.ui.label_message.setText("NOT PASSED")
            self.ui.label_message.setStyleSheet("color: red; font-size: 50px; font-weight: bold;")
            self.retry_mode = True

        # Update result message
        if self.test_passed:
            self.ui.label_message.setText("PASSED")
            self.ui.label_message.setStyleSheet("QLabel { color: green; font-size: 50px; font-weight: bold; }")

            print("Test Passed: Prompting QR code scan.")
            qr_dialog = SerialScannerDialog(self)
            if qr_dialog.exec_():
                serial_number = qr_dialog.get_serial_number()
                if serial_number:
                    print(f"Serial Number Scanned: {serial_number}")
                    self.save_resistances_to_excel(serial_number)
                    self.reset_device()
                else:
                    print("Invalid Serial Number! Please scan again.")
        else:
            self.ui.label_message.setText("NOT PASSED")
            self.ui.label_message.setStyleSheet("QLabel { color: red; font-size: 50px; font-weight: bold; }")
            self.retry_mode = True
            self.test_passed = False
            if self.ui.scan_nogoodkeyboards.isChecked():
                print("Saving failed result (NO GOOD folder)...")
                qr_dialog = SerialScannerDialog(self)
                if qr_dialog.exec_():
                    serial_number = qr_dialog.get_serial_number()
                    if serial_number:
                        print(f"Serial Number Scanned (Failed): {serial_number}")
                        self.save_resistances_to_excel(serial_number)
                        #self.reset_device()
                    else:
                        print("Invalid Serial Number! Please scan again.")
            else:
                print("scan_nogoodkeyboards is unchecked. Failed test not saved.")

        print(f"Final Test Status: {'PASSED' if self.test_passed else 'NOT PASSED'}")


    def save_resistances_to_excel(self, serial_number):
        """Save aftertouch (resistance) values to Excel, including all keys. 'N/A' for untested keys."""

        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

        if not self.test_passed and self.ui.scan_nogoodkeyboards.isChecked():
            results_subfolder = "no good results"
        else:
            results_subfolder = "good results"

        # Combine: "Results/good results" or "Results/no good results"
        results_folder = os.path.join("Results", results_subfolder)

        # Make sure it exists
        os.makedirs(results_folder, exist_ok=True)

        filename = os.path.join(results_folder, f"{serial_number}_{timestamp}.xlsx")

        # Open an empty workbook
        workbook = openpyxl.Workbook()
        sheet = workbook.active

        # Define full 88-key range
        full_notes = list(range(21, 109))  # MIDI notes 21 to 108

        # Write weight in cell A1
        sheet.cell(row=1, column=1, value=f"Weight: {self.midi_app.weight} g").alignment = Alignment(horizontal='left',
                                                                                                      vertical='center')

        # Write MIDI note numbers in the first row
        for col, note in enumerate(full_notes, start=1):
            sheet.cell(row=2, column=col, value=note).alignment = Alignment(horizontal='center', vertical='center')

        # Write note names in the second row
        for col, note in enumerate(full_notes, start=1):
            name = self.midi_to_note_name(note)
            sheet.cell(row=3, column=col, value=name).alignment = Alignment(horizontal='center', vertical='center')

        # Write resistance values (from last_resistance_per_key or N/A)
        for col, note in enumerate(full_notes, start=1):
            resistance = self.last_resistance_per_key.get(note, " ")
            sheet.cell(row=4, column=col, value=resistance).alignment = Alignment(horizontal='center',
                                                                                  vertical='center')

        # Save
        workbook.save(filename)
        print(f"Resistance values saved to: {filename}")

    def evaluate_full_test(self):
        """Check if both velocity AND aftertouch are valid in FULL test."""
        # If any selected key not played → test cannot pass
        if not (self.played_notes & self.selected_notes) == self.selected_notes:
            return False

        # Dynamic part
        dynamic_ok = all(self.slider_good.get(n, False) for n in self.selected_notes)

        # Aftertouch part
        aft_ok = True
        for n in self.selected_notes:
            if n not in self.latest_resistance_values:
                aft_ok = False
                break

        return dynamic_ok and aft_ok

    def update_velocity_display(self, velocity):
        """Display the last received velocity."""
        self.ui.lineEdit_velocity.setText(f" {velocity:.2f}")
        self.ui.lineEdit_velocity.setStyleSheet("QLineEdit { font-size: 40px; }")
        #print(f"Updated last velocity display: {velocity}")
    def update_aftertouch_display(self, aftertouch):
        """Display the last received velocity."""
        self.ui.lineEdit_aftertouch.setText(f" {aftertouch}")
        self.ui.lineEdit_aftertouch.setStyleSheet("QLineEdit { font-size: 40px; }")
        #print(f"Updated last velocity display: {velocity}")
    def update_resistance_display(self, resistance):
        """Display the last received velocity."""
        self.ui.lineEdit_resistance.setText(f" {resistance}")
        self.ui.lineEdit_resistance.setStyleSheet("QLineEdit { font-size: 40px; }")
        #print(f"Updated last velocity display: {velocity}")
    def update_real_velo_display(self, velocity):
        """Display the last received velocity."""
        self.ui.lineEdit_velo.setText(f" {velocity}")
        self.ui.lineEdit_velo.setStyleSheet("QLineEdit { font-size: 40px; }")

    def update_note_display(self, note):
        """Display the corresponding musical note."""
        self.ui.lineEdit_note.setText(note)
        self.ui.lineEdit_note.setStyleSheet("QLineEdit { font-size: 40px;}")

    def update_velocity_lines(self):
        """Position the min/max velocity lines across all sliders."""
        #In acoustic mode → hide lines and STOP
        if self.midi_app.mode == "acoustic":
            self.min_vel_line.hide()
            self.max_vel_line.hide()
            return

        try:
            min_vel = int(self.ui.lineEdit_min_vel.text()) if self.ui.lineEdit_min_vel.text() else 55
            max_vel = int(self.ui.lineEdit_max_vel.text()) if self.ui.lineEdit_max_vel.text() else 107
        except ValueError:
            min_vel, max_vel = 55, 107  # Default values

        # Get reference slider height (assuming all sliders are the same height)
        slider_sample = next(iter(self.sliders_velocity.values()), None)
        if slider_sample is None:
            return  # No sliders found

        slider_height = slider_sample.height()
        slider_top = slider_sample.y()
        slider_bottom = slider_top + slider_height
        slider_left = min(slider.x() for slider in self.sliders_velocity.values())  # Leftmost slider
        slider_right = max(slider.x() + slider.width() for slider in self.sliders_velocity.values())  # Rightmost slider

        # Calculate the Y position of the velocity lines
        min_pos = slider_bottom - int((min_vel / 127) * slider_height)
        max_pos = slider_bottom - int((max_vel / 127) * slider_height)

        # Position the lines across all sliders
        self.min_vel_line.setGeometry(slider_left, min_pos, slider_right - slider_left, 2)
        self.max_vel_line.setGeometry(slider_left, max_pos, slider_right - slider_left, 2)

        self.min_vel_line.show()
        self.max_vel_line.show()

    """ ----------------------------------------- MIDI_COM_TEST --------------------------------------------- """


    """ ----------------------------------------- CALIBRATION --------------------------------------------- """



if __name__ == "__main__":
    app = QApplication(sys.argv)

    print("📂 Prompting user for INI file before launching...")

    # Step 1: First, prompt the user to select an INI file
    midi_app = MidiApp()  # This now forces user to select INI

    print("INI file selected. Proceeding with loading screen...")

    # Step 2: Show the loading screen while initializing UI
    loading_screen = LoadingScreen()
    loading_screen.show()
    QApplication.processEvents()  # Prevent UI from freezing

    print("Loading Main Application...")

    # Step 3: Initialize MainWindow **AFTER** the loading screen
    window = MainWindow(midi_app)  # Pass the MIDI app with INI file

    print("Closing Loading Screen, Showing Application...")
    loading_screen.close()

    window.show()
    sys.exit(app.exec_())




