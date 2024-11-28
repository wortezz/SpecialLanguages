import unittest
from unittest.mock import Mock, patch
from Commands.add_item_command import AddItemCommand
from Core.user_interface import UserInterface
from Commands.show_history_command import History

class TestAddItemCommand(unittest.TestCase):
    def setUp(self):
        self.user_interface = Mock(spec=UserInterface)
        self.history = Mock(spec=History)
        self.data = []
        self.local_data = []
        self.command = AddItemCommand(self.user_interface, self.history, self.data, self.local_data, "posts")

    @patch('builtins.input', side_effect=["1", "Test Post", "This is the body of the post"])
    def test_execute_add_post(self, mock_input):
        self.command.execute()

        self.assertEqual(len(self.local_data), 1)
        self.assertEqual(self.local_data[0]["userId"], 1)
        self.assertEqual(self.local_data[0]["title"], "Test Post")
        self.assertEqual(self.local_data[0]["body"], "This is the body of the post")

