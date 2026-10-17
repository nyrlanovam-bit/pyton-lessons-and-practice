contacts = [
    {'name': 'Geektech', 'phone': '0507052018'},
    {'name': 'Служба спасения', 'phone': '911'},
    {'name': 'Пожарная служба', 'phone': '101'}
]


def create():
    name = input('Введите имя: ')
    phone = input('Введите номер телефона: ')

    contacts.append({
        'name': name,
        'phone': phone
    })


def edit():
    index = int(input('Введите индекс контакта: '))

    name = input('Введите новое имя: ')
    phone = input('Введите новый номер телефона: ')

    contacts[index] = {
        'name': name,
        'phone': phone
    }


def delete():
    index = int(input('Введите индекс контакта: '))
    contacts.pop(index)


ten = []

for i in range(1, 11):
    ten.append(i)


evens = []

for i in ten:
    if i % 2 == 0:
        evens.append(i)


squares = []

for i in evens:
    squares.append(i ** 2)

print(squares)


def get_item(items=ten):

    while True:
        index = input('Введите индекс или exit для выхода: ')

        if index == 'exit':
            break

        try:
            index = int(index)
            print(f'Элемент: {items[index]}')

        except IndexError:
            print('Неверный индекс!')
            print(f'Актуальные индексы: 0 - {len(items) - 1}')

        except ValueError:
            print('Введите число или exit')



    