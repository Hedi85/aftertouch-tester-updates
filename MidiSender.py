import mido

class Midisender:
    def __init__(self):
        self.tinyusb_outport = None
        self.open_tinyusb_port()

    def open_tinyusb_port(self):
        """Open the 'TinyUSB Device' MIDI output port if available."""
        for port in mido.get_output_names():
            if "TinyUSB Device" in port:
                try:
                    self.tinyusb_outport = mido.open_output(port)
                    print(f"Connected to TinyUSB output port: {port}")
                    return
                except IOError:
                    print(f"Could not open TinyUSB MIDI output port: {port}")

        print("Error: TinyUSB MIDI output port not found.")

    def send_control_change_tinyusb(self, channel, control, value):
        if not self.tinyusb_outport:
            print("Error: TinyUSB MIDI output port is not open.")
            return

        msg = mido.Message(
            'control_change',
            channel=channel,
            control=control,
            value=value
        )
        self.tinyusb_outport.send(msg)
        print(f"Sent CC via TinyUSB → ch:{channel} cc:{control} val:{value}")

    def close(self):
        if self.tinyusb_outport:
            self.tinyusb_outport.close()
            self.tinyusb_outport = None
