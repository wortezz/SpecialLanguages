import os
from lab4.classes.color_utils import ColorUtils
from lab4.classes.text_alignment import TextAlignment

class ASCIIGenerator:
    def __init__(self):
        self._char_set = {}
        self._load_characters()
        self._width = 0
        self._height = 0
        self._text = ""
        self._color = ""
        self.ascii_art = None
        self.color_utils = ColorUtils()
        self._alignment = TextAlignment()

    def _load_characters(self):
        for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#_+-:,. ":
            if char.isupper():
                filename = f"../Lab4/config/alphabets/{char}{char}.txt"
            elif char.islower():
                filename = f"../Lab4/config/alphabets/{char}.txt"
            elif char.isdigit():
                filename = f"../Lab4/config/numbers/{char}.txt"
            else:
                filename = f"../Lab4/config/symbols/{char}.txt"

            if os.path.exists(filename):
                with open(filename, 'r') as file:
                    self._char_set[char] = [line.rstrip('\n') for line in file.readlines()]
            else:
                self._char_set[char] = [' ' * 10] * 10

    def generate_art(self):
        ascii_lines = ['' for _ in range(self._height)]
        for char in self._text:
            if char in self._char_set:
                char_lines = self._char_set[char]
            else:
                char_lines = [' ' * self._width] * self._height

            if len(char_lines) < self._height:
                char_lines += [' ' * self._width] * (self._height - len(char_lines))

            for i in range(self._height):
                ascii_lines[i] += char_lines[i] + ' '
        return ascii_lines

    def generate_colored_art(self):
        if self.ascii_art is None:
            return []
        colored_lines = []
        color_code = self._color
        for line in self.ascii_art:
            colored_lines.append(f"{color_code}{line}{self.color_utils.reset_color()}")
        return colored_lines

    def display_art(self, ascii_art):
        if ascii_art is None:
            raise ValueError("ASCII-арт відсутній, створіть його!")
        else:
            for line in ascii_art:
                aligned_line = self._alignment.align_line(line, self._width * len(self._text))
                print(aligned_line)
