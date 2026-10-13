"""
Задание 7 (средняя сложность): Перегрузка оператора +.
Класс Vector поддерживает сложение векторов.
"""


class Vector:
    """Класс двумерного вектора с перегрузкой оператора +."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        """Перегрузка оператора + для сложения векторов."""
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        raise TypeError("Можно складывать только векторы с векторами")

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def __repr__(self):
        return self.__str__()


if __name__ == "__main__":
    v1 = Vector(2, 3)
    v2 = Vector(5, 7)
    v3 = v1 + v2

    print(f"{v1} + {v2} = {v3}")