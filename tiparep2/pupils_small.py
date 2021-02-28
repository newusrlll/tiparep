class Pupil():
    def __init__(self, f, n, p):
        self.f = f
        self.n = n
        self.p = p
file = open("pupils_txt.txt", "r", encoding='utf-8')
pupla = file.read().split('\n')
pupils = []
for pupil in pupla:
    pupil = pupil.split(' ')
    pupils.append(Pupil(pupil[0], pupil[1], pupil[2]))
s_a = []
otlichniki = []
for pupil in pupils:
    s_a.append(int(pupil.p))
    print(pupil.f, pupil.n, '-', pupil.p)
    if pupil.p == '5':
        otlichniki.append(pupil.f)
print('Отличники:')
for i in otlichniki:
    print(i)


print('Средняя оценка класса:', sum(s_a) / len(s_a))
