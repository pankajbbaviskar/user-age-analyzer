# Examples

This document provides various examples of using the User Age Analyzer package.

## Basic Examples

### Simple Age Analysis

```python
from user_age_analyzer.api import UserAgeAnalyzer

# Create an analyzer instance
analyzer = UserAgeAnalyzer()

# Fetch 10 random users
analyzer.fetch_users(10)

# Analyze ages
analysis = analyzer.analyze_ages()

# Print results
print(f"Total users analyzed: {analysis['total_users']}")
print(f"Average age: {analysis['average_age']:.1f}")
print(f"\nYoungest person:")
print(f"Name: {analysis['youngest_person']['name']}")
print(f"Age: {analysis['youngest_person']['age']}")
print(f"\nOldest person:")
print(f"Name: {analysis['oldest_person']['name']}")
print(f"Age: {analysis['oldest_person']['age']}")
```

### Saving and Loading Data

```python
from user_age_analyzer.api import UserAgeAnalyzer
import json

# Fetch and save data
analyzer = UserAgeAnalyzer()
analyzer.fetch_users(5)
analyzer.save_to_file()  # Creates timestamped JSON file

# Load saved data (example)
with open('data/users_data_2025-07-27-17-31-28.json', 'r') as f:
    saved_data = json.load(f)
```

### Error Handling Example

```python
from user_age_analyzer.api import UserAgeAnalyzer

analyzer = UserAgeAnalyzer()

try:
    analyzer.fetch_users(5)
    if not analyzer.users_data:
        print("No data was fetched")
    else:
        analysis = analyzer.analyze_ages()
        print(f"Successfully analyzed {analysis['total_users']} users")
except Exception as e:
    print(f"An error occurred: {str(e)}")
```

## Working with Results

### Filtering Users by Age

```python
from user_age_analyzer.api import UserAgeAnalyzer

analyzer = UserAgeAnalyzer()
analyzer.fetch_users(20)

analysis = analyzer.analyze_ages()
all_users = analysis['all_users']

# Filter users under 30
young_users = [user for user in all_users if user['age'] < 30]

print("\nUsers under 30:")
for user in young_users:
    print(f"{user['name']}: {user['age']} years")
```

### Statistical Analysis

```python
from user_age_analyzer.api import UserAgeAnalyzer
import statistics

analyzer = UserAgeAnalyzer()
analyzer.fetch_users(50)

analysis = analyzer.analyze_ages()
ages = [user['age'] for user in analysis['all_users']]

# Calculate additional statistics
median_age = statistics.median(ages)
age_variance = statistics.variance(ages)
age_stdev = statistics.stdev(ages)

print(f"Median age: {median_age}")
print(f"Age variance: {age_variance:.2f}")
print(f"Age standard deviation: {age_stdev:.2f}")
```

These examples demonstrate common use cases and patterns for the User Age Analyzer package. For more detailed information about the API, please refer to the [API Reference](./api_reference.md).
