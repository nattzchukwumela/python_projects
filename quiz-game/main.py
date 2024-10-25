from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QDialog, QApplication
from modules import quiz_questions

class Quiz(QWidget):
    def __init__(self):
        super().__init__()
        self.question = None
        self.answer = None
        self.difficulty = None

        # App setting
        self.setWindowTitle('Quiz Game')
        self.resize(350, 300)

        # App widgets
        # App text
        font = QFont('../font/poppin/Poppins-medium.ttf', 18) # default app font
        self.question_box = QLabel('start Question')
        self.question_box.setFont(font)
        self.question_box.setAlignment(Qt.AlignCenter)

        # App buttons
        self.start = QPushButton('start')
        self.skip = QPushButton('skip')
        self.end = QPushButton('end quiz')

        # App layouts
        main_layout = QVBoxLayout()
        btn_layout = QHBoxLayout()

        # combine layouts
        btn_layout.addWidget(self.start)
        btn_layout.addWidget(self.skip)
        btn_layout.addWidget(self.end)

        # create layout
        main_layout.addWidget(self.question_box)
        main_layout.addLayout(btn_layout)
        self.setLayout(main_layout)

# start/ init app
if __name__ in '__main__':
    app = QApplication([])
    main_window = Quiz()
    main_window.show()
    app.exec_()
