from unittest import TestCase
from unittest.mock import patch
from Core.user_interface import UserInterface
from colorama import Fore

class TestUserInterface(TestCase):
    @patch("builtins.print")
    def test_display_message(self, mock_print):
        message = "Test Message"
        UserInterface.display_message(message, color=Fore.RED)
        mock_print.assert_called_with(Fore.RED + message + "\033[0m")
