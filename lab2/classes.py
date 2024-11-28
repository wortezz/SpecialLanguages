import math
from abc import ABC, abstractmethod
from Shared.constants.GlobalVariables import memory_value, history
from Shared.decimal_settings.settings import DecimalSettings
from Shared.validators.math_utils import validate_operator

class CalculatorInterface(ABC):
    @abstractmethod
    def perform_calculation(self):
        pass

    @abstractmethod
    def ask_for_another_calculation(self):
        pass

class BaseCalculator(CalculatorInterface):
    def __init__(self):
        self.memory = Memory()
        self.history = History()
        self.settings = DecimalSettings()

    def get_input(self):
        num1 = self._get_number_input("Введіть перше число або 'm' для використання пам'яті: ")
        operator = self._get_operator_input("Введіть оператор (+, -, *, /, ^, %, √): ")
        num2 = None if operator == '√' else self._get_number_input("Введіть друге число або 'm' для використання пам'яті: ")
        return num1, num2, operator

    def _get_number_input(self, prompt):
        while True:
            user_input = input(prompt).lower()
            if user_input == 'm' and self.memory.get_memory_value() is not None:
                print(f"Використано число з пам'яті: {self.memory.get_memory_value()}")
                return self.memory.get_memory_value()
            try:
                return float(user_input)
            except ValueError:
                print("Помилка: введіть дійсне число або 'm'.")

    def _get_operator_input(self, prompt):
        while True:
            operator = input(prompt)
            if validate_operator(operator):
                return operator
            else:
                print("Неправильний оператор! Спробуйте ще раз.")

    @staticmethod
    def calculate(num1, num2, operator, decimal_precision):
        match operator:
            case '+':
                result = num1 + num2
            case '-':
                result = num1 - num2
            case '*':
                result = num1 * num2
            case '/':
                if num2 == 0:
                    raise ZeroDivisionError("Ділення на нуль не дозволено")
                result = num1 / num2
            case '^':
                result = num1 ** num2
            case '%':
                if num2 == 0:
                    raise ZeroDivisionError("Ділення на нуль не дозволено")
                result = num1 % num2
            case '√':
                if num1 < 0:
                    raise ValueError("Квадратний корінь з від'ємного числа не дозволений")
                result = math.sqrt(num1)
            case _:
                raise ValueError("Неправильний оператор!")

        return round(result, decimal_precision)

class Calculator(BaseCalculator):
    def perform_calculation(self):
        num1, num2, operator = self.get_input()
        result = BaseCalculator.calculate(num1, num2, operator, self.settings.get_decimal_precision())
        expression = f"{num1} {operator} {num2}" if operator != '√' else f"√{num1}"
        print(f"Результат: {result}")
        self.history.add_to_history(expression, result)

        if isinstance(result, (int, float)):
            save_memory = input("Зберегти результат у пам'ять? (y/n): ").lower()
            if save_memory == 'y':
                self.memory.set_memory_value(result)
                print(f"Результат {result} збережено в пам'ять.")
            else:
                print("Результат не було збережено в пам'ять.")

    def ask_for_another_calculation(self):
        while True:
            again = input("Бажаєте виконати ще одне обчислення? (y/n): ").lower()
            if again == 'y':
                return True
            elif again == 'n':
                return False
            else:
                print("Неправильний вибір, спробуйте знову.")

class History:
    def __init__(self):
        self.__history = history

    def add_to_history(self, expression, result):
        self.__history.append(f"{expression} = {result}")

    def clear_history(self):
        self.__history = []

    def show_history(self):
        if self.__history:
            print("Історія обчислень:")
            for entry in self.__history:
                print(entry)
        else:
            print("Історія порожня.")

class Memory:
    def __init__(self):
        self.__memory_value = memory_value

    def get_memory_value(self):
        return self.__memory_value

    def set_memory_value(self, value):
        self.__memory_value = value

    def clear_memory(self):
        self.__memory_value = None
        print("Пам'ять очищено.")

    def show_memory(self):
        if self.__memory_value is not None:
            print(f"Збережене в пам'яті число: {self.__memory_value}")
        else:
            print("Пам'ять порожня.")

