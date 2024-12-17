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
- Validate interactions between components, such as services, databases, APIs, and external systems.
- Test end-to-end scenarios involving multiple components.
- May use real or mocked dependencies to simulate component interactions.

## Required test coverage

### Test Coverage Requirements
- **Minimum Coverage**: 80% of the codebase.
- **Reason**: 
  - This threshold applies the **Pareto Principle**, which suggests that 80% of bugs are typically found in 20% of the modules.
  - Ensuring this level of coverage helps identify and address potential issues early in development.

### Checking Test Coverage
Test coverage must be verified before pushing changes to the remote branch. Use the following `pytest` command to generate an HTML coverage report:

```bash
pytest --cov=<your_package_name> --cov-report=html
```

- Replace `<your_package_name>` with the name of the package or directory you want to measure coverage for.
- This command creates a detailed HTML report in a `htmlcov` directory, which can be opened in a browser for review.

## Mocking

### General guidelines
- Use a shared directory containing a `BaseMock` abstract class, implemented for each specific mock needed during testing.
- Avoid defining mocks directly in test files; use a dedicated file for mock definitions.
- Use `unittest.mock` to mock method behaviors or responses.
- Centralize all mocked data in a `Mocks` data file.

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
minversion = 8.0
addopts = --strict-markers --disable-warnings -v
testpaths = tests
python_files = *_test.py
python_classes = Tests*
python_functions = test_*
markers =
    Slow: marks tests as slow (deselect with '-m "not slow"')
    Integration: marks integration tests
log_cli = true
log_cli_level = INFO
log_cli_format = %(asctime)s [%(levelname)s]
log_cli_data_format = %Y-%m-%d %H:%M:%S
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
