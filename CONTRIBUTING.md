# Contributing to 3D Universe

Thank you for considering contributing to 3D Universe! This document provides guidelines and instructions for contributing to this project.

## Code of Conduct

Please be respectful and considerate of others when contributing to this project.

## How to Contribute

### Reporting Issues

If you find a bug or have a suggestion for improvement:

1. Check if the issue already exists in the [GitHub Issues](https://github.com/govindrnaik/3d-universe/issues)
2. If not, create a new issue with a descriptive title and detailed information about the issue

### Making Changes

1. Fork the repository
2. Create a new branch for your changes: `git checkout -b feature/your-feature-name`
3. Make your changes, following the code style guidelines
4. Write tests for your changes if applicable
5. Update documentation as needed
6. Commit your changes with a descriptive message

### Submitting a Pull Request

1. Push your changes to your fork: `git push origin feature/your-feature-name`
2. Create a Pull Request against the main repository
3. Describe your changes in detail in the PR description
4. Reference any related issues

## Development Setup

1. Clone the repository
2. Set up a virtual environment: `python -m venv .venv`
3. Activate the virtual environment:
   - Windows: `.venv\Scripts\activate`
   - Unix/MacOS: `source .venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Run the application: `python app.py`

## Code Style Guidelines

- Follow [PEP 8](https://pep8.org/) for Python code
- Use meaningful variable and function names
- Write comments for complex logic
- Format code with Black: `black .`
- Sort imports with isort: `isort .`

## Testing

- Write tests for new features using pytest
- Run the test suite before submitting a PR: `pytest`

## Documentation

- Update documentation when adding or changing features
- Ensure docstrings are up to date and follow the Google style guide

Thank you for contributing!