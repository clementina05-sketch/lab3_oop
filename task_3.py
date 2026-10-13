"""
Задание 1 (средняя сложность): Класс «Книга» с полями «название», «автор».
"""


class Book:
    """Класс, представляющий книгу."""

    def __init__(self, title, author, year=None):
        """Инициализация книги."""
        self.title = title
        self.author = author
        self.year = year

    def display_info(self):
        """Выводит информацию о книге."""
        info = f"Книга: '{self.title}', Автор: {self.author}"
        if self.year:
            info += f", Год: {self.year}"
        return info

    def __str__(self):
        """Строковое представление объекта."""
        return self.display_info()


if __name__ == "__main__":
    book1 = Book("Мастер и Маргарита", "Михаил Булгаков", 1967)
    book2 = Book("1984", "Джордж Оруэлл")

    print(book1)
    print(book2)