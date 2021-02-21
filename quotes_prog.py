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
    authors = []
    a = input('Автор фразы?')
    authors.append(a)
    data = file.write('(' + a + ')\n')
    print(data)
    while True:
        b = input('Хотите добавить ещё одну цитату?(да/нет)')
        if b == 'да':
            c = input('Введите цитату:')
            data = file.write(c + '\n')
            a = input('Автор фразы:')
            authors.append(a)
            data = file.write('(' + a + ')\n')
        else:
            print(authors)
            break
file.close()