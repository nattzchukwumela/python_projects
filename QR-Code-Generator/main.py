import qrcode
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QPushButton, QDialog, QHBoxLayout, QVBoxLayout, QLineEdit, QApplication



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
        self.backspace.setStyleSheet("QPushButton{color: #ff0;}")
        self.reset.setStyleSheet("QPushButton{color: red;}")
        btn_layout = QHBoxLayout()

        #App widgets/layouts
        main_layout = QVBoxLayout()

        main_layout.addWidget(self.text_box)
        btn_layout.addWidget(self.reset)
        btn_layout.addWidget(self.backspace)
        main_layout.addLayout(btn_layout)
        self.setLayout(main_layout)

if __name__ in '__main__':
    app = QApplication([])
    main_window = gen_qr()
    main_window.show()
    app.exec_()






