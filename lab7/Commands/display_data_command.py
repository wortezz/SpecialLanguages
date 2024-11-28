from Commands.command import Command
from Core.user_interface import UserInterface
from colorama import Fore

class DisplayDataCommand(Command):
    def __init__(self, user_interface, data, data_type="posts"):
        self.user_interface = user_interface
        self.data = data
        self.data_type = data_type

    def execute(self):
        color = Fore.BLUE if self.data_type == "posts" else Fore.MAGENTA
        if self.data:
            self.user_interface.display_data(self.data, color=color)
        else:
            message = f"Дані для {self.data_type} відсутні."
            self.user_interface.display_message(message, color=Fore.RED)
