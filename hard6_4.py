import math

class Figure:
    def __init__(self, color, *sides):
        self.__color = color
        self.filled = False
        self.__sides = []
        if sides and self.__is_valid_sides(*sides):
            self.set_sides(*sides)  # Устанавливаем стороны
        else:
            self.set_sides(*[1] * self.sides_count)  # Установка сторон по умолчанию

    def __is_valid_color(self, r, g, b):
        return all(isinstance(x, int) and 0 <= x <= 255 for x in (r, g, b))

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)

    def get_color(self):
        return list(self.__color)

    def __is_valid_sides(self, *new_sides):
        if len(new_sides) != self.sides_count:
            return False
        return all(isinstance(side, int) and side > 0 for side in new_sides)

    def get_sides(self):
        return list(self.__sides)

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

class Circle(Figure):
    def __init__(self, color, *sides):
        self.sides_count = 1  # Круг имеет 1 сторону (длина окружности)
        super().__init__(color, *sides)

    @property
    def __radius(self):
        return self.get_sides()[0]  # радиус круга

    def get_square(self):
        return math.pi * (self.__radius ** 2)

class Triangle(Figure):
    def __init__(self, color, *sides):
        self.sides_count = 3  # Треугольник имеет 3 стороны
        super().__init__(color, *sides)

    def get_square(self):
        # Использование формулы Герона
        a, b, c = self.get_sides()
        s = sum(self.get_sides()) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))

class Cube(Figure):
    def __init__(self, color, *sides):
        self.sides_count = 12  # Куб имеет 12 рёбер
        super().__init__(color, *sides)

        # Установка рёбер куба
        if len(sides) == 1:  # Если передано одно значение (длина ребра)
            self.set_sides(*[sides[0]] * self.sides_count)  # Все рёбра равны этому значению
        else:
            self.set_sides(*[1] * self.sides_count)  # Все рёбра равны 1 по умолчанию

    def get_volume(self):
        return self.get_sides()[0] ** 3  # Объём куба

# Пример для проверки
circle1 = Circle((200, 200, 100), 10)  # (Цвет)
cube1 = Cube((222, 35, 130), 6)  # Устанавливаем цвет и количество рёбер

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())  # Ожидается: [55, 66, 77]
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())  # Ожидается: [222, 35, 130]

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится, так как количество сторон не равно 12
print(cube1.get_sides())  # Ожидается: [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())  # Ожидается: [15]

# Проверка периметра (круга), это длина:
print(len(circle1))  # Это будет 15 (длина окружности)

# Проверка объёма (куба):
print(cube1.get_volume())  # Это будет 6**3 = 216