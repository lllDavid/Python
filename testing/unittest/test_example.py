import unittest
from unittest.mock import patch, Mock
from example import get_user_profile

class TestService(unittest.TestCase):

    @patch("example.requests.get")
    def test_get_user_profile_success(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"id": 1, "name": "Alice"}
        mock_get.return_value = mock_response

        result = get_user_profile(1)
        self.assertEqual(result, {"id": 1, "name": "Alice"})
        mock_get.assert_called_once_with("https://api.example.com/users/1")

    @patch("example.requests.get")
    def test_get_user_profile_failure(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        result = get_user_profile(2)
        self.assertIsNone(result)
        mock_get.assert_called_once_with("https://api.example.com/users/2")

if __name__ == "__main__":
    unittest.main()