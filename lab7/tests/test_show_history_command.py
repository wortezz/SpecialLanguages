from unittest import TestCase
from unittest.mock import MagicMock
from Commands.show_history_command import ShowHistoryCommand
from Core.user_interface import UserInterface

class TestShowHistoryCommand(TestCase):
    def test_execute(self):
        mock_ui = MagicMock(UserInterface)
        mock_history = MagicMock()
        mock_history.history = [{'request': 'GET /posts', 'response': [{'id': 1, 'title': 'Test'}]}]

        command = ShowHistoryCommand(mock_ui, mock_history)

        command.execute()

        mock_ui.display_message.assert_called_with("=== Історія запитів ===")
        mock_history.show_history.assert_called_once()
