import unittest
from unittest.mock import patch, MagicMock
from Commands.load_data_command import LoadDataCommand
from Core.user_interface import UserInterface

class TestLoadDataCommand(unittest.TestCase):
    @patch("Core.api_client.APIClient.get_data")
    def test_execute_load_data(self, mock_get_data):
        mock_get_data.return_value = [{"id": 1, "title": "Test Post"}]
        user_interface = UserInterface()
        history = MagicMock()
        posts = []
        albums = []
        command = LoadDataCommand(user_interface, history, posts, albums)

        command.execute()
        self.assertEqual(len(posts), 1)
        history.log_request.assert_called()

if __name__ == "__main__":
    unittest.main()
