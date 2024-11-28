class FontError(Exception):
    def __init__(self, font):
        self.message = f"Помилка: Невірний вибір шрифту '{font}'."
        super().__init__(self.message)

class ColorError(Exception):
    def __init__(self, color):
        self.message = f"Помилка: Невірний вибір кольору '{color}'."
        super().__init__(self.message)
