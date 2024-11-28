import unittest
from unittest.mock import patch, MagicMock
from Commands.save_data_command import SaveDataCommand
from Core.user_interface import UserInterface
from Core.data_saver import DataSaver

class TestSaveDataCommand(unittest.TestCase):
    @patch("builtins.input", return_value="json")
    def test_execute_save_data_json(self, mock_input):
        user_interface = UserInterface()
        data_saver = DataSaver()
        data = [{"id": 1, "title": "Test Post"}]
        command = SaveDataCommand(user_interface, data_saver, data, "posts")

        data_saver.save_data = MagicMock()
        command.execute()

        data_saver.save_data.assert_called_once()

if __name__ == "__main__":
    unittest.main()
