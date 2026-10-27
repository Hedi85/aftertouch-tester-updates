from PySide2.QtCore import Signal, QObject
import threading
import mido
import collections
import time


class CircularBuffer:
    """Thread-safe circular buffer implementation."""
    def __init__(self, size):
        self.buffer = collections.deque(maxlen=size)
        self.lock = threading.Lock()

    def push(self, item):
        with self.lock:
            self.buffer.append(item)

    def pop(self):
        with self.lock:
            if self.buffer:
                return self.buffer.popleft()
            return None

    def __len__(self):
        with self.lock:
            return len(self.buffer)


class MidiListener(QObject):
    midi_signal = Signal(str, int, int, int)

    def __init__(self, port_name, buffer_size=2048):
        super().__init__()
        self.port_name = port_name
        self.buffer_size = buffer_size
        self.buffer = CircularBuffer(buffer_size)
        self.running = False
        self.listener_thread = None
        self.processor_thread = None

    def start(self):
        """Start listener and processor threads (always fresh)."""
        if self.running:
            return  # already running
        self.running = True

        # Recreate fresh threads every time
        self.listener_thread = threading.Thread(target=self.listen, daemon=True)
        self.processor_thread = threading.Thread(target=self.process_messages, daemon=True)
        self.listener_thread.start()
        self.processor_thread.start()

    def listen(self):
        try:
            with mido.open_input(self.port_name, virtual=False) as inport:
                while self.running:
                    msg = inport.poll()
                    if msg:
                        self.buffer.push(msg)
                    else:
                        time.sleep(0.0001)
        except Exception as e:
            print(f"Error in MIDI listener: {e}")

    def process_messages(self):
        while self.running:
            msg = self.buffer.pop()
            if msg:
                self.emit_signal(msg)
            else:
                time.sleep(0.0001)

    def emit_signal(self, msg):
        try:
            if msg.type == 'note_on':
                self.midi_signal.emit("note", msg.channel, msg.note, msg.velocity)
            elif msg.type == 'note_off':
                self.midi_signal.emit("note_off", msg.channel, msg.note, msg.velocity)
            elif msg.type in ['aftertouch', 'channel_aftertouch']:
                self.midi_signal.emit("aftertouch", msg.channel, None, msg.value)
            else:
                raw_bytes = msg.bytes()
                status = raw_bytes[0]
                data1 = raw_bytes[1]
                if 0xC0 <= status <= 0xC5:
                    self.midi_signal.emit("switch", status, data1, 0)
        except Exception as e:
            print(f"Error emitting MIDI signal: {e}")

    def stop(self):
        """Stop the listener and processor threads safely."""
        if not self.running:
            return
        self.running = False

        if self.listener_thread and self.listener_thread.is_alive():
            self.listener_thread.join(timeout=1.0)
        if self.processor_thread and self.processor_thread.is_alive():
            self.processor_thread.join(timeout=1.0)

        self.listener_thread = None
        self.processor_thread = None

    def is_running(self):
        return self.running
