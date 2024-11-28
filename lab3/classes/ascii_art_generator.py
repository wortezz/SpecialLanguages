from art import text2art
from lab3.classes.error_handler import FontError
from lab3.classes.color_utils import ColorManager

class AsciiArtGenerator:
    def __init__(self):
        self.fonts = ["block", "starwars", "shadow", "banner3", "cyberlarge",
                      "caligraphy", "univers", "epic", "stellar"]

    def select_font(self):
        print("Доступні шрифти: ")
        for i, font in enumerate(self.fonts):
            print(f"{i + 1}. {font}")
        font_choice = int(input("Виберіть шрифт за номером: ")) - 1
        if font_choice < 0 or font_choice >= len(self.fonts):
            raise FontError("Недійсний вибір")
        return self.fonts[font_choice]

    def generate_ascii_art(self, text, font, symbol):
        ascii_art = text2art(text, font=font)
        art_lines = ascii_art.splitlines()

        new_art = []

        for line in art_lines:
            new_line = ' '.join(symbol if char != ' ' else ' ' for char in line)
            new_art.append(new_line)

        return "\n".join(new_art)

