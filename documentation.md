# Testing Standards Guide

## Required Tests

### Unit Tests
Unit tests are essential for verifying the functionality of individual components or functions in isolation, ensuring that each unit performs as expected. 

Characteristics:
- Focus on testing small, isolated pieces of functionality (functions, methods, or classes).
- Independent of external systems such as databases, APIs, or file systems.
- Fast and lightweight, facilitating quick feedback during development.

### Integration Tests
Integration tests ensure that different modules or components of a system interact correctly, verifying the data flow and communication between them.

Characteristics:
- Validate interactions between components, such as services, databases, APIs, and external systems.
- Test end-to-end scenarios involving multiple components.
- May use real or mocked dependencies to simulate component interactions.

## Required Test Coverage
- **Minimum coverage**: 80% of the codebase.
- **Why**: We apply the Pareto Principle, which states that 80% of all bugs can be found in 20% of program modules.

## Mocking
- Use a shared directory containing a `BaseMock` abstract class, implemented for each specific mock needed during testing.
- Avoid defining mocks directly in test files; use a dedicated file for mock definitions.
- Use `unittest.mock` to mock method behaviors or responses.
- Centralize all mocked data in a `Mocks` data file.

## Test Dependencies

### Testing Dependency
- **pytest**

### Mocks
- **pytest-mock**

### Coverage
- **pytest-coverage**

## Test Configuration

### Test Configurations
- Defined and read from a `config.json` file located in the project root directory.

### Pytest Configuration
- Configurations defined in `pytest.ini` located in the project root directory.

#### Base `pytest.ini` Configuration:
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

## Test Naming Patterns

### Test Files
- Naming pattern: `<module_or_feature>_test.py`
- **Example**: Testing `user_auth.py` -> `user_auth_test.py`

### Test Methods
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

### Edge Cases
- Include specific edge cases in the test name using `edge_case_<describe_edge_case>`.
- Use keywords like `with_valid_params` for different parameter types.

### Test Fixtures

#### Mock Fixtures
- Naming pattern: `mock_<subject>`.
  - **Example**: `mock_get_users_with_valid_data`
- Import pre-defined data samples from `data_mocks.py`.

#### Tools Fixtures
- Naming pattern: `<ToolName>`.
  - **Example**: `Client`, `Mocker`, `Logger`, `Db_connection`.

## Test Directory Layout
```
Test/
├── conftest.py             # Shared mocks and data fixtures
├── mocks/
│   └── base_mock.py        # Abstract BaseMock class
├── unit_test/
│   ├── components_dir_1/
│   │   ├── component_1/
│   │   │   ├── conftest.py
│   │   │   ├── mock_data.py
│   │   │   └── test_component1.py
│   │   └── component_2/
│   │       ├── conftest.py
│   │       ├── mock_data.py
│   │       └── test_component2.py
├── integration_test/
│   ├── integration1/
│   │   ├── conftest.py
│   │   ├── mock_data.py
│   │   └── test_integration1.py
│   └── integration2/
│       ├── conftest.py
│       ├── mock_data.py
│       └── test_integration2.py
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
- **Third-Party Systems**: Mock API responses using `request_mock` fixtures.
- **Database Mocking**: [Options to be studied]
  - In-memory database.
  - Throwable Docker containers with database images.
  - Real database for testing purposes.

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
