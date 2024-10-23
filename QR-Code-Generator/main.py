import qrcode
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLineEdit, \
    QApplication, QMessageBox, QFileDialog, QLabel
import os


class GenQr(QWidget):
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
        self.generate = QPushButton('generate')
        self.backspace.setStyleSheet("QPushButton{color: #ff0;}")
        self.generate.setStyleSheet("QPushButton{color: green;}")
        self.reset.setStyleSheet("QPushButton{color: red;}")
        btn_layout = QHBoxLayout()

        # QR img widget
        self.display_img = QLabel('Image will appear here')
        self.display_img.setAlignment(Qt.AlignCenter)

        #App widgets/layouts
        main_layout = QVBoxLayout()

        main_layout.addWidget(self.text_box)
        main_layout.addWidget(self.display_img)
        btn_layout.addWidget(self.reset)
        btn_layout.addWidget(self.generate)
        btn_layout.addWidget(self.backspace)
        main_layout.addLayout(btn_layout)
        self.setLayout(main_layout)

        self.generate.clicked.connect(self.btn_click)
        self.reset.clicked.connect(self.btn_click)

        #button click functionality
    def btn_click(self):
        btn = app.sender()
        self.text = btn.text()
        qr_txt = self.text_box.text()
        print(qr_txt)
        if self.text == 'generate':
          if qr_txt.startswith('https://') or qr_txt.startswith('http://'):
                qr = qrcode.QRCode(
                    version=1,
                    error_correction = qrcode.constants.ERROR_CORRECT_L,
                    box_size = 10,
                    border = 5,
                )
                qr.add_data(self.text_box.text())
                qr.make(fit=True)
                qr_img = qr.make_image(fill_color='black', back_color='white')

                # choose a path to save the image
                self.name, _ = QFileDialog.getSaveFileName(
                    self,
                    "Save QR Code",
                    os.getcwd(),
                    "PNG Image (*.png)"
                    )

                # Choose directory to save file
                save_path = os.path.join(self.name)
                qr_img.save(save_path)

                # Display QR-Code on the app
                self.display_img.hide()
                img = QPixmap(save_path)
                width, height = self.display_img.width(), self.display_img.height()
                scaled_img = img.scaled(width, height, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                self.display_img.setPixmap(scaled_img)
                self.display_img.show()


                # The code will only run if there's an invalid url
          elif not (qr_txt.startswith('https://') or qr_txt.startswith('http://')):
              QMessageBox.critical(None, "Error", "Invalid URL. Please enter a URL starting with http:// or https://")

        elif self.text == 'reset':
             self.text_box.setText('')


if __name__ in '__main__':
    app = QApplication([])
    main_window = GenQr()
    main_window.show()
    app.exec_()






