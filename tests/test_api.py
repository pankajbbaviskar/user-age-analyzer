import unittest
from unittest.mock import patch, MagicMock
from datetime import datetime
import json
from user_age_analyzer.api import UserAgeAnalyzer

class TestUserAgeAnalyzer(unittest.TestCase):
    def setUp(self):
        self.analyzer = UserAgeAnalyzer()
        self.sample_data = {
            "results": [
                {
                    "name": {"first": "John", "last": "Doe"},
                    "dob": {"age": 25}
                },
                {
                    "name": {"first": "Jane", "last": "Smith"},
                    "dob": {"age": 35}
                },
                {
                    "name": {"first": "Bob", "last": "Johnson"},
                    "dob": {"age": 45}
                }
            ]
        }

    @patch('requests.get')
    def test_fetch_users_success(self, mock_get):
        # Configure the mock response
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = self.sample_data
        mock_get.return_value = mock_response

        # Test fetching users
        self.analyzer.fetch_users(3)
        
        # Verify the API was called with correct parameters
        mock_get.assert_called_once_with("https://randomuser.me/api/?results=3")
        self.assertEqual(len(self.analyzer.users_data), 3)

    @patch('requests.get')
    def test_fetch_users_api_error(self, mock_get):
        # Configure mock to simulate API error
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        # Test fetching users with error
        self.analyzer.fetch_users(3)
        self.assertEqual(len(self.analyzer.users_data), 0)

    def test_analyze_ages_empty_data(self):
        # Test analysis with no data
        result = self.analyzer.analyze_ages()
        self.assertEqual(result, {"error": "No User Data is Found to analyze"})

    def test_analyze_ages_with_data(self):
        # Set sample data directly
        self.analyzer.users_data = self.sample_data["results"]

        # Test age analysis
        result = self.analyzer.analyze_ages()

        # Verify analysis results
        self.assertEqual(result["total_users"], 3)
        self.assertEqual(result["youngest_person"]["name"], "John Doe")
        self.assertEqual(result["youngest_person"]["age"], 25)
        self.assertEqual(result["oldest_person"]["name"], "Bob Johnson")
        self.assertEqual(result["oldest_person"]["age"], 45)
        self.assertEqual(result["average_age"], 35.0)
        self.assertEqual(result["sum_of_age"], 105)
        self.assertEqual(len(result["all_users"]), 3)

    @patch('builtins.open')
    def test_save_to_file(self, mock_open):
        # Set sample data
        self.analyzer.users_data = self.sample_data["results"]
        
        # Test saving to file
        self.analyzer.save_to_file()
        
        # Verify file was opened for writing
        mock_open.assert_called_once()
        # Verify the first argument of the first call contains the correct filename pattern
        args, _ = mock_open.call_args
        self.assertTrue(args[0].startswith("users_data_"))
        self.assertTrue(args[0].endswith(".json"))

if __name__ == '__main__':
    unittest.main()
