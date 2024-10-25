from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QDialog, QApplication
from modules import quiz_questions

class Quiz(QWidget):
    def __init__(self):
        super().__init__()
        self.question = None
        self.answer = None
        self.difficulty = None

