from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import*
from random import shuffle


def show_result():
    ansGroupBox.show()
    RadioGroupBox.hide()
    btn_Ok.setText('Следующий вопрос')

def show_question():
    ansGroupBox.hide()
    RadioGroupBox.show()
    btn_Ok.setText('Ответить')
    RadioGroup.setExclusive(False)
    nb1.setChecked(False)
    vb.setChecked(False)
    nb2.setChecked(False)
    nb3.setChecked(False)
    RadioGroup.setExclusive(True)
    q = Question('аааа', 'Писец', 'Пепец', 'Капец', 'Блеанб')
    ask(q)

def ask(q):
    shuffle(answers)
    text.setText(q.a)
    vans.setText(q.p)
    answers[0].setText(q.p)
    answers[1].setText(q.n1)
    answers[2].setText(q.n2)
    answers[3].setText(q.n3)

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно')
    if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
        show_correct('Неправильно')

def show_correct(res):
    ans.setText(res)
    show_result()

def test():
    if btn_Ok.text() == 'Ответить':
        check_answer()
    else:
        show_question()


class Question():
    def __init__(self, a, p, n1, n2, n3):
        self.a = a
        self.p = p
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3

app = QApplication([])

main_win = QWidget()
main_win.resize(400, 200)
main_win.setWindowTitle('Memo Card')

btn_Ok = QPushButton('Ответить')

text = QLabel('Какой национальности не существует?')
vans = QLabel('Ответ будет тут!')
RadioGroupBox = QGroupBox('Варианты')

RadioGroup = QButtonGroup()

nb1 = QRadioButton('Энцы')
vb = QRadioButton('Смурфы')
nb2 = QRadioButton('Чулымцы')
nb3 = QRadioButton('Алеуты')

RadioGroup.addButton(nb1)
RadioGroup.addButton(vb)
RadioGroup.addButton(nb2)
RadioGroup.addButton(nb3)

ans1 = QHBoxLayout()

ans2 = QVBoxLayout()
ans3 = QVBoxLayout()

ans2.addWidget(nb1)
ans2.addWidget(vb)

ans3.addWidget(nb2)
ans3.addWidget(nb3)

ans1.addLayout(ans2)
ans1.addLayout(ans3)

RadioGroupBox.setLayout(ans1)

ansGroupBox = QGroupBox('Результат теста')

ansGroupBox.hide()

ans = QLabel('Прав ты или нет?')

l1 = QVBoxLayout()

l1.addWidget(ans, alignment=(Qt.AlignLeft|Qt.AlignTop))
l1.addWidget(vans, alignment=Qt.AlignHCenter, stretch=2)

ansGroupBox.setLayout(l1)

ll1 = QHBoxLayout()
ll2 = QHBoxLayout()
ll3 = QHBoxLayout()

ll1.addWidget(text, alignment=(Qt.AlignHCenter|Qt.AlignVCenter))
ll2.addWidget(RadioGroupBox)
ll2.addWidget(ansGroupBox)
ll3.addStretch(1)
ll3.addWidget(btn_Ok, stretch=2)
ll3.addStretch(1)

lc = QVBoxLayout()

lc.addLayout(ll1, stretch=2)
lc.addLayout(ll2, stretch=8)
lc.addStretch(1)
lc.addLayout(ll3, stretch=1)
lc.addStretch(1)
lc.setSpacing(5)

answers = [vb, nb1, nb2, nb3]

q = Question('Я придурок?', 'Более чем', 'Ненене', 'Нет', 'Да')
ask(q)



btn_Ok.clicked.connect(test)
main_win.setLayout(lc)
main_win.show()

app.exec_()