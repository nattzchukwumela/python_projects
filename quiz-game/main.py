from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QDialog, QApplication
from modules import quiz_questions

class Quiz(QWidget):
    def __init__(self):
        super().__init__()
        self.btn_layout = None
        self.answers_layout = None
        self.main_layout = None
        self.score_label = None
        self.question_box = None
        self.end_btn = None
        self.skip_btn = None
        self.start_btn = None
        self.current_question_index = 0
        self.score = 0
        self.answer_buttons = []
        self.setup_ui()

    def setup_ui(self):
        # App setting
        self.setWindowTitle('Quiz Game')
        self.resize(350, 300)

        # App widgets
        # App text
        font = QFont('../font/poppin/Poppins-medium.ttf', 18) # default app font
        self.question_box = QLabel('click start to begin')
        self.question_box.setFont(font)
        self.question_box.setAlignment(Qt.AlignCenter)

        #track score
        self.score_label = QLabel(f"score {self.score}")
        self.score_label.setAlignment(Qt.AlignCenter)

        # App buttons
        self.start_btn = QPushButton('start')
        self.skip_btn = QPushButton('skip')
        self.end_btn = QPushButton('end quiz')

        # disable button
        self.skip_btn.setEnabled(False)
        self.end_btn.setEnabled(False)

        # connect functions btn
        self.start_btn.clicked.connect(self.start_quiz)

        # App layouts
        self.main_layout = QVBoxLayout()
        self.answers_layout = QVBoxLayout()
        self.btn_layout = QHBoxLayout()

        # combine layouts
        self.btn_layout.addWidget(self.start_btn)
        self.btn_layout.addWidget(self.skip_btn)
        self.btn_layout.addWidget(self.end_btn)

        # create layout
        self.main_layout.addWidget(self.score_label)
        self.main_layout.addWidget(self.question_box)
        self.main_layout.addLayout(self.answers_layout)
        self.main_layout.addLayout(self.btn_layout)

        self.setLayout(self.main_layout)

    def start_quiz(self):
        self.score = 0
        self.current_question_index = 0
        self.score_label.setText(f"score {self.score}")
        self.start_btn.setEnabled(False)
        self.end_btn.setEnabled(True)
        self.skip_btn.setEnabled(True)
        self.display_question()

        # button creation and deletion handler
    def create_answer_button(self, options):
        # first clear existing layout
        for button in self.answer_buttons:
            self.answers_layout.removeWidget(button)
            button.deleteLater()
        self.answer_buttons.clear()

        # second create new button
        for option in options:
            button = QPushButton(option)
            button.clicked.connect(lambda _, ans=option: self.check_answer(ans))
            self.answers_layout.addWidget(button)
            self.answer_buttons.append(button)

        # show question and update question
    def display_question(self):
        if self.current_question_index < len(quiz_questions):
            current_question = quiz_questions[self.current_question_index]
            self.question_box.setText(current_question['question'])
            self.create_answer_button(current_question['options'])

        # check if user selection is same as answer to question
    def check_answer(self, picked_answer):
        current_question = quiz_questions[self.current_question_index]
        print('clicked')
        print(self.current_question_index)
        if picked_answer == current_question['answer']:
            self.score += 1
            self.score_label.setText(f"current score: {self.score}")
        self.next_question()

        # update question everytime user makes a choice
    def next_question(self):
        self.current_question_index += 1
        self.display_question()


# start/ init app
if __name__ in '__main__':
    app = QApplication([])
    main_window = Quiz()
    main_window.show()
    app.exec_()
