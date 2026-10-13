"""
Задание 5 (средняя сложность): Наследование «Животное» → «Собака».
"""


class Animal:
    """Базовый класс животного."""

    def __init__(self, name):
        self.name = name

    def speak(self):
        """Издает звук. Переопределяется в наследниках."""
        return "..."

    def __str__(self):
        return f"Животное: {self.name}"


class Dog(Animal):
    """Класс собаки, наследник Animal."""

    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        """Собака говорит Гав."""
        return f"{self.name} говорит Гав!"

    def __str__(self):
        return f"Собака: {self.name}, Порода: {self.breed}"


if __name__ == "__main__":
    animal = Animal("Неизвестное")
    dog = Dog("Шарик", "Лабрадор")

    print(animal.speak())
    print(dog.speak())
    print(dog)