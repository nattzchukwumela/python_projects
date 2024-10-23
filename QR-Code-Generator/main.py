import qrcode
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QInputDialog, QPushButton, QDialog, QHBoxLayout, QVBoxLayout, QLineEdit, \
    QApplication, QMessageBox, QFileDialog
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

        #App widgets/layouts
        main_layout = QVBoxLayout()

        main_layout.addWidget(self.text_box)
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
          elif not (qr_txt.startswith('https://') or qr_txt.startswith('http://')):
              QMessageBox.critical(None, "Error", "Invalid URL. Please enter a URL starting with http:// or https://")

        elif self.text == 'reset':
            self.text_box.setText('')



if __name__ in '__main__':
    app = QApplication([])
    main_window = GenQr()
    main_window.show()
    app.exec_()






