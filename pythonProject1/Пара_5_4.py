import inspect


class Humman:
    def __init__(self, age, height, name='John'):
        self.age = age
        self.name = name
        self.secondname = 'Wick'


sig = inspect.signature(Humman)
for parameter in sig.parameters.values():
    print(parameter.name, parameter.default)