# Getting Started

This guide will help you get started with the User Age Analyzer package.

## Installation

### Prerequisites

- Python 3.13 or higher
- pip package manager

### Standard Installation

```bash
pip install user-age-analyzer
```

### Development Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd user-age-analyzer
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   # On Windows:
   .venv\Scripts\activate
   # On Unix or MacOS:
   source .venv/bin/activate
   ```

3. Install development dependencies:
   ```bash
   pip install -e ".[dev]"
   ```

## Basic Usage

### Fetching and Analyzing User Data

```python
from user_age_analyzer.api import UserAgeAnalyzer

# Create analyzer instance
analyzer = UserAgeAnalyzer()

# Fetch 5 random users
analyzer.fetch_users(5)

# Analyze the ages
analysis = analyzer.analyze_ages()

print(f"Total Users: {analysis['total_users']}")
print(f"Average Age: {analysis['average_age']}")
print(f"Youngest: {analysis['youngest_person']['name']} ({analysis['youngest_person']['age']})")
print(f"Oldest: {analysis['oldest_person']['name']} ({analysis['oldest_person']['age']})")
```

### Saving Data to File

```python
# Save the fetched data to a JSON file
analyzer.save_to_file()
```

## FAQ

### Q: Where are the JSON files saved?
A: JSON files are saved in the `data` directory with timestamps in the format: `users_data_YYYY-MM-DD-HH-MM-SS.json`

### Q: How can I handle API errors?
A: The package automatically handles API errors. If an error occurs, the `users_data` will be empty and can be checked:
```python
analyzer.fetch_users(5)
if not analyzer.users_data:
    print("Error fetching data")
```

### Q: What Python versions are supported?
A: The package requires Python 3.13 or higher due to use of modern features and type hints.
