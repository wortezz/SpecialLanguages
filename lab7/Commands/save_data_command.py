from Commands.command import Command
from Core.data_saver import DataSaver
from Core.user_interface import UserInterface

class SaveDataCommand(Command):
    def __init__(self, user_interface, data_saver, data, data_type="posts"):
        self.user_interface = user_interface
        self.data_saver = data_saver
        self.data = data
        self.data_type = data_type

    def execute(self):
        format_choice = input(f"Виберіть формат для збереження {self.data_type} (JSON, CSV, TXT): ").strip().lower()
        filename = f"{self.data_type}.{format_choice}"
        self.data_saver.save_data(self.data, filename, format_choice)
