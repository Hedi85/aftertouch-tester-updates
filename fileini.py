# midi_setup.py
import configparser
from PySide2.QtWidgets import QMessageBox, QFileDialog
import mido
from midi_listener import MidiListener
from MidiSender import Midisender
import os


class MidiApp:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.load_config_file()
        self.set_midi_ports()

    def load_config_file(self):
        # Open a file dialog for the user to select a configuration file
        config_path, _ = QFileDialog.getOpenFileName(None, "Select Configuration File", "", "Config Files (*.ini)")

        if config_path:
            self.config.read(config_path)
            try:
                self.midi_in_index = int(self.config["MIDI"]["midi_in"])
                self.midi_out_index = int(self.config["MIDI"]["midi_out"])
                self.key_number = int(self.config["KEYBOARD_FORMAT"]["key_number"])
                self.at_vmin = float(self.config["AT_VOLTAGE"]["vmin"])
                self.at_vmax = float(self.config["AT_VOLTAGE"]["vmax"])
                self.at_exp = float(self.config["AT_VOLTAGE"]["exponent"])
                self.black_gain = int(self.config["Vel_gain"]["black"])
                self.white_gain = int(self.config["Vel_gain"]["white"])
                self.serial_port = self.config["SERIAL"]["port"]

                self.ratio = float(self.config["RATIO"]["global"])
                self.min_velocity = int(self.config["VELOCITY_LIMITS"]["min_velocity"])
                self.max_velocity = int(self.config["VELOCITY_LIMITS"]["max_velocity"])
                self.ratio_black = float(self.config["RATIO"]["black"])
                self.ratio_white = float(self.config["RATIO"]["white"])
                self.min_resistance = int(self.config["RESISTANCE_LIMITS"]["min_resistance"])
                self.max_resistance = int(self.config["RESISTANCE_LIMITS"]["max_resistance"])
                self.counter = int(self.config["COUNTER"]["counter"])
                self.weight = int(self.config["WEIGHT"]["weight"])

                self.switches = int(self.config["SWITCHES"]["number"])

                self.split_enabled = self.config.getboolean("SPLIT", "enabled", fallback=False)
                self.scan_no_good_enabled = self.config.getboolean("SCAN_NO_GOOD", "enabled", fallback=False)
                self.notimer_enabled = self.config.getboolean("NOTIMER", "enabled", fallback=False)

                self.mode = self.config.get("MODE", "type", fallback="electrical")
                self.test_mode = self.config.get("TEST", "test_mode", fallback="dynamic")


                # Load selected notes
                selected_str = self.config["SELECTION"].get("selected_notes", "")
                if selected_str:
                    self.selected_notes = list(map(int, selected_str.split(',')))
                else:
                    self.selected_notes = list(range(21, 21 + self.key_number))  # Default: all notes

                self.config_path = config_path

                print(f"Config loaded from {config_path}")
            except KeyError as e:
                QMessageBox.critical(None, "Configuration Error", f"Missing required key: {e}")

            self.config_filename = os.path.basename(config_path)

        else:
            QMessageBox.critical(None, "Configuration Error", "No configuration file selected.")
            raise SystemExit("Application requires a configuration file to run.")

    def set_midi_ports(self):
        midi_in_ports = mido.get_input_names()
        midi_out_ports = mido.get_output_names()

        # TinyUSB INPUT (used by MidiListener)
        self.tinyusb_port = next(
            (port for port in midi_in_ports if "TinyUSB Device" in port),
            None
        )

        if self.tinyusb_port:
            print(f"Using TinyUSB MIDI input: {self.tinyusb_port}")
        else:
            print("TinyUSB MIDI input not found")

        #Disable MIDI DIN completely
        self.midi_in_port = None
        self.midi_out_port = None

    def get_serial_port(self):
        """Return the serial port name from the config file."""
        return self.serial_port

    def load_config(self, file_path):
        """Load a new configuration file and update MIDI ports."""
        self.config.read(file_path)
        self.midi_in_index = int(self.config["MIDI"]["midi_in"])
        self.midi_out_index = int(self.config["MIDI"]["midi_out"])
        self.key_number = int(self.config["KEYBOARD_FORMAT"]["key_number"])
        self.at_vmin = float(self.config["AT_VOLTAGE"]["vmin"])
        self.at_vmax = float(self.config["AT_VOLTAGE"]["vmax"])
        self.at_exp = float(self.config["AT_VOLTAGE"]["exponent"])
        self.black_gain = int(self.config["Vel_gain"]["black"])
        self.white_gain = int(self.config["Vel_gain"]["white"])

        self.ratio = float(self.config["RATIO"]["global"])
        self.min_velocity = int(self.config["VELOCITY_LIMITS"]["min_velocity"])
        self.max_velocity = int(self.config["VELOCITY_LIMITS"]["max_velocity"])
        self.ratio_black = float(self.config["RATIO"]["black"])
        self.ratio_white = float(self.config["RATIO"]["white"])
        self.min_resistance = int(self.config["RESISTANCE_LIMITS"]["min_resistance"])
        self.max_resistance = int(self.config["RESISTANCE_LIMITS"]["max_resistance"])

        self.counter = int(self.config["COUNTER"]["counter"])
        self.weight = int(self.config["WEIGHT"]["weight"])

        self.split_enabled = self.config.getboolean("SPLIT", "enabled", fallback=False)
        self.scan_no_good_enabled = self.config.getboolean("SCAN_NO_GOOD", "enabled", fallback=False)
        self.notimer_enabled = self.config.getboolean("NOTIMER", "enabled", fallback=False)

        # Load selected notes
        selected_str = self.config["SELECTION"].get("selected_notes", "")
        if selected_str:
            self.selected_notes = list(map(int, selected_str.split(',')))
        else:
            self.selected_notes = list(range(21, 21 + self.key_number))  # Default: all notes

        self.set_midi_ports()  # Update ports based on new configuration

    def save_selected_keys(self, selected_notes, file_path=None):
        """Save the selected notes into the INI config file."""
        if not file_path:
            file_path = self.config_path

        self.config["SELECTION"] = {
            "selected_notes": ",".join(str(n) for n in selected_notes)
        }

        with open(file_path, 'w') as configfile:
            self.config.write(configfile)

    def start_midi_listener(self, update_function):
        """Start the MIDI listener and connect it to the provided update function."""
        try:
            # Stop any existing listeners before starting a new one
            self.stop_midi_listeners()

            if hasattr(self, 'midi_sender') and self.midi_sender.outport:
                self.midi_sender.close()

            if self.tinyusb_port:
                self.tinyusb_listener = MidiListener(self.tinyusb_port)
                self.tinyusb_listener.midi_signal.connect(update_function)
                self.tinyusb_listener.start()
                print(f"Listening on TinyUSB Device: {self.tinyusb_port}")

            if self.midi_in_port:
                self.ini_listener = MidiListener(self.midi_in_port)
                self.ini_listener.midi_signal.connect(update_function)
                self.ini_listener.start()
                print(f"Listening on config.ini MIDI input: {self.midi_in_port}")

            # Initialize the MIDI sender with the selected output port
            self.midi_sender = Midisender(self.midi_out_port)

        except Exception as e:
            QMessageBox.critical(None, "Connection Error", f"Failed to start listener: {str(e)}")

    def stop_midi_listeners(self):
        """Stop any active MIDI listeners."""
        if hasattr(self, 'tinyusb_listener') and self.tinyusb_listener.is_running():
            self.tinyusb_listener.stop()
        if hasattr(self, 'ini_listener') and self.ini_listener.is_running():
            self.ini_listener.stop()

