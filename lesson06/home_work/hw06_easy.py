# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.


class Triangle(object):
    label: str
    _dot_A: tuple
    _dot_B: tuple
    _dot_C: tuple

    def __init__(self, label):
        self.label = label

    def set_dots(self, dot_a, dot_b, dot_c):
        self._dot_A = dot_a
        self._dot_B = dot_b
        self._dot_C = dot_c

    @property
    def dot_a(self):
        return self._dot_A

    @property
    def dot_b(self):
        return self._dot_B

    @property
    def dot_c(self):
        return self._dot_C

    def len_ab(self):

        a = abs(self.dot_a[0] - self.dot_b[0]) ** 2
        b = abs(self.dot_a[1] - self.dot_b[1]) ** 2

        # Хотел организовать это в отдельную функцию но не понял как сделать так, чтобы она не была методом класса
        # или скрытым методом класса
        return round((a + b) ** (1/2), 2)

    def len_ac(self):

        a = abs(self.dot_a[0] - self.dot_c[0]) ** 2
        b = abs(self.dot_a[1] - self.dot_c[1]) ** 2

        return round((a + b) ** (1/2), 2)

    def len_bc(self):

        a = abs(self.dot_b[0] - self.dot_c[0]) ** 2
        b = abs(self.dot_b[1] - self.dot_c[1]) ** 2

        return round((a + b) ** (1/2), 2)

    def lengths(self):
        return [self.len_ab(), self.len_ac(), self.len_bc()]

    def perimeter(self):
        return round(sum(self.lengths()), 2)

    def half_per(self):
        return round(self.perimeter() / 2, 2)

    def altitude(self):

        h = self.half_per()
        a = h - self.len_ab()
        b = h - self.len_ac()
        c = h - self.len_bc()

        return round((2 / self.len_bc()) * (h * a * b * c) ** (1/2), 2)

    def area(self):
        return round(self.len_bc() * self.altitude() / 2, 2)


first = Triangle("first")
first.set_dots((0, 0), (2, 6), (8, 2))
print(first.lengths(), "", sep="\n")
print(first.perimeter(), first.altitude(), first.area(), sep="\n")


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

# При условии, что координаты вводятся последовательно по часовой стрелке


class IsoTrap(object):
    label: str
    _dot_A: tuple
    _dot_B: tuple
    _dot_C: tuple
    _dot_D: tuple

    def __init__(self, label):
        self.label = label

    def set_dots(self, dot_a, dot_b, dot_c, dot_d):
        self._dot_A = dot_a
        self._dot_B = dot_b
        self._dot_C = dot_c
        self._dot_D = dot_d

    @property
    def dot_a(self):
        return self._dot_A

    @property
    def dot_b(self):
        return self._dot_B

    @property
    def dot_c(self):
        return self._dot_C

    @property
    def dot_d(self):
        return self._dot_D

    def len_ab(self):

        a = abs(self.dot_a[0] - self.dot_b[0]) ** 2
        b = abs(self.dot_a[1] - self.dot_b[1]) ** 2

        return round((a + b) ** (1/2), 2)

    def len_bc(self):

        a = abs(self.dot_b[0] - self.dot_c[0]) ** 2
        b = abs(self.dot_b[1] - self.dot_c[1]) ** 2

        return round((a + b) ** (1/2), 2)

    def len_cd(self):

        a = abs(self.dot_c[0] - self.dot_d[0]) ** 2
        b = abs(self.dot_c[1] - self.dot_d[1]) ** 2

        return round((a + b) ** (1/2), 2)

    def len_ad(self):

        a = abs(self.dot_a[0] - self.dot_d[0]) ** 2
        b = abs(self.dot_a[1] - self.dot_d[1]) ** 2

        return round((a + b) ** (1/2), 2)

    def lengths(self):
        return [self.len_ab(), self.len_bc(), self.len_cd(), self.len_ad()]

    def flank(self):
        check = 0
        checks = self.lengths().copy()
        for i in checks:
            if checks.count(i) > 1:
                check = i
        return check

    def bases(self):
        check = []
        checks = self.lengths().copy()
        for i in checks:
            if checks.count(i) == 1:
                check.append(i)
        return check

    def perimeter(self):
        return round(sum(self.lengths()), 2)

    def check(self):
        if self.flank() == 0:
            return False
        else:
            return True

    def altitude(self):

        if self.check():

            if self.bases()[0] > self.bases()[1]:
                a = self.bases()[1]
                b = self.bases()[0]
            else:
                b = self.bases()[1]
                a = self.bases()[0]

            return round((self.flank() ** 2 - ((a - b) ** 2 / 4)) ** (1/2), 2)

        else:
            return "Не является равнобочным"

    def area(self):

        if self.check():
            return round(self.altitude() * sum(self.bases()) / 2, 2)
        else:
            return "Не является равнобочным"

second = IsoTrap("second")
second.set_dots((0, 0), (2, 3), (4, 3), (6, 0))
print("", "", second.lengths(), "", sep="\n")
print(second.perimeter(), second.altitude(), second.area(), sep="\n")

third = IsoTrap("third")
third.set_dots((0, 0), (2, 3), (4, 3), (6, 1))
print("", "", third.lengths(), "", sep="\n")
print(third.perimeter(), third.altitude(), third.area(), sep="\n")
