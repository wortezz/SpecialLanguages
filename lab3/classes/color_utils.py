from colorama import Fore, init
from lab3.classes.error_handler import ColorError

init(autoreset=True)

class ColorManager:
    def select_color(self):
        colors = {
            'red': Fore.RED,
            'green': Fore.GREEN,
            'yellow': Fore.YELLOW,
            'blue': Fore.BLUE,
            'magenta': Fore.MAGENTA,
            'cyan': Fore.CYAN,
            'white': Fore.WHITE
        }
        print("Доступні кольори:", ", ".join(colors.keys()))
        color_choice = input("Виберіть колір: ").lower()
        if color_choice not in colors:
            raise ColorError(color_choice)
        return colors[color_choice]
