import unittest
from unittest.mock import MagicMock
from Commands.delete_item_command import DeleteItemCommand
from Core.user_interface import UserInterface

class TestDeleteItemCommand(unittest.TestCase):
    def setUp(self):
        self.user_interface = UserInterface()
        self.history = MagicMock()
        self.local_data = [{"id": 1, "title": "Test Post"}]
        self.command = DeleteItemCommand(self.user_interface, self.history, self.local_data, "posts")

    def test_execute_delete_post(self):
        with unittest.mock.patch('builtins.input', return_value="1"):
            self.command.execute()

        self.assertEqual(len(self.local_data), 0)
        self.history.log_request.assert_called_once_with("DELETE /posts", {"id": 1, "title": "Test Post"})

if __name__ == "__main__":
    unittest.main()
