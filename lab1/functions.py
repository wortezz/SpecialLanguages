import math

from Shared.constants.GlobalVariables import history
from Shared.decimal_settings.settings import DecimalSettings
from Shared.validators.math_utils import validate_operator
decimal_settings = DecimalSettings()
def set_memory_value(result):
    global memory_value
    memory_value = result

def get_memory_value():
    return memory_value

def calculate(num1, num2, operator):
    try:
        if operator == '+':
            return num1 + num2
        elif operator == '-':
            return num1 - num2
        elif operator == '*':
            return num1 * num2
        elif operator == '/':
            if num2 == 0:
                raise ZeroDivisionError("Ділення на нуль не дозволено")
            return num1 / num2
        elif operator == '^':
            return num1 ** num2
        elif operator == '%':
            if num2 == 0:
                raise ZeroDivisionError("Ділення на нуль не дозволено")
            return num1 % num2
        elif operator == '√':
            if num1 < 0:
                raise ValueError("Квадратний корінь з від'ємного числа не дозволений")
            return math.sqrt(num1)
        raise ZeroDivisionError
    except ZeroDivisionError as e:
        return e
    except ValueError as e:
        return e

def get_input():
    while True:
        num1_input = input("Введіть перше число або 'm' для використання пам'яті: ").lower()
        if num1_input == 'm' and get_memory_value() is not None:
            num1 = get_memory_value()
            print(f"Використано число з пам'яті: {num1}")
            break
        elif num1_input == 'm' and get_memory_value() is None:
            print("Помилка: пам'ять порожня.")
        else:
            try:
                num1 = float(num1_input)
                break
            except ValueError:
                print("Помилка: введіть дійсне число або 'm'.")

    operator = input("Введіть оператор (+, -, *, /, ^, %, √): ")
    while not validate_operator(operator):
        print("Неправильний оператор! Спробуйте ще раз.")
        operator = input("Введіть оператор (+, -, *, /, ^, %, √): ")

    num2 = None
    if operator != '√':
        while True:
            num2_input = input("Введіть друге число або 'm' для використання пам'яті: ").lower()
            if num2_input == 'm' and get_memory_value() is not None:
                num2 = get_memory_value()
                print(f"Використано число з пам'яті: {num2}")
                break
            elif num2_input == 'm' and get_memory_value() is None:
                print("Помилка: пам'ять порожня.")
            else:
                try:
                    num2 = float(num2_input)
                    break
                except ValueError:
                    print("Помилка: введіть дійсне число або 'm'.")
    return num1, num2, operator

def memory_store(result):
    return result

def ask_for_another_calculation():
    while True:
        again = input("Бажаєте виконати ще одне обчислення? (y/n): ").lower()
        if again == 'y':
            return True
        elif again == 'n':
            return False
        else:
            print("Неправильний вибір, спробуйте знову.")

def perform_calculation():

    while True:
        num1, num2, operator = get_input()
        result = calculate(num1, num2 if operator != '√' else None, operator)
        expression = f"{num1} {operator} {num2}" if operator != '√' else f"√{num1}"

        if isinstance(result, (int, float)):
            result = round(result, decimal_settings.get_decimal_precision())

        history.append(f"{expression} = {result}")
        print(f"Результат: {result}")
        if isinstance(result, (int, float)):
            memory_choice = input("Зберегти результат у пам'яті? (y/n): ").lower()
            if memory_choice == 'y':
                set_memory_value(result)
                print(f"Результат {result} збережено в пам'ять.")
        else:
            print("Помилка не може бути збережена в пам'ять.")

        if not ask_for_another_calculation():
            break

def validate_operator(operator):
    return operator in ['+', '-', '*', '/', '^', '%', '√']

def show_memory():
    if get_memory_value() is not None:
        print(f"Збережене в пам'яті число: {get_memory_value()}")
    else:
        print("Пам'ять порожня.")

def show_history():
    if history:
        print("Історія обчислень:")
        for record in history:
            print(record)
    else:
        print("Історія порожня.")

def exit_calculator():
    print("Дякуємо за використання калькулятора!")
    return True

def main():
    while True:
        print("\n--- Меню ---")
        print("1. Виконати нове обчислення")
        print("2. Переглянути історію обчислень")
        print("3. Змінити кількість знаків після коми")
        print("4. Очистити число збережене в пам'яті")
        print("5. Показати збережене число в пам'яті")
        print("6. Вийти\n")
        choice = input("Оберіть дію (1, 2, 3, 4, 5, 6): ")

        match choice:
            case '1':
                perform_calculation()
            case '2':
                show_history()
            case '3':
                decimal_settings.set_decimal_precision()
                print(f"Кількість знаків після коми змінено на {decimal_settings.get_decimal_precision()}.")
            case '4':
                set_memory_value(0)
                print("Збережене значення очищено")
            case '5':
                show_memory()
            case '6':
                if exit_calculator():
                    break
            case _:
                print("Невірний вибір, спробуйте знову.")

