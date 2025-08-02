# Contributing

Thank you for your interest in contributing to User Age Analyzer! This document provides guidelines and instructions for contributing to the project.

## Getting Started

1. Fork the repository
2. Clone your fork:
   ```bash
   git clone https://github.com/yourusername/user-age-analyzer.git
   cd user-age-analyzer
   ```
3. Create a virtual environment and install development dependencies:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # or `.venv\Scripts\activate` on Windows
   pip install -e ".[dev]"
   ```

## Development Process

1. Create a branch for your feature/fix:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. Make your changes

3. Run tests:
   ```bash
   pytest tests/
   ```

4. Format your code:
   ```bash
   black .
   isort .
   ```

5. Commit your changes:
   ```bash
   git add .
   git commit -m "Description of your changes"
   ```

6. Push to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```

7. Create a Pull Request

## Code Style

- Follow PEP 8 guidelines
- Use type hints
- Write docstrings for functions and classes
- Keep functions focused and single-purpose
- Add comments for complex logic

## Testing

- Write tests for new features
- Ensure all tests pass before submitting PR
- Include both positive and negative test cases
- Mock external API calls in tests

## Documentation

When adding or modifying features:
1. Update docstrings
2. Update API documentation
3. Add examples if relevant
4. Update README if necessary

## Pull Request Guidelines

1. Reference any related issues
2. Provide clear description of changes
3. Include any necessary documentation updates
4. Ensure all tests pass
5. Keep changes focused and atomic

## Questions

If you have questions about contributing:
1. Check existing issues
2. Create a new issue with the question
3. Ask in the pull request

Thank you for contributing!
