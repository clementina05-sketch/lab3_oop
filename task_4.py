"""
Задание 6 (повышенная сложность): Наследование от встроенного списка
с дополнительными методами.
"""


class NumberList(list):
    """Список чисел с дополнительными методами."""

    def sum(self):
        """Возвращает сумму всех элементов."""
        return sum(self)

    def average(self):
        """Возвращает среднее арифметическое."""
        if not self:
            return 0
        return sum(self) / len(self)

    def max_element(self):
        """Возвращает максимальный элемент."""
        if not self:
            return None
        return max(self)

    def min_element(self):
        """Возвращает минимальный элемент."""
        if not self:
            return None
        return min(self)


if __name__ == "__main__":
    numbers = NumberList([4, 8, 15, 16, 23, 42])

    print(f"Список: {numbers}")
    print(f"Сумма: {numbers.sum()}")
    print(f"Среднее: {numbers.average():.2f}")
    print(f"Максимум: {numbers.max_element()}")
    print(f"Минимум: {numbers.min_element()}")
