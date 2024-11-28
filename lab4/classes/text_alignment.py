class TextAlignment:
    def __init__(self):
        self._alignment = "left"

    def set_alignment(self):
        print("Виберіть вирівнювання тексту:")
        print("1. Зліва")
        print("2. По центру")
        print("3. Справа")
        alignment_option = input("Виберіть варіант (1, 2 або 3): ").strip()

        if alignment_option == '1':
            self._alignment = 'left'
        elif alignment_option == '2':
            self._alignment = 'center'
        elif alignment_option == '3':
            self._alignment = 'right'
        else:
            self._alignment = 'left'
            raise ValueError("Недійсний варіант. За замовчуванням вибрано ліве вирівнювання.")

    def align_line(self, line, width):
        if self._alignment == 'left':
            return line.ljust(width)
        elif self._alignment == 'center':
            return line.center(width)
        elif self._alignment == 'right':
            return line.rjust(width)
        else:
            return line
