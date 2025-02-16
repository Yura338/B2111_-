def checker(function, *args, **kwargs):
    def checker(*args, **kwargs):
        try:
            result = function(*args, **kwargs)
        except Exception as exs:
            print(f"We have a problem - {exs}")
        else:
            print(f"No problem - {result}")

    return checker


def calculate(expression):
    return eval(expression)


calculate = checker(calculate)
calculate("2+2")
