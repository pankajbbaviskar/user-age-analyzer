# User Age Analyzer

A Python application that fetches user data from the Random User API and performs age-based analysis on the retrieved users.

## Features

- Fetches random user data from [Random User API](https://randomuser.me/)
- Analyzes user ages to find:
  - Total number of users
  - Youngest person's details
  - Oldest person's details
  - Average age
  - Sum of all ages
  - Complete list of users with their ages
- Saves fetched user data to JSON files with timestamps
- Includes comprehensive test suite

## Project Structure

```
user-age-analyzer/
│
├── user_age_analyzer/      # Main package directory
│   ├── __init__.py
│   └── api.py             # Main implementation of UserAgeAnalyzer
│
├── tests/                 # Test directory
│   ├── __init__.py
│   └── test_api.py       # Test suite for UserAgeAnalyzer
│
├── examples/             # Example code and tutorials
│   └── vars.py          # Example of Python variables and formatting
│
├── docs/                # Documentation directory
│
├── data/               # Data directory for JSON files
│   └── .gitkeep
│
├── setup.py            # Package setup file
├── requirements.txt    # Project dependencies
├── README.md          # Project documentation
├── LICENSE            # MIT License
└── .gitignore        # Git ignore file
```

## Requirements

- Python 3.13+
- Required packages (install via requirements.txt):
  - requests==2.32.4
  - pytest==8.4.1

## Installation

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd python-code
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   # On Windows:
   .venv\Scripts\activate
   # On Unix or MacOS:
   source .venv/bin/activate
   ```

3. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Basic Usage

```python
from src.call_api import UserAgeAnalyzer

# Create an instance of UserAgeAnalyzer
analyzer = UserAgeAnalyzer()

# Fetch 5 random users
analyzer.fetch_users(5)

# Analyze the ages
analysis = analyzer.analyze_ages()

# Save the data to a JSON file
analyzer.save_to_file()
```

### Analysis Output

The `analyze_ages()` method returns a dictionary containing:
- `total_users`: Total number of users analyzed
- `youngest_person`: Details of the youngest person
- `oldest_person`: Details of the oldest person
- `average_age`: Average age of all users
- `sum_of_age`: Sum of all users' ages
- `all_users`: List of all users with their ages

## Testing

The project includes a comprehensive test suite that covers:
- Successful API calls
- API error handling
- Age analysis with sample data
- Empty data handling
- File saving functionality

To run the tests:
```bash
python -m unittest -v test_call_api.py
```

## Data Storage

User data is automatically saved to JSON files with timestamps in the format:
```
users_data_YYYY-MM-DD-HH-MM-SS.json
```

## Error Handling

The application includes error handling for:
- API request failures
- Empty or invalid data
- File operations

## Documentation

Comprehensive documentation is available in the `docs` directory:

- [Getting Started](docs/getting_started.md) - Installation and basic usage instructions
- [API Reference](docs/api_reference.md) - Detailed API documentation and method descriptions
- [Examples](docs/examples.md) - Code examples and common use cases
- [Contributing](docs/contributing.md) - Guidelines for contributing to the project

The documentation covers:
- Complete API reference with method descriptions
- Step-by-step tutorials and examples
- Error handling strategies
- Best practices and usage patterns
- Development and contribution guidelines
- Frequently Asked Questions (FAQ)

For the full documentation, start with the [Documentation Index](docs/index.md).

## License

This project is provided as-is for demonstration purposes.

## Contributing

can contribute connect with me[pankaj_baviskar@hotmil.com]

## Author

Pankaj Baviskar[Pankaj_Baviskar@hotmail.com]


