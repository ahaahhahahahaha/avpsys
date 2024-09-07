from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, 
                             QWidget, QHBoxLayout, 
                             QVBoxLayout, QGroupBox, 
                             QRadioButton, QPushButton, 
                             QLabel, QButtonGroup)
from random import shuffle, randint 

class Question():
    def __init__(self, question, answer , wrong1, wrong2, wrong3):
        self.question = question
        self.answer = answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list = []
question_list.append(Question("What is my favorite Inside track?", "All Eyes On Me","Bezos II",'30',"Problematic"))
question_list.append(Question("What is my favorite Make Happy track?", "Panderin'","Intro",'Rap',"Straight White Man"))
question_list.append(Question("What is my favorite what. track?", "Repeat Stuff","Sad",'#deep',"Left brain,Right brain"))
question_list.append(Question("What is my least favorite Inside track?", "Any Day Now","All Eyes On Me",'Welcome to the Internet',"Goodbye"))
question_list.append(Question("What is my least favorite Make Happy track?", "Intro","Can't Handle This",'Lower Your Expectations',"Panderin'"))
question_list.append(Question("What is my least favorite what. track?", "Sad","From God's Perspective",'#deep',"Repeat Stuff"))
question_list.append(Question("What is my favorite Bo Burnham Special?", "Inside","The Inside Outtakes",'Make Happy',"what."))
question_list.append(Question("What is my least favorite Bo Burnham Special?", "What.","The Inside Outtakes",'Make Happy',"Inside"))
question_list.append(Question("When did Inside come out?", "May 20","June 20",'June 18',"May 21"))
question_list.append(Question("Which year did The Inside Outtakes come out?", "2022 ","2021",'2020',"2023"))


app = QApplication([])
window = QWidget()

label_question = QLabel("What is 1 + 1?")
button_ok = QPushButton("Answer")



RadioGroupBox = QGroupBox("Answer Options")
rbtn_1 = QRadioButton("Option 1")
rbtn_2 = QRadioButton("Option 2")
rbtn_3 = QRadioButton("Option 3")
rbtn_4 = QRadioButton("Option 4")

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

layout_ans2 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)

layout_ans3 = QVBoxLayout()
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)

layout_ans1 = QHBoxLayout()
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

AnsGroupBox = QGroupBox()
label_result = QLabel()
label_correct = QLabel()

layout_res = QVBoxLayout()
layout_res.addWidget(label_result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(label_correct, alignment=Qt.AlignHCenter , stretch=2)

AnsGroupBox.setLayout(layout_res)

layout_line1 = QHBoxLayout()
layout_line1.addWidget(label_question , alignment=(Qt.AlignHCenter | Qt.AlignVCenter))

layout_line2 = QHBoxLayout()
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
AnsGroupBox.hide()

layout_line3 = QHBoxLayout()
layout_line3.addStretch(1)
layout_line3.addWidget(button_ok, stretch=2)
layout_line3.addStretch(1)

layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.addSpacing(5)

def show_result():
    ''' show answer panel '''
    RadioGroupBox.hide()
    AnsGroupBox.show()
    button_ok.setText('Next question')


def show_question():
    ''' show question panel '''
    RadioGroupBox.show()
    AnsGroupBox.hide()
    button_ok.setText('Answer')
    RadioGroup.setExclusive(False) 
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True) 

def test():
    if button_ok.text() == "Answer":
        check_answer()
    else:
        next_question()


answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def ask(q:Question):
    ''' the function writes the value of the question and answers into the corresponding widgets while distributing the answer options randomly'''
    shuffle(answers)
    answers[0].setText(q.answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    label_question.setText(q.question)
    label_correct.setText(q.answer) 
    show_question() 


def show_correct(res):
    ''' show result - put the written text into "result" and show the corresponding panel '''
    label_result.setText(res)
    show_result()


def check_answer():
    ''' if an answer option was selected, check and show answer panel '''
    if answers[0].isChecked():
        show_correct('Correct!')
        window.score += 1
    else:
        show_correct('Incorrect!')
    print("Stats: \nTotal:" , window.total, 
          "\Score:", window.score,
          "\nRating:", int(window.score / window.total * 100))

def next_question():
    window.total += 1
    window.cur_question = randint(0, len(question_list) -1)
    q = question_list[window.cur_question]
    ask(q)

window.cur_question = -1
window.total = 0
window.score = 0

next_question()

window.setLayout(layout_card)
window.setWindowTitle("Memory Card")
button_ok.clicked.connect(test)

window.show()
app.exec()