import random


class Student:
    def __init__(self, name):
        self.name = name
        self.knowledge = random.randint(5, 20)
        self.energy = 100
        self.happiness = random.randint(40, 100)
        self.homework_done = 0
        self.status = random.randint(5, 30)

    def study(self):
        if self.energy > 10:
            self.knowledge += random.randint(5, 15)
            self.energy -= 10
            self.status -= 2.5
            self.happiness -= 15
            print(
                f"{self.name} учится! Знания: {self.knowledge}, Энергия: {self.energy}, Счастье: {self.happiness}, Статус: {self.status}")
        else:
            print(f"{self.name} слишком устал, чтобы учиться.")

    def do_homework(self):
        if self.energy > 15:
            self.homework_done += 1
            self.knowledge += random.randint(2, 10)
            self.energy -= 15
            self.status -= 0
            self.happiness -= 15
            print(
                f"{self.name} сделал домашнее задание! Знания: {self.knowledge}, Энергия: {self.energy}, Счастье: {self.happiness}, Статус: {self.status}")
        else:
            print(f"{self.name} слишком устал для домашней работы.")

    def rest(self):
        self.energy += 20
        self.happiness += 10
        print(f"{self.name} отдыхает. Энергия: {self.energy}, Счастье: {self.happiness}")

    def talk_to_teacher(self):
        self.knowledge += random.randint(5, 10)
        self.status += 10
        self.energy -= 20
        print(f"{self.name} поговорил с учителем. Знания: {self.knowledge}, Статус: {self.status}")

    def talk_to_classmates(self):
        self.happiness += 10
        self.status += 15
        self.energy -= 20
        self.knowledge -= random.randint(0, 10)
        print(f"{self.name} пообщался с одноклассниками. Счастье: {self.happiness}, Статус: {self.status}")

    def check_parameters(self):
        print(
            f"Параметры {self.name}: Знания - {self.knowledge}, Энергия - {self.energy}, Счастье - {self.happiness}, ДЗ выполнено - {self.homework_done}, Статус - {self.status}")

    def check_game_over(self):
        if self.energy < 1:
            print(f"{self.name} полностью вымотан и потерял сознание! Игра окончена.")
            return True
        if self.happiness < 1:
            print(f"{self.name} впал в депрессию! Игра окончена.")
            return True
        if self.status < 1:
            print(f"{self.name} тебя не счетают часть колектива! Игра окончена.")
            return True
        if self.knowledge > 500:
            print(f"Поздравляем! {self.name} стал гением и выиграл игру! 🎉")
            return True
        return False


def main():
    name = input("Введите имя школьника: ")
    student = Student(name)

    while True:
        if student.check_game_over():
            break

        print("\nВыберите действие:")
        print("1 - Учиться")
        print("2 - Делать домашку")
        print("3 - Отдыхать")
        print("4 - Поговорить с учителем")
        print("5 - Поговорить с одноклассниками")
        print("6 - Проверить параметры")
        print("7 - Выйти из симулятора")

        choice = input("Ваш выбор: ")

        if choice == "1":
            student.study()
        elif choice == "2":
            student.do_homework()
        elif choice == "3":
            student.rest()
        elif choice == "4":
            student.talk_to_teacher()
        elif choice == "5":
            student.talk_to_classmates()
        elif choice == "6":
            student.check_parameters()
        elif choice == "7":
            print("Выход из симулятора. До свидания!")
            break
        else:
            print("Неверный выбор, попробуйте снова.")


if __name__ == "__main__":
    main()
