from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import*


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
    shuffle(q.answers)
    q.text.setText(q.a)
    q.vans.setText(q.p)
    q.answers[0].setText(q.p)
    q.answers[1].setText(q.n1)
    q.answers[2].setText(q.n2)
    q.answers[3].setText(q.n3)

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
