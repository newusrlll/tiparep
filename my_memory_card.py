from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import*
from rfll import *

class Question():
    def __init__(self, a, p, n1, n2, n3, tx, va):
        self.a = a
        self.p = p
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
        self.answers = [p, n1, n2, n3]
        self.text = QLabel(tx)
        self.vans = QLabel(va)

app = QApplication([])

main_win = QWidget()
main_win.resize(400, 200)
main_win.setWindowTitle('Memo Card')

btn_Ok = QPushButton('Ответить')

q = Question('Я придурок?', 'Более чем', 'Ненене', 'Нет', 'Да', 'Какой национальности не существует?', 'Ответ будет тут!')
ask(q)

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
l1.addWidget(q.vans, alignment=Qt.AlignHCenter, stretch=2)

ansGroupBox.setLayout(l1)

ll1 = QHBoxLayout()
ll2 = QHBoxLayout()
ll3 = QHBoxLayout()

ll1.addWidget(q.text, alignment=(Qt.AlignHCenter|Qt.AlignVCenter))
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
btn_Ok.clicked.connect(test)
main_win.setLayout(lc)
main_win.show()

app.exec_()