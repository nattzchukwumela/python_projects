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
        self.resize(300, 400)

        # App widgets
        self.question_box = QLabel('Ask Question')
        self.start = QPushButton('start')
        self.skip = QPushButton('skip')
        self.end = QPushButton('end quiz')


