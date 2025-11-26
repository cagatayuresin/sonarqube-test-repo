# sonarqube-test-repo

A test repository for SonarQube and GitHub Actions integration.

## Overview

This repository demonstrates how to integrate SonarQube code analysis with GitHub Actions. It includes:

- A simple Python calculator module
- Unit tests with pytest
- GitHub Actions workflow for automated SonarQube analysis
- SonarQube project configuration

## Project Structure

```
.
├── .github/
│   └── workflows/
│       └── sonarqube.yml    # GitHub Actions workflow
├── src/
│   ├── __init__.py
│   └── calculator.py        # Sample Python module
├── tests/
│   ├── __init__.py
│   └── test_calculator.py   # Unit tests
├── sonar-project.properties # SonarQube configuration
├── pyproject.toml           # Python project configuration
└── README.md
```

## Setup

### Prerequisites

- Python 3.9+
- SonarQube server or SonarCloud account

### Running Tests Locally

```bash
# Install dependencies
pip install pytest pytest-cov

# Run tests with coverage
pytest tests/ --cov=src --cov-report=xml --cov-report=term-missing
```

### GitHub Actions Integration

The workflow in `.github/workflows/sonarqube.yml` automatically:
1. Runs on push to `main` branch and on pull requests
2. Sets up Python environment
3. Runs tests with coverage
4. Performs SonarQube analysis

### Required Secrets

Configure the following secrets in your GitHub repository:
- `SONAR_TOKEN`: Your SonarQube authentication token
- `SONAR_HOST_URL`: Your SonarQube server URL (e.g., `https://sonarcloud.io`)

## License

MIT License - see [LICENSE](LICENSE) for details