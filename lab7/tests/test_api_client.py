from unittest import TestCase
from unittest.mock import patch, MagicMock
from Core.api_client import APIClient

class TestAPIClient(TestCase):
    @patch('Core.api_client.requests.get')
    def test_get_data_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = [{'id': 1, 'title': 'Test Post'}]

        mock_get.return_value = mock_response

        data = APIClient.get_data("posts")
        self.assertIsNotNone(data)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['title'], 'Test Post')

    @patch('Core.api_client.requests.get')
    def test_get_data_failure(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_response.json.return_value = None  

        mock_get.return_value = mock_response

        data = APIClient.get_data("posts")
        self.assertIsNone(data)
