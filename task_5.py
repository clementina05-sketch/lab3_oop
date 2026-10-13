"""
Задание 8 (повышенная сложность): Класс с использованием property.
"""


class Temperature:
    """Класс для работы с температурой с использованием property."""

    def __init__(self, celsius=0):
        self._celsius = celsius

    @property
    def celsius(self):
        """Геттер для градусов Цельсия."""
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        """Сеттер с проверкой: не ниже абсолютного нуля."""
        if value < -273.15:
            raise ValueError("Температура не может быть ниже абсолютного нуля")
        self._celsius = value

    @property
    def fahrenheit(self):
        """Геттер для градусов Фаренгейта."""
        return self._celsius * 9 / 5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        """Сеттер для градусов Фаренгейта."""
        self.celsius = (value - 32) * 5 / 9

    def __str__(self):
        return f"{self._celsius}°C = {self.fahrenheit:.2f}°F"


if __name__ == "__main__":
    temp = Temperature(25)
    print(temp)

    temp.fahrenheit = 100
    print(f"После установки 100°F: {temp}")

    try:
        temp.celsius = -300
    except ValueError as e:
        print(f"Ошибка: {e}")