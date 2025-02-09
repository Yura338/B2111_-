def checker(var1):
    if type(var1) != str:
        raise TypeError(f"Я не можу працювати з таким типом даних - {type(var1)}, треба тип -str")
    else:
        return var1


my_var = 10
my_var2 = "vasya"
checker(my_var)
checker(my_var2)
