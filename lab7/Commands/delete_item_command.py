from Commands.command import Command
from Core.user_interface import UserInterface
from colorama import Fore

class DeleteItemCommand(Command):
    def __init__(self, user_interface, history, local_data, data_type="posts"):
        self.user_interface = user_interface
        self.history = history
        self.local_data = local_data
        self.data_type = data_type

    def execute(self):
        try:
            delete_id = int(input(f"Введіть ID {self.data_type[:-1]} для видалення: "))
            item_to_delete = next((item for item in self.local_data if item["id"] == delete_id), None)
            if item_to_delete:
                self.local_data.remove(item_to_delete)
                self.history.log_request(f"DELETE /{self.data_type}", item_to_delete)
                self.user_interface.display_message(f"{self.data_type[:-1].capitalize()} з ID {delete_id} видалено!", color=Fore.GREEN)
            else:
                self.user_interface.display_message(f"{self.data_type[:-1].capitalize()} з ID {delete_id} не знайдено або не може бути видалено.", color=Fore.RED)
        except ValueError:
            self.user_interface.display_message("Помилка введення даних. Спробуйте знову.", color=Fore.RED)
