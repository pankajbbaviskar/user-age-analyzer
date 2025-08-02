# API Reference

This document provides detailed information about the User Age Analyzer API.

## UserAgeAnalyzer Class

The main class that provides all functionality for fetching and analyzing user data.

### Methods

#### `__init__(self)`

Initializes a new UserAgeAnalyzer instance.

**Parameters**: None

**Returns**: None

---

#### `fetch_users(self, count: int) -> None`

Fetches random user data from the RandomUser API.

**Parameters**:
- `count` (int): Number of users to fetch

**Returns**: None

**Side Effects**:
- Updates `self.users_data` with fetched user information
- Prints status messages to console
- May create a JSON file with timestamp if successful

**Example**:
```python
analyzer = UserAgeAnalyzer()
analyzer.fetch_users(5)  # Fetches 5 random users
```

---

#### `analyze_ages(self) -> dict`

Analyzes the age data of fetched users.

**Parameters**: None

**Returns**: 
Dictionary containing:
- `total_users`: Total number of users
- `youngest_person`: Dict with name and age of youngest person
- `oldest_person`: Dict with name and age of oldest person
- `average_age`: Average age of all users
- `sum_of_age`: Sum of all users' ages
- `all_users`: List of all users with their ages

**Example**:
```python
analysis = analyzer.analyze_ages()
print(f"Average age: {analysis['average_age']}")
```

---

#### `save_to_file(self) -> None`

Saves the current user data to a JSON file.

**Parameters**: None

**Returns**: None

**Side Effects**:
- Creates a JSON file in the `data` directory with timestamp in filename

**Example**:
```python
analyzer.save_to_file()  # Creates file like 'users_data_2025-07-27-17-31-28.json'
```

## Error Handling

The API includes built-in error handling for:
- Network connectivity issues
- API response errors
- Invalid data formats
- File system operations

Errors are handled gracefully with appropriate console messages and empty data structures to prevent crashes.
