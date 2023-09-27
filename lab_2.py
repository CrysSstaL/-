class Fract:
    # инициализация данных в классе
    # используем магические методы!
    def __init__(self, num, denom):
        self.num = num
        self.denom = denom

    def __str__(self): # вызывается print (чтобы печетались данные, а не обьекты)
        return str(self.num)+'/'+str(self.denom)

    def decimal_fract(self): # перевод в десячиную дробь
        return round(self.num / self.denom, 6)

    def __add__(self, other):  # сложение
        new_num = self.num * other.denom + other.num * self.denom
        new_denom = self.denom * other.denom
        degree = reduction(new_num, new_denom)
        return Fract(new_num//degree, new_denom//degree)

    def __sub__(self, other):  # вычитание
        new_num = self.num * other.denom - other.num * self.denom
        new_denom = self.denom * other.denom
        degree = reduction(new_num, new_denom)
        return Fract(new_num//degree, new_denom//degree)

    def __mul__(self, other): # умножение
        new_num = self.num * other.num
        new_denom = self.denom * other.denom
        degree = reduction(new_num, new_denom)
        return Fract(new_num//degree, new_denom//degree)

    def __floordiv__(self, other): # деление
        new_num = self.num * other.denom
        new_denom = self.denom * other.num
        degree = reduction(new_num, new_denom)
        return Fract(new_num//degree, new_denom//degree)

    #   Сравнение дробей
    def __ne__(self, other): # проверка на неравенство
        return (self.num * other.denom) != (other.num * self.denom)

    def __eq__(self, other): # проверка на равенство
        return (self.num * other.denom) == (other.num * self.denom)

    def __gt__(self, other): # проверка на 1 дробь > 2 дробь
        return str(self.num * other.denom) > str(other.num * self.denom)

    def __lt__(self, other): # проверка на 1 дробь < 2 дробь
        return self.num * other.denom < other.num * self.denom


def reduction(m, n): # НОД для сокращения дробей
    while m % n != 0:
        m, n = n, m % n
    return n


if __name__ == "__main__":
    f1 = Fract(int(input()), int(input()))
    f2 = Fract(int(input()), int(input()))
    print(f" f1 = {f1}   f2 = {f2} ")
    print(f" Сумма = {f1 + f2}")
    print(f" Десятичная дробь от суммы = {(f1 + f2).decimal_fract()}")
    print(f" Разность = {f1 - f2}")
    print(f" Произведение = {f1 * f2}")
    print(f" Деление = {f1 // f2}")
    print(f" Функция f1 не равна f2 = {f1 != f2}")
    print(f" Функция f1 равна f2 = {f1 == f2}")
    print(f" Функция f1 больше f2 = {f1 > f2}")
    print(f" Функция f1 меньше f2 = {f1 < f2}")
