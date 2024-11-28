import os
from unittest import TestCase
from unittest.mock import patch, MagicMock
from Core.data_saver import DataSaver


class TestDataSaver(TestCase):

    @patch("builtins.open", new_callable=MagicMock)  # Мокаємо відкриття файлів
    def test_save_as_json(self, mock_open):
        mock_open.return_value.__enter__.return_value = MagicMock()
        data = [{'id': 1, 'title': 'Test Post'}]

        # Тестуємо метод save_as_json
        test_file = "Data/test.json"  # Вказуємо шлях до файлу
        DataSaver.save_as_json(data, test_file)

        # Перевіряємо, що файл відкрито для запису
        mock_open.assert_called_with(test_file, "w")

    @patch("builtins.open", new_callable=MagicMock)  # Мокаємо відкриття файлів
    def test_save_as_csv(self, mock_open):
        mock_open.return_value.__enter__.return_value = MagicMock()
        data = [{'id': 1, 'title': 'Test Post'}]

        # Тестуємо метод save_as_csv
        test_file = "Data/test.csv"  # Вказуємо шлях до файлу
        DataSaver.save_as_csv(data, test_file)

        # Перевіряємо, що файл відкрито для запису
        mock_open.assert_called_with(test_file, "w", newline='')

    @patch("builtins.open", new_callable=MagicMock)  # Мокаємо відкриття файлів
    def test_save_as_txt(self, mock_open):
        mock_open.return_value.__enter__.return_value = MagicMock()
        data = [{'id': 1, 'title': 'Test Post'}]

        # Тестуємо метод save_as_txt
        test_file = "Data/test.txt"  # Вказуємо шлях до файлу
        DataSaver.save_as_txt(data, test_file)

        # Перевіряємо, що файл відкрито для запису
        mock_open.assert_called_with(test_file, "w")
