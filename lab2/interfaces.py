import os
import sys

lab2_root = os.path.abspath(os.path.join(os.path.dirname(__file__)))
sys.path.append(lab2_root)

from classes import Calculator

def main():
    calc = Calculator()
    while True:
        print("\n--- Меню ---")
        print("1. Виконати нове обчислення")
        print("2. Переглянути історію обчислень")
        print("3. Змінити кількість знаків після коми")
        print("4. Очистити пам'ять")
        print("5. Показати збережене число в пам'яті")
        print("6. Вийти\n")

        choice = input("Оберіть дію (1, 2, 3, 4, 5, 6): ")

        match choice:
            case '1':
                try:
                    calc.perform_calculation()
                except ZeroDivisionError as e:
                    print(e)
                except ValueError as e:
                    print(e)
                else:
                    if not calc.ask_for_another_calculation():
                        continue
            case '2':
                calc.history.show_history()
            case '3':
                try:
                    calc.settings.set_decimal_precision()
                except ValueError as e:
                    print(e)
                except TypeError as e:
                    print(e)
            case '4':
                calc.memory.clear_memory()
            case '5':
                calc.memory.show_memory()
            case '6':
                print("Дякуємо за використання калькулятора!")
                break
            case _:
                print("Невірний вибір, спробуйте знову.")
