ch1 = int(input("Ведіть перше число"))
ch2= int(input("Ведіть друге число"))
ch3= int(input("Ведіть третє число"))


def check(ch1, ch2, ch3):
    if ch1 %5 == 0:
        if ch2 %5 == 0:
            if ch3 %5 == 0:
                sp = [ch1, ch2, ch3]
                sp.sort()
                print(sp)
            else:
                raise TypeError("Не правильне Третє число, всі мають ділитися на 5")
        else:
            raise TypeError("Не правильне Друге число, всі мають ділитися на 5")
    else:
        raise TypeError("Не правильне Перше число, всі мають ділитися на 5")
try:
    check(ch1, ch2, ch3)

except TypeError:
    print("Введено не правильні числа")