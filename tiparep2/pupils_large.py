import time

class Pupil():
    def __init__(self, f, n, p):
        self.f = f
        self.n = n
        self.p = p

pupils = 0
otlichniki = []
s_a = 0

start_time = time.time()

with open("pupils_large_txt.txt", "r", encoding='utf-8') as file:
    for line in file:
        data = line.split(' ')
        data_pupil = Pupil(data[0], data[1], int(data[2]))

        if data_pupil.p == 5:
            otlichniki.append(data_pupil.f)

        pupils += 1
        s_a += data_pupil.p


print('Средняя оценка класса:', (s_a/pupils), '\n\n', 'Лучшие ученики:')

for pupil in otlichniki:
    print(pupil)

print('Время выполнения', (time.time()-start_time), 'секунд.')