import os
import sys

lab7_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(lab7_root)

from Commands.load_data_command import LoadDataCommand
from Commands.display_data_command import DisplayDataCommand
from Commands.add_item_command import AddItemCommand
from Commands.delete_item_command import DeleteItemCommand
from Commands.save_data_command import SaveDataCommand
from Commands.show_history_command import ShowHistoryCommand, History
from Core.user_interface import UserInterface
from Core.data_saver import DataSaver

def main():
    user_interface = UserInterface()
    history = History()
    data_saver = DataSaver()

    posts = []
    local_posts = []
    albums = []
    local_albums = []

    while True:
        print("\n=== Меню ===")
        print("1. Завантажити дані")
        print("2. Відобразити пости")
        print("3. Додати новий пост")
        print("4. Видалити пост")
        print("5. Відобразити альбоми")
        print("6. Додати новий альбом")
        print("7. Видалити альбом")
        print("8. Зберегти пости у файл")
        print("9. Зберегти альбоми у файл")
        print("10. Показати історію")
        print("0. Вихід")

        choice = input("Оберіть опцію: ").strip()

        match choice:
            case "1":
                LoadDataCommand(user_interface, history, posts, albums).execute()
            case "2":
                DisplayDataCommand(user_interface, posts + local_posts, "posts").execute()
            case "3":
                AddItemCommand(user_interface, history, posts, local_posts, "posts").execute()
            case "4":
                DeleteItemCommand(user_interface, history, local_posts, "posts").execute()
            case "5":
                DisplayDataCommand(user_interface, albums + local_albums, "albums").execute()
            case "6":
                AddItemCommand(user_interface, history, albums, local_albums, "albums").execute()
            case "7":
                DeleteItemCommand(user_interface, history, local_albums, "albums").execute()
            case "8":
                SaveDataCommand(user_interface, data_saver, posts + local_posts, "posts").execute()
            case "9":
                SaveDataCommand(user_interface, data_saver, albums + local_albums, "albums").execute()
            case "10":
                ShowHistoryCommand(user_interface, history).execute()
            case "0":
                break
            case _:
                print("Неправильний вибір. Спробуйте ще раз.")



