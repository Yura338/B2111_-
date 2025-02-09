ch1 = float(input("Ведіть перше число"))
ch2= float(input("Ведіть друге число"))


try:
    result = ch1/ch2
    print(result)
except:
    print(f"Ви намагалися поділити {ch1} на {ch2} і отримали помилку")
    if ch2 == 0:
        print("На нуль ділити не можна")
else:
    print("Розрахунки завершені")
