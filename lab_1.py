import sympy as sym
from sympy import *


# Абстрактный класс который не вызывается, а только инициализирует данные
class Abstract:
    # Инициализайия данных
    def __init__(self, function, delta_x, point):
        self.function = function
        self.delta_x = delta_x
        self.point = point
        self.f = lambdify(x, self.function)

    # переопредление print
    def __str__(self):
        return f"f(x) = {self.function} "


class Calc(Abstract):
    def right_p(self):
        # Формула правой производной через предел
        return round(sym.limit((self.f(x+self.delta_x) - self.f(x)) / self.delta_x, x, self.point, dir='+'), 5)

    def left_p(self):
        # Формула левой производной через предел
        # Альтернативная формула
        # sym.limit((self.f(x) - self.f(x-self.delta_x)) / self.delta_x, x, self.point)
        return round(sym.limit((self.f(x+self.delta_x) - self.f(x)) / self.delta_x, x, self.point, dir='-'), 5)

    def center_p(self):
        # Формула центральной производной через предел
        # Альтернативная формула
        # sym.limit((self.f(x+self.delta_x) - self.f(x-self.delta_x)) / 2*self.delta_x, x, self.point)
        return round(sym.limit((self.f(x+self.delta_x) - self.f(x)) / self.delta_x, x, self.point, dir='+-'), 5)

    def diff(self):
        return sym.diff(self.function, x)


if __name__ == '__main__':
    x = symbols('x')
    delta_x = 0.000000001
    function = 1/x + (3*x)**2 + 45
    point = 2
    a = Calc(function, delta_x, point)
    print(a)
    print(f"f'(x) = {a.diff()}")
    print(f"Проивзодная справа {a.right_p()}")
    print(f"Проивзодная слева {a.left_p()}")
    print(f"Проивзодная центральная {a.center_p()}")

