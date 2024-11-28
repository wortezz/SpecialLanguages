import os
import sys

lab3_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(lab3_root)

from lab3.classes.ascii_art_generator import AsciiArtGenerator
from lab3.classes.ascii_art_settings import AsciiArtSettings
from lab3.classes.color_utils import ColorManager
from lab3.classes.file_saver import FileManager
from lab3.classes.error_handler import FontError, ColorError

def main():
    ascii_art_generator = AsciiArtGenerator()
    ascii_art_service = AsciiArtSettings()
    color_manager = ColorManager()
    file_manager = FileManager()

    while True:
        print("\n--- Меню ---")
        print("1. Створити ASCII арт")
        print("2. Вихід")
        choice = input("Виберіть опцію: ")

        match choice:
            case '1':
                try:
                    user_text = input("Введіть слово або фразу для перетворення на ASCII-арт: ")
                    selected_font = ascii_art_generator.select_font()
                    selected_color = color_manager.select_color()
                    custom_symbol = input("Введіть символ, який використати в ASCII-арт: ")

                    ascii_art = ascii_art_generator.generate_ascii_art(user_text, selected_font, custom_symbol)
                    ascii_art = ascii_art_service.preview_and_change_symbol(
                        ascii_art, selected_color, user_text, selected_font, ascii_art_generator)

                    change_size = input("Бажаєте змінити розмір ASCII-арту? (так/ні): ").strip().lower()
                    if change_size == 'так':
                        ascii_art = ascii_art_service.change_size(ascii_art, ascii_art_generator, selected_color)

                    save_option = input("Бажаєте зберегти ASCII-арт у файл? (так/ні): ").strip().lower()
                    if save_option == 'так':
                        file_manager.save_to_file(ascii_art)

                except (FontError, ColorError) as error:
                    print(error.message)
                except ValueError:
                    print("Помилка: Введено невірне значення. Будь ласка, спробуйте ще раз.")

            case '2':
                print("Вихід з генератора ASCII-арту!")
                break

            case _:
                print("Неправильний вибір, спробуйте ще раз.")
