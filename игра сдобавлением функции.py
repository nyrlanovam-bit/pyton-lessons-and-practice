import random

player = {'hp': 100, 'has_key': False}
events = ['змея (-20 HP) 🐍', 'ловушка (-30 HP) 💥', 'обвал (-15 HP) 🪨', 'призрак (-25 HP) 👻']
damage = [20, 30, 15, 25]


def get_choice(max_option):
    while True:
        try:
            choice = int(input('Ваш выбор: '))
            if 1 <= choice <= max_option:
                return choice
            print(f'Введите число от 1 до {max_option}!')
        except ValueError:
            print('Ошибка! Введите только цифру 😅')


def check_hp():
    try:
        if player['hp'] <= 0:
            print('\nВы теряете сознание от боли')
            print('И резко открываете глаза в кровати! Всё это был кошмар 😱')
            return False
        return True
    except KeyError:
        print('Ошибка структуры данных')
        return False


def room_1():
    print('\n 1 комната 🚪 ')
    print('Перед вами 3 прохода Ключ спрятан в одном из них')

    for tunnel in range(1, 4):
        print(f'{tunnel} — Осмотреть проход {tunnel}')

    choice = get_choice(3)
    if choice == 2:
        print('\nВы сразу нашли ключ 🔑')
        player['has_key'] = True
    else:
        print('\nЗдесь тупик Пришлось обшарить остальные проходы и потерять силы (-10 HP)')
        player['has_key'] = True
        player['hp'] -= 10
        if not check_hp(): return False

    print('\nВы вставляете ключ в тяжелую дверь Замок щелкает 🔓')
    print('1 — Осторожно приоткрыть и заглянуть')
    print('2 — Резко толкнуть дверь и вбежать')

    choice = get_choice(2)
    if choice == 2:
        print('Вы спотыкаетесь о порог в темноте (-10 HP) 💥')
        player['hp'] -= 10
        if not check_hp(): return False
    else:
        print('Вы аккуратно проходите внутрь 👣')

    return True


def corridor():
    print('\n Темный длинный коридор 🏃‍♂️ ')
    print('Вы шагаете по коридору Эхо ваших шагов разносится по стенам')
    print('Впереди видны два пути:')
    print('1 — Пойти по освещенному участку')
    print('2 — Срезать через темную нишу')

    choice = get_choice(2)
    if choice == 2:
        print('В темноте вы наступаете на острые обломки (-15 HP) 🩹')
        player['hp'] -= 15
        if not check_hp(): return False
    else:
        print('Вы спокойно проходите по свету и выходите к следующему залу')

    return True


def room_2():
    print('\n--- Вторая комната 🗝️ ---')
    steps = 2

    while steps > 0:
        print(f'\nОсталось пройти развилок: {steps}')
        print('1 — Повернуть налево\n2 — Повернуть направо')

        get_choice(2)
        idx = random.randint(0, len(events) - 1)
        print(f'Опасность на пути: {events[idx]}')
        player['hp'] -= damage[idx]

        if not check_hp():
            return False

        steps -= 1
        print(f'Осталось здоровья: {player["hp"]}')

    print('\nВы вышли из лабиринта!')
    return True


def room_3():
    print('\n--- Тупик 🕳️ ---')
    print('Пол трескается вы проваливаетесь в бездну 😱')
    print('\nВы резко открываете глаза у себя в кровати 🛏️')
    print('Авария и лабиринт были лишь сном 😅')
    print('ВЫ ПРОСНУЛИСЬ 🏆')


def start_game():
    print('Вы сбили человека на дороге! 🚗💥')
    print('1 — Уехать в панике\n2 — Вызвать полицию')

    choice = get_choice(2)
    if choice == 2:
        print('\nПриехала полиция вас задержали до суда 🚔')
        print('КОНЕЦ ИГРЫ (Закон есть закон) ⚖️')
        return

    print('\nВы в панике сворачиваете не туда и заходите в лабиринт 🏚️')

    if room_1() and corridor() and room_2():
        room_3()


if __name__ == '__main__':
    start_game()