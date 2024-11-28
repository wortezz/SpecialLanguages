import os
import sys

lab8_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(lab8_root)

from Director.director import Director

def main(director):
    while True:
        print("\nОберіть дію:")
        print("1. Завантажити дані")
        print("2. Переглянути мінімальні та максимальні значення")
        print("3. Побудувати базову візуалізацію")
        print("4. Побудувати лінійний графік")
        print("5. Побудувати стовпчикову діаграму")
        print("6. Побудувати діаграму розсіювання")
        print("7. Побудувати порівняльний графік")
        print("8. Експортувати графік")
        print("0. Вийти")
        choice = input("Ваш вибір: ")

        match choice:
            case "1":
                file_path = input("Введіть шлях до CSV-файлу: ")
                director.load_data(file_path)
                director.process_data()
            case "2":
                director.explore_data()
            case "3":
                try:
                    director.create_basic_visualization()
                except KeyError as e:
                    print(e)
            case "4":
                director.create_line_chart()
            case "5":
                director.create_bar_chart()
            case "6":
                director.create_scatter_plot()
            case "7":
                director.create_combined_visualization()
            case "8":
                try:
                    filename = input("Введіть назву файлу для збереження: ")
                    file_format = input("Введіть формат файлу (png, jpg, svg): ")
                    director.export_visualization(filename, file_format)
                except ValueError as e:
                    print(e)
            case "0":
                print("Вихід з програми.")
                break
            case _:
                print("Невірний вибір. Спробуйте ще раз.")


