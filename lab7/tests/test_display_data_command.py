import unittest
from Commands.display_data_command import DisplayDataCommand
from Core.user_interface import UserInterface

class TestDisplayDataCommand(unittest.TestCase):
    def setUp(self):
        self.user_interface = UserInterface()
        self.data = [{"id": 1, "title": "Test Post"}]
        self.command = DisplayDataCommand(self.user_interface, self.data, "posts")

    def test_execute_display_data(self):
        self.user_interface.display_data = unittest.mock.MagicMock()
        self.command.execute()
        self.user_interface.display_data.assert_called_once()

if __name__ == "__main__":
    unittest.main()
