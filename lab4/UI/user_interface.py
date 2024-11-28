import os
import sys

lab4_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(lab4_root)

from lab4.classes.ascii_generator import ASCIIGenerator
from lab4.classes.file_saver import FileManager
from lab4.classes.text_alignment import TextAlignment
from lab4.classes.color_utils import ColorUtils

def main():
    file_manager = FileManager()
    generator = ASCIIGenerator()
    text_alignment = TextAlignment()

    while True:
        print("\nМеню:")
        print("1. Створити ASCII-арт")
        print("2. Вибрати колір для ASCII-арту")
        print("3. Вийти")

        choice = input("Виберіть варіант: ").strip()

        match choice:
            case '1':
                try:
                    generator._text = input("Введіть слово або фразу для перетворення в ASCII-арт: ")
                    generator._width = int(input("Введіть ширину для кожного символу: ") or 10)
                    generator._height = int(input("Введіть висоту для кожного символу: ") or 10)

                    ascii_art = generator.generate_art()
                    text_alignment.set_alignment()
                    generator._alignment = text_alignment
                    generator.display_art(ascii_art)
                    generator.ascii_art = ascii_art

                    print("Бажаєте зберегти ASCII-арт у файл?")
                    print("1. Так \n2. Ні")
                    save_option = input("Виберіть варіант (1 або 2): ").strip()

                    if save_option == '1':
                        file_manager.save_to_file(ascii_art)
                    elif save_option == '2':
                        print("ASCII-арт не збережено.")
                    else:
                        print("Недійсний варіант. ASCII-арт не збережено.")
                except ValueError as e:
                    print(e)

            case '2':
                try:
                    print("Ваш ASCII-арт: \n")
                    generator.display_art(generator.ascii_art)
                    chosen_color_code = generator.color_utils.choose_color()
                    generator._color = chosen_color_code
                    colored_art = generator.generate_colored_art()
                    generator.display_art(colored_art)
                except ValueError as e:
                    print(e)

            case '3':
                print("Вихід з програми.")
                break

            case _:
                print("Недійсний варіант. Спробуйте ще раз.")
