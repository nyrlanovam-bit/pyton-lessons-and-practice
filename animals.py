class Animal:
    def __init__(self, name, age, color, habitat, food):
        self.name = name
        self.age = age
        self.color = color
        self.habitat = habitat
        self.food = food

    def eat(self):
        print(f"{self.name} ест: {self.food}")

    def show_info(self):
        print(f"Имя: {self.name}")
        print(f"Возраст: {self.age} лет")
        print(f"Цвет: {self.color}")
        print(f"Среда обитания: {self.habitat}")


class Reptile(Animal):
    def __init__(self, name, age, color, habitat, food,
                 skin_type, trick):
        super().__init__(name, age, color, habitat, food)
        self.skin_type = skin_type
        self.trick = trick

    def climb(self):
        print(f"{self.name} карабкается по искусственной скале!")

    def perform_trick(self):
        print(f"{self.name} выполняет трюк: {self.trick}!")


class Amphibian(Animal):
    def __init__(self, name, age, color, habitat, food,
                 skin_moisture, jump_length):
        super().__init__(name, age, color, habitat, food)
        self.skin_moisture = skin_moisture
        self.jump_length = jump_length

    def jump(self):
        print(f"{self.name} прыгает на {self.jump_length} метра!")

    def underwater_show(self):
        print(f"{self.name} выполняет подводный разворот!")


class ZooShow:
    def __init__(self):
        self.reptiles = [
            Reptile(
                "Торнадо — Python", 6, "коричневый",
                "Тропический террариум", "мыши",
                "чешуйчатая кожа",
                "проходит через кольца и тоннель"
            ),
            Reptile(
                "Рокки — Iguana", 4, "зелёный",
                "Зелёный вольер", "растения",
                "чешуйчатая кожа",
                "карабкается на вершину скалы"
            ),
            Reptile(
                "Капитан Панцирь — Turtle", 12, "зелёный",
                "Солнечная поляна", "растения",
                "панцирь",
                "проходит лабиринт и находит флаг"
            )
        ]

        self.amphibians = [
            Amphibian(
                "Прыг-Скок — Frog", 3, "зелёный",
                "Болото", "насекомые",
                "влажная кожа", 2.5
            ),
            Amphibian(
                "Бум — Toad", 5, "коричневый",
                "Лесной водоём", "насекомые",
                "влажная кожа", 1.2
            ),
            Amphibian(
                "Аква — Newt", 2, "оранжевый",
                "Подводный грот", "мелкие беспозвоночные",
                "влажная кожа", 0.8
            )
        ]

        self.regular_price = 800
        self.vip_price = 3000

    def start(self):
        print("\n" + "=" * 50)
        print("       ДОБРО ПОЖАЛОВАТЬ В ДЖУНГЛИ-ШОУ!")
        print("=" * 50)

        print("\nВыберите представление:")
        print("1. Ящеры против гравитации")
        print("2. Прыжок в приключение")

        choice = input("\nВаш выбор (1/2): ")

        if choice == "1":
            animals = self.reptiles
            title = "ЯЩЕРЫ ПРОТИВ ГРАВИТАЦИИ"
        elif choice == "2":
            animals = self.amphibians
            title = "ПРЫЖОК В ПРИКЛЮЧЕНИЕ"
        else:
            print("Ошибка! Такого шоу нет.")
            return

        print("\n" + "=" * 50)
        print(f"       ПРОГРАММА: {title}")
        print("=" * 50)

        for animal in animals:
            print()
            animal.show_info()
            animal.eat()

            if isinstance(animal, Reptile):
                animal.climb()
                animal.perform_trick()
            elif isinstance(animal, Amphibian):
                animal.jump()
                animal.underwater_show()

            print("-" * 50)

        print("\n" + "=" * 50)
        print("              БИЛЕТНАЯ КАССА")
        print("=" * 50)
        print(f"1. Обычное место — {self.regular_price} сом")
        print(f"2. VIP-место у сцены — {self.vip_price} сом")

        try:
            count = int(input("\nСколько билетов хотите купить? "))

            if count <= 0:
                print("Количество билетов должно быть больше нуля!")
                return

        except ValueError:
            print("Ошибка! Введите количество целым числом.")
            return

        seat = input("Выберите место (1 или 2): ")

        if seat == "1":
            seat_name = "Обычное место"
            price = self.regular_price
        elif seat == "2":
            seat_name = "VIP-место у сцены"
            price = self.vip_price
        else:
            print("Ошибка! Такого места нет.")
            return

        total = count * price

        print("\n" + "=" * 50)
        print("              ВАШ БИЛЕТ")
        print("=" * 50)
        print(f"Название шоу: {title}")
        print(f"Место: {seat_name}")
        print(f"Количество билетов: {count}")
        print(f"Цена одного билета: {price} сом")
        print(f"ИТОГО К ОПЛАТЕ: {total} сом")
        print("=" * 50)

        print(f"\nСЕГОДНЯ НА СЦЕНЕ — «{title}»!")

        for animal in animals:
            print(f"Звезда шоу: {animal.name}")

        print("\nВас ждут невероятные трюки,")
        print("захватывающие прыжки и удивительные приключения!")
        print("Спасибо за покупку! Приятного просмотра!")


zoo = ZooShow()
zoo.start()
           

