import time

class Pupil():
    def __init__(self, f, n, p):
        self.f = f
        self.n = n
        self.p = p

pupils = []
s_a = []
otlichniki = []

start_time = time.time()

file = open("pupils_txt.txt", "r", encoding='utf-8')
pupla = file.read().split('\n')

for pupil in pupla:
    pupil = pupil.split(' ')
    pupils.append(Pupil(pupil[0], pupil[1], pupil[2]))

for pupil in pupils:
    s_a.append(int(pupil.p))
    print(pupil.f, pupil.n, '-', pupil.p)
    if pupil.p == '5':
        otlichniki.append(pupil.f)
print('Отличники:')
for i in otlichniki:
    print(i)


print(time.time()-start_time)
print('Время выполнения', time.time()-start_time, 'секунд.')

print('Средняя оценка класса:', sum(s_a) / len(s_a))