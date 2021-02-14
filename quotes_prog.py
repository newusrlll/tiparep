while True:
    filename = input('Введите название файла')
    try:
        file = open(filename, "r", encoding='utf-8')
        break
    except IOError:
        print('Некорректное название файла, введите снова')
data = file.read()
print(data)
with open(filename, "a", encoding='utf-8') as file:
    a = input('Автор фразы?')
    data = file.write('(' + a + ')\n')
    print(data)
file.close()