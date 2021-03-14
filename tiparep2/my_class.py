class Pupil():
    def __init__(self, n, a):
        self.n = n
        self.a = a

p = 0
v_a = []
chmo = ''
chmo_max = 0

with open("my_group.txt", "r", encoding='utf-8') as file:
    for line in file:
        data = line.split(' - ')
        data_pupil = Pupil(data[0], int(data[1]))
        p+=1
        if chmo_max < data_pupil.a:
            chmo_max = data_pupil.a
            chmo = line
        v_a.append(data_pupil.a)


print('Старший ученик:', chmo)
print('Средний возраст группы:', (sum(v_a)/p))