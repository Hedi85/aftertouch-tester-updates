from PySide2.QtWidgets import QDialog, QVBoxLayout, QLabel, QProgressBar
from PySide2.QtCore import Qt

class UpdateDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Updating…")
        self.setFixedSize(400, 120)
        self.setWindowFlags(Qt.Window | Qt.CustomizeWindowHint | Qt.WindowTitleHint)

        layout = QVBoxLayout(self)

        self.label = QLabel("Preparing update…")
        layout.addWidget(self.label)

        self.progress = QProgressBar()
        self.progress.setMinimum(0)
        self.progress.setMaximum(100)
        layout.addWidget(self.progress)

        # Match your style (dark gray background)
        self.setStyleSheet("""
            QDialog { background-color: #222; color: white; }
            QLabel { font-size: 14px; }
            QProgressBar {
                background: #444;
                border: 1px solid #888;
                height: 18px;
            }
            QProgressBar::chunk {
                background: #00C8FF;   /* cyan like Arturia UI? change if needed */
            }
        """)

    def set_status(self, text):
        self.label.setText(text)

    def set_progress(self, value):
        self.progress.setValue(value)
