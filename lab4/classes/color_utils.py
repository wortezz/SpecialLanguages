import json

class ColorUtils:
    def __init__(self):
        self._load_colors()

    def _load_colors(self):
        with open('../Lab4/config/colors.json', 'r', encoding="utf8") as file:
            data = json.load(file)
            self._colors = data['colors']

    def get_color_code(self, color_name):
        return f"\033[{self._colors.get(color_name, '0')}m"

    def reset_color(self):
        return self.get_color_code("reset")

    def choose_color(self):
        print("Виберіть колір для ASCII-арту:")
        color_keys = list(self._colors.keys())
        for i, color in enumerate(color_keys, start=1):
            print(f"{i}. {color}")

        color_choice = input("Виберіть колір: ").strip()

        if color_choice.isdigit() and 1 <= int(color_choice) <= len(color_keys):
            selected_color = color_keys[int(color_choice) - 1]
            print(f"Обраний колір: {selected_color}")
            return self.get_color_code(selected_color)
        else:
            raise ValueError("Недійсний варіант. Використано стандартний колір.")

    @property
    def colors(self):
        return self._colors
