class AsciiArtSettings:
    def preview_ascii_art(self, art, color):
        print(color + art)

    def preview_and_change_symbol(self, ascii_art, color, user_text, selected_font, art_generator):
        while True:
            self.preview_ascii_art(ascii_art, color)

            change_symbol = input("Бажаєте змінити символ? (так/ні): ").strip().lower()
            if change_symbol == 'так':
                custom_symbol = input("Введіть новий символ: ")
                ascii_art = art_generator.generate_ascii_art(user_text, selected_font, custom_symbol)
            else:
                break
        return ascii_art

    def change_size(self, ascii_art, art_service, color):
        width = int(input("Введіть бажану ширину (0 для оригінального розміру): ") or 0)
        height = int(input("Введіть бажану висоту (0 для оригінального розміру): ") or 0)

        resized_art = self.resize_ascii_art(ascii_art, width, height)
        print("Попередній перегляд з новим розміром:")
        self.preview_ascii_art(resized_art, color)

        return resized_art

    def resize_ascii_art(self, ascii_art, width, height):
        if width < 0 or height < 0:
            raise ValueError("Ширина і висота повинні бути додатними.")

        lines = ascii_art.splitlines()
        resized_lines = []
        for line in lines:
            if width > 0:
                new_line = ''.join(char * width if char != ' ' else ' ' * width for char in line)
            else:
                new_line = line
            resized_lines.append(new_line)
        if height > 0:
            resized_lines = [line for line in resized_lines for _ in range(height)]
            resized_lines = resized_lines[:height * len(lines)]

        return '\n'.join(resized_lines)
