import unittest
from unittest import mock
import sys
import os
from classes import Calculator, BaseCalculator, CalculatorInterface, History, Memory
from Shared.validators.math_utils import validate_operator

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../lab2")))

class TestCalculatorOperations(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()
        self.calculator.settings.set_decimal_precision(2)

    def test_addition(self):
        self.assertEqual(self.calculator.calculate(10, 5, '+', self.calculator.settings.get_decimal_precision()), 15)
        self.assertEqual(self.calculator.calculate(-5, -10, '+', self.calculator.settings.get_decimal_precision()), -15)
        self.assertEqual(self.calculator.calculate(0, 0, '+', self.calculator.settings.get_decimal_precision()), 0)

    def test_subtraction(self):
        self.assertEqual(self.calculator.calculate(10, 5, '-', self.calculator.settings.get_decimal_precision()), 5)
        self.assertEqual(self.calculator.calculate(-10, -5, '-', self.calculator.settings.get_decimal_precision()), -5)
        self.assertEqual(self.calculator.calculate(5, 10, '-', self.calculator.settings.get_decimal_precision()), -5)

    def test_multiplication(self):
        self.assertEqual(self.calculator.calculate(3, 5, '*', self.calculator.settings.get_decimal_precision()), 15)
        self.assertEqual(self.calculator.calculate(-3, -5, '*', self.calculator.settings.get_decimal_precision()), 15)
        self.assertEqual(self.calculator.calculate(3, 0, '*', self.calculator.settings.get_decimal_precision()), 0)

    def test_division(self):
        self.assertEqual(self.calculator.calculate(10, 2, '/', self.calculator.settings.get_decimal_precision()), 5.00)
        self.assertEqual(self.calculator.calculate(10, 3, '/', self.calculator.settings.get_decimal_precision()), 3.33)
        with self.assertRaises(ZeroDivisionError):
            self.calculator.calculate(10, 0, '/', self.calculator.settings.get_decimal_precision())

    def test_square_root(self):
        self.assertEqual(self.calculator.calculate(16, None, '√', self.calculator.settings.get_decimal_precision()), 4)
        self.assertEqual(self.calculator.calculate(2.25, None, '√', self.calculator.settings.get_decimal_precision()), 1.5)
        with self.assertRaises(ValueError):
            self.calculator.calculate(-16, None, '√', self.calculator.settings.get_decimal_precision())

    def test_modulus(self):
        self.assertEqual(self.calculator.calculate(10, 3, '%', self.calculator.settings.get_decimal_precision()), 1)
        self.assertEqual(self.calculator.calculate(10, 2, '%', self.calculator.settings.get_decimal_precision()), 0)
        with self.assertRaises(ZeroDivisionError):
            self.calculator.calculate(10, 0, '%', self.calculator.settings.get_decimal_precision())

    def test_exponentiation(self):
        self.assertEqual(self.calculator.calculate(2, 3, '^', self.calculator.settings.get_decimal_precision()), 8)
        self.assertEqual(self.calculator.calculate(5, 0, '^', self.calculator.settings.get_decimal_precision()), 1)
        self.assertEqual(self.calculator.calculate(-2, 3, '^', self.calculator.settings.get_decimal_precision()), -8)

    def test_decimal_precision_setting(self):
        self.calculator.settings.set_decimal_precision(4)
        self.assertEqual(self.calculator.settings.get_decimal_precision(), 4)
        self.calculator.settings.set_decimal_precision(1)
        self.assertEqual(self.calculator.settings.get_decimal_precision(), 1)

    def test_set_decimal_precision_with_invalid_input(self):
        with self.assertRaises(TypeError):
            self.calculator.settings.set_decimal_precision("two")
        with self.assertRaises(ValueError):
            self.calculator.settings.set_decimal_precision("-2")

    def test_memory_storage_and_retrieval(self):
        self.calculator.memory.set_memory_value(42)
        self.assertEqual(self.calculator.memory.get_memory_value(), 42)

    def test_memory_clear(self):
        self.calculator.memory.set_memory_value(42)
        self.calculator.memory.clear_memory()
        self.assertIsNone(self.calculator.memory.get_memory_value())

    def test_memory_operations(self):
        self.calculator.memory.set_memory_value(10)
        self.assertEqual(self.calculator.memory.get_memory_value(), 10)
        self.calculator.memory.show_memory()
        self.calculator.memory.clear_memory()
        self.assertIsNone(self.calculator.memory.get_memory_value())

    def test_history_addition(self):
        self.calculator.history.clear_history()
        self.calculator.history.add_to_history("1 + 1", 2)
        self.calculator.history.add_to_history("2 + 3", 5)
        self.assertEqual(len(self.calculator.history._History__history), 2)

    def test_history_display_when_empty(self):
        self.calculator.history.clear_history()
        self.assertEqual(len(self.calculator.history._History__history), 0)

    def test_invalid_operator(self):
        with self.assertRaises(ValueError):
            self.calculator.calculate(10, 5, 'invalid_operator', self.calculator.settings.get_decimal_precision())

    def test_set_decimal_precision_valid(self):
        self.calculator.settings.set_decimal_precision(2)
        self.assertEqual(self.calculator.settings.get_decimal_precision(), 2)

    def test_validate_operator_with_valid_operators(self):
        valid_operators = ['+', '-', '*', '/', '^', '%', '√']
        for operator in valid_operators:
            self.assertTrue(validate_operator(operator), f"Operator {operator} should be valid.")

    def test_validate_operator_with_invalid_operators(self):
        invalid_operators = ['&', '!', '@', 'a', '1', '', None]
        for operator in invalid_operators:
            self.assertFalse(validate_operator(operator), f"Operator {operator} should be invalid.")


    def test_ask_for_another_calculation(self):
        with unittest.mock.patch('builtins.input', side_effect=['y', 'n']):
            self.assertTrue(self.calculator.ask_for_another_calculation())
            self.assertFalse(self.calculator.ask_for_another_calculation())

    def test_get_number_input_invalid(self):
        with unittest.mock.patch('builtins.input', side_effect=['invalid', '5']):
            result = self.calculator._get_number_input("Введіть число: ")
            self.assertEqual(result, 5)

    def test_get_number_input_valid_memory(self):
        self.calculator.memory.set_memory_value(10)
        with unittest.mock.patch('builtins.input', side_effect=['m']):
            result = self.calculator._get_number_input("Введіть число: ")
            self.assertEqual(result, 10)

    def test_get_input(self):
        with unittest.mock.patch('builtins.input', side_effect=['5', '+', '3']):
            num1, num2, operator = self.calculator.get_input()
            self.assertEqual(num1, 5)
            self.assertEqual(num2, 3)
            self.assertEqual(operator, '+')

    def test_get_operator_input(self):
        with unittest.mock.patch('builtins.input', side_effect=['+', '*']):
            operator = self.calculator._get_operator_input("Введіть оператор: ")
            self.assertEqual(operator, '+')
            operator = self.calculator._get_operator_input("Введіть оператор: ")
            self.assertEqual(operator, '*')

    def test_show_memory(self):
        self.calculator.memory.set_memory_value(42)
        with unittest.mock.patch('builtins.print') as mocked_print:
            self.calculator.memory.show_memory()
            mocked_print.assert_called_with("Збережене в пам'яті число: 42")

    def test_show_history_empty(self):
        self.calculator.history.clear_history()
        with unittest.mock.patch('builtins.print') as mocked_print:
            self.calculator.history.show_history()
            mocked_print.assert_called_with("Історія порожня.")

    def test_add_to_history(self):
        self.calculator.history.clear_history()
        self.calculator.history.add_to_history("1 + 1", 2)
        self.assertIn("1 + 1 = 2", self.calculator.history._History__history)

    def test_clear_history(self):
        self.calculator.history.add_to_history("1 + 1", 2)
        self.calculator.history.add_to_history("2 * 2", 4)
        self.calculator.history.clear_history()
        self.assertEqual(len(self.calculator.history._History__history), 0)

    def test_invalid_number_input(self):
        with unittest.mock.patch('builtins.input', side_effect=['text', '12.5']):
            result = self.calculator._get_number_input("Введіть число: ")
            self.assertEqual(result, 12.5)

    def test_calculator_invalid_calculation(self):
        with self.assertRaises(ValueError):
            self.calculator.calculate(10, 5, '?', self.calculator.settings.get_decimal_precision())

    def test_add_negative_to_memory(self):
        self.calculator.memory.set_memory_value(-10)
        self.assertEqual(self.calculator.memory.get_memory_value(), -10)

    def test_memory_retrieval_when_empty(self):
        self.calculator.memory.clear_memory()
        self.assertIsNone(self.calculator.memory.get_memory_value())

    def test_calculator_history_size_limit(self):
        self.calculator.history.clear_history()
        for i in range(100):
            self.calculator.history.add_to_history(f"{i} + {i}", i + i)
        self.assertEqual(len(self.calculator.history._History__history), 100)  # Assuming no size limit

    def test_change_memory_value(self):
        self.calculator.memory.set_memory_value(5)
        self.calculator.memory.set_memory_value(10)
        self.assertEqual(self.calculator.memory.get_memory_value(), 10)

    def test_square_root_with_zero(self):
        self.assertEqual(self.calculator.calculate(0, None, '√', self.calculator.settings.get_decimal_precision()), 0)

    def test_square_root_with_precision(self):
        self.calculator.settings.set_decimal_precision(3)
        result = self.calculator.calculate(2, None, '√', self.calculator.settings.get_decimal_precision())
        self.assertEqual(result, 1.414)
