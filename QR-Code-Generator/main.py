import qrcode
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QPushButton, QDialog, QHBoxLayout, QVBoxLayout, QLineEdit


class gen_qr(QWidget):
    def __init__(self):
        super().__init__()
        self.name = None
        self.text = None

        # App Settings
        self.setWindowTitle('QR CODE GENERATOR')
        self.resize(400, 250)

        #Add App Widgets
        #Buttons Widgets
        font = QFont('../font/poppin/Poppins-medium.ttf', 20)
        self.text_box = QLineEdit()
        self.text_box.setFont(font)

        self.reset = QPushButton('reset')
        self.backspace = QPushButton('backspace')

        #App widgets/layouts





