from Commands.command import Command
from Core.user_interface import UserInterface
from colorama import Fore


class AddItemCommand(Command):
    def __init__(self, user_interface, history, remote_data, local_data, data_type="posts"):
        self.user_interface = user_interface
        self.history = history
        self.remote_data = remote_data
        self.local_data = local_data
        self.data_type = data_type

    def execute(self):
        try:
            user_id = int(input("Введіть ID користувача: "))
            title = input("Введіть заголовок: ")

            max_remote_id = max((item["id"] for item in self.remote_data), default=0)
            max_local_id = max((item["id"] for item in self.local_data if isinstance(item, dict) and "id" in item),default=0)
            new_item_id = max(max_remote_id, max_local_id) + 1

            new_item = {
                "userId": user_id,
                "id": new_item_id,
                "title": title
            }

            if self.data_type == "posts":
                new_item["body"] = input("Введіть текст: ")

            self.local_data.append(new_item)
            self.history.log_request(f"POST /{self.data_type}", new_item)
            self.user_interface.display_message("Новий запис додано!", color=Fore.GREEN)
        except ValueError:
            self.user_interface.display_message("Помилка введення даних. Спробуйте знову.", color=Fore.RED)

