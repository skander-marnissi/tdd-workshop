# Testing standards guide

## Required tests

### Unit tests
Unit tests are essential for verifying the functionality of individual components or functions in isolation, ensuring that each unit performs as expected. 

Characteristics:
- Focus on testing small, isolated pieces of functionality (functions, methods, or classes).
- Independent of external systems such as databases, APIs, or file systems.
- Fast and lightweight, facilitating quick feedback during development.

### Integration tests
Integration tests ensure that different modules or components of a system interact correctly, verifying the data flow and communication between them.

Characteristics:
- Validate interactions between components, such as services, APIs, and internal modules.
- Test end-to-end scenarios involving multiple components within the project.
- Use mocked dependencies to simulate interactions with external systems, avoiding real system dependencies.

## Test coverage

### Coverage requirements
- **Minimum coverage**: 80% of the codebase.
- **Reason**: 
  - This threshold applies the **Pareto Principle**, which suggests that 80% of bugs are typically found in 20% of the modules.
  - Ensuring this level of coverage helps identify and address potential issues early in development.

### Coverage configuration
To ensure that your codebase is properly covered by tests, we use **pytest-cov** for measuring test coverage. The following configuration is provided as an example template for your project.

#### Base `.coveragerc` configuration:
The `.coveragerc` file contains the configuration for **coverage** and is used by pytest-cov during test runs to track test coverage.

```ini
[coverage:run]
branch = True      # Enables branch coverage, which ensures coverage reports consider code branches.
source =           # Specifies which directories or packages to include in the coverage analysis, you can list multiple items here.
    your_package_name
omit =             # Exclude specific files or directories from being included in the coverage report,  you can list multiple items here.
    */directory_name/*
    */file_name.py

[coverage:report]
show_missing = True     # Shows lines that are not covered in the report.
skip_covered = True     # Skips displaying files that have full coverage.
focus = True            # Focuses on files that have the most important code (useful for large projects).
include =               # Specifies the files or directories to include in the report.
    app/*
fail_under = 80         # Fails the test if the coverage percentage is below a certain threshold.

[coverage:html]
directory = htmlcov         # Defines the output directory for the HTML report.
title = Coverage Report     # The title of the HTML coverage report page

[coverage:xml]
output = coverage.xml      # Specifies the output file for the XML report.

[coverage:json]      
output = coverage.json     # Specifies the output file for the JSON report.

[coverage:debug]
trace = True       # Traces code execution during coverage collection
config = True      # Displays the configuration being used
data = True        # Shows coverage data in detail
```
### Checking coverage
Test coverage must be verified before pushing changes to the remote branch. Use the following `pytest` command to generate an HTML coverage report:

```bash
pytest --cov=<your_package_name> --cov-report=html
```

- Replace `<your_package_name>` with the name of the package or directory you want to measure coverage for.
- This command creates a detailed HTML report in a `htmlcov` directory, which can be opened in a browser for review.

## Mocking

### General guidelines
- Use `pytest-mock` to mock method behaviors or responses.
- Use a `BaseMock` abstract class, implemented for each specific mock needed during testing.
- Centralize all mocked data samples in a `mock_data.py` data file.
- Centralize all mock fixtures in `conftest.py` data file.

### Mocking third-party systems
- Mock API responses using `request_mock` fixtures to simulate external system behavior.
- Avoid directly patching functions that can be naturally invoked during integration tests to ensure realistic simulations.

### Database mocking options (To be studied):
- **In-Memory Database**: Lightweight but may lack real-world simulation capabilities.
- **Throwable Docker Containers**: Use database images to create isolated environments during testing.
- **Dedicated Testing Database**: Set up a real database instance exclusively for test purposes to ensure high-fidelity simulations.

## Test dependencies

### Testing dependency
- **pytest**: The core framework for running Python tests.

### Coverage
- **pytest-cov**: : Measures test coverage and integrates it with **pytest**

### Mocks and stubbing
- **pytest-mock**: Integrates **unittest.mock** with pytest for mocking functionality.
- **pytest-faker**: : Provides fake data generation via **faker**.

### Performance and stress testing
- **pytest-benchmark**: Measures code performance during tests.

### Specialized testing
- **pytest-flask**: Adds support for Flask applications.

## Test configuration

### Test configurations
- Defined and read from a `config.json` file located in the project root directory.

### Pytest configuration
- Configurations defined in `pytest.ini` located in the project root directory.

#### Base `pytest.ini` configuration:
```ini
[pytest]
minversion = 8.0                                    # Specifies the minimum version of pytest required for the test suite.                                  
addopts = --strict-markers --disable-warnings -v    # Allows you to specify additional command-line options that should be passed to pytest every time it is run.
testpaths = tests                                   # Specifies the directories where pytest will search for test files.
python_files = **/*_test.py                         # Specifies the file pattern pytest uses to identify test files.
python_classes = Test*                              # Specifies the pattern that test class names should follow.
python_functions = test_*                           # Specifies the pattern for test function names.
markers =                                           # This section defines custom markers that can be used to categorize or tag tests.
    Slow: marks tests as slow (deselect with '-m "not slow"') # Marks a test as "slow", so you can selectively run tests using -m "not slow" to exclude them or -m "slow" to run them.
    Integration: marks integration tests                      # Marks a test as an integration test. You can run only integration tests by using -m "Integration"
log_cli = true                                      # Enables or disables logging to the command-line interface (CLI)
log_cli_level = INFO                                # Specifies the logging level for the CLI output.
log_cli_format = %(asctime)s [%(levelname)s]        # Specifies the format for the log output in the CLI.
log_cli_data_format = %Y-%m-%d %H:%M:%S             # Defines the date format for the timestamp in log messages.
```

## Test naming patterns

### Test files
- Naming pattern: `<module_or_feature>_test.py`
- **Example**: Testing `user_auth.py` -> `user_auth_test.py`

### Test methods
- Naming pattern: `test_<UnitOfWork>_<Scenario>_<ExpectedOutcome>`

#### Example:
```python
def test_add_item_to_cart_with_valid_data_returns_updated_cart():
    pass

def test_remove_item_from_cart_when_item_exists_returns_success():
    pass

def test_checkout_with_empty_cart_raises_error():
    pass
```

### Edge cases
- Include specific edge cases in the test name using `edge_case_<describe_edge_case>`.
- Use keywords like `with_valid_params` for different parameter types.

### Test fixtures

#### Mock fixtures
- Naming pattern: `mock_<subject>`.
  - **Example**: `mock_get_users_with_valid_data`
- Import pre-defined data samples from `data_mocks.py`.

#### Tools fixtures
- Naming pattern: `<ToolName>`.
  - **Example**: `Client`, `Mocker`, `Logger`, `Db_connection`.

## Test directory layout
```
Test/
├── conftest.py             # Shared mocks and tool fixtures
├── mocks/
│   └── base_mock.py        # Abstract BaseMock class
├── unit_tests/             # Unit tests directory
│   ├── components_dir_1/   # Component directory (e.g., /services)
│   │   ├── conftest.py
│   │   ├── mock_data.py
│   │   ├── test_component_dir_1_1.py
│   │   └── test_component_dir_1_2.py
│   │   ...
│   ├── component_dir_2/
│   │   ├── conftest.py
│   │   ├── mock_data.py
│   │   ├── test_component_dir_2_1.py
│   │   └── test_component_dir_2_2.py
│   │   ...
│   └── ...                 # Additional component directories
├── integration_tests/      # Integration tests directory
│   ├── integration_dir_1/
│   │   ├── conftest.py
│   │   ├── mock_data.py
│   │   ├── test_integration_dir_1_1.py
│   │   └── test_integration_dir_1_2.py
│   │   ...
│   ├── integration_dir_2/
│   │   ├── conftest.py
│   │   ├── mock_data.py
│   │   ├── test_integration_dir_2_1.py
│   │   └── test_integration_dir_2_2.py
│   │   ...
│   └── ...                 # Additional integration directories

```

## Unit Tests

### Characteristics
[To be completed]

### Mocking
[To be completed]

## Integration Tests

### Characteristics
- **Focus on Component Interactions**: Validates communication and data flow between components.
- **End-to-End Scenarios**: Tests functionality involving multiple components, APIs, or external services.
- **Real or Mocked Dependencies**: Simulate dependencies like databases or APIs.

### Mocking
- **Third-Party Systems**: Mock API responses using `request_mock` fixtures to simulate interactions.
- **Database Mocking**: Ensure isolated and realistic test environments with options such as Docker containers or dedicated testing databases.

## Test-Driven Development (TDD)

### Red-Green-Refactor Methodology
- **Red**: [To be completed]
- **Green**: [To be completed]
- **Refactor**: [To be completed]

## Test Debugger Configuration

### VS Code
[To be completed]

### PyCharm
[To be completed]
