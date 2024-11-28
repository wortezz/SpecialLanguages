import unittest
from unittest.mock import Mock, patch
from UI.user_interface import main
from Commands.show_history_command import History
from Core.user_interface import UserInterface
from Core.data_saver import DataSaver

class TestApp(unittest.TestCase):
    def setUp(self):
        self.user_interface = Mock(spec=UserInterface)
        self.history = Mock(spec=History)
        self.data_saver = Mock(spec=DataSaver)
        self.posts = []
        self.local_posts = []
        self.albums = []
        self.local_albums = []

    @patch('builtins.input', side_effect=["1", "0"])
    @patch('Commands.load_data_command.LoadDataCommand.execute')
    def test_load_data_command(self, mock_load_execute, mock_input):
        main()
        mock_load_execute.assert_called_once()

    @patch('builtins.input', side_effect=["2", "0"])
    @patch('Commands.display_data_command.DisplayDataCommand.execute')
    def test_display_posts_command(self, mock_display_execute, mock_input):
        main()
        mock_display_execute.assert_called_once()

    @patch('builtins.input', side_effect=["3", "1", "Test Title", "Test Body", "0"])
    @patch('Commands.add_item_command.AddItemCommand.execute')
    def test_add_post_command(self, mock_add_execute, mock_input):
        main()
        mock_add_execute.assert_called_once()

    @patch('builtins.input', side_effect=["4", "1", "0"])
    @patch('Commands.delete_item_command.DeleteItemCommand.execute')
    def test_delete_post_command(self, mock_delete_execute, mock_input):
        main()
        mock_delete_execute.assert_called_once()

    @patch('builtins.input', side_effect=["5", "0"])
    @patch('Commands.display_data_command.DisplayDataCommand.execute')
    def test_display_albums_command(self, mock_display_execute, mock_input):
        main()
        mock_display_execute.assert_called_once()

    @patch('builtins.input', side_effect=["6", "1", "Test Album Title", "0"])
    @patch('Commands.add_item_command.AddItemCommand.execute')
    def test_add_album_command(self, mock_add_execute, mock_input):
        main()
        mock_add_execute.assert_called_once()

    @patch('builtins.input', side_effect=["7", "1", "0"])
    @patch('Commands.delete_item_command.DeleteItemCommand.execute')
    def test_delete_album_command(self, mock_delete_execute, mock_input):
        main()
        mock_delete_execute.assert_called_once()

    @patch('builtins.input', side_effect=["8", "json", "0"])
    @patch('Commands.save_data_command.SaveDataCommand.execute')
    def test_save_posts_command(self, mock_save_execute, mock_input):
        main()
        mock_save_execute.assert_called_once()

    @patch('builtins.input', side_effect=["9", "json", "0"])
    @patch('Commands.save_data_command.SaveDataCommand.execute')
    def test_save_albums_command(self, mock_save_execute, mock_input):
        main()
        mock_save_execute.assert_called_once()

    @patch('builtins.input', side_effect=["10", "0"])
    @patch('Commands.show_history_command.ShowHistoryCommand.execute')
    def test_show_history_command(self, mock_history_execute, mock_input):
        main()
        mock_history_execute.assert_called_once()

    @patch('builtins.input', side_effect=["0"])
    def test_exit(self, mock_input):
        main()


