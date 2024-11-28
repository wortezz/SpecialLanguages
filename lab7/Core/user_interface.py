from tabulate import tabulate
from colorama import Fore, Style

class UserInterface:
    @staticmethod
    def display_data(data, color=Fore.GREEN):
        print(color + tabulate(data, headers="keys", tablefmt="grid") + Style.RESET_ALL)

    @staticmethod
    def display_message(message, color=Fore.CYAN):
        print(color + message + Style.RESET_ALL)
