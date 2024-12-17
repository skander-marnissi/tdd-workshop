# Testing Standards

## Summary
- [Required Tests](#required-tests)
  - [Unit Tests](#unit-tests)
  - [Integration Tests](#integration-tests)
- [Test Coverage](#test-coverage)
  - [Coverage Requirements](#coverage-requirements)
  - [Coverage Configuration](#coverage-configuration)
  - [Checking Coverage](#checking-coverage)
- [Mocking](#mocking)
  - [General Guidelines](#general-guidelines)
  - [Mocking Third-Party Systems](#mocking-third-party-systems)
  - [Database Mocking Options](#database-mocking-options-to-be-studied)
- [Test Dependencies](#test-dependencies)
  - [Testing Dependency](#testing-dependency)
  - [Coverage](#coverage)
  - [Mocks and Stubbing](#mocks-and-stubbing)
  - [Performance and Stress Testing](#performance-and-stress-testing)
  - [Specialized Testing](#specialized-testing)
- [Test Configuration](#test-configuration)
  - [Test Configurations](#test-configurations)
  - [Pytest Configuration](#pytest-configuration)
- [Tests Naming Patterns](#tests-naming-patterns)
  - [Test Files](#test-files)
  - [Test Methods](#test-methods)
  - [Edge Cases](#edge-cases)
- [Fixtures and Data Mocks Naming](#fixtures-and-data-mocks-naming)
  - [Mock Fixtures](#mock-fixtures)
  - [Tools Fixtures](#tools-fixtures)
  - [Data Mocks](#data-mocks)
- [Test Directory Layout](#test-directory-layout)
- [Test-Driven Development (TDD)](#test-driven-development-tdd)
  - [Red-Green-Refactor Methodology](#red-green-refactor-methodology)
  - [Key Principles of TDD](#key-principles-of-tdd)
- [Visual Studio Code Test Debugging Configuration](#visual-studio-code-test-debugging-configuration)
- [Special Thanks](#special-thanks)

---

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

## Tests naming patterns

### Test files

**Naming pattern**: `<module_or_feature>_test.py`

- **Description**:  
  This pattern associates each test file directly with the module or feature it tests.  
  - `<module_or_feature>` should clearly identify the functionality under test (e.g., `user_auth`, `cart`, `database`).

- **Examples**:  
  - `user_auth_test.py`: Tests related to the `user_auth` module.
  - `cart_test.py`: Tests specifically targeting cart-related functionalities.

- **Best practices**:  
  - Keep test files focused on a single module or closely related set of features.
  - Match the naming between the target code file and its corresponding test file for easy navigation.

### Test methods

**Naming pattern**: `test_<unit_of_work>_<scenario>_<expected_outcome>`

- **Description**:  
  Break down test names into three distinct parts to clearly convey intent:  
  - `<unit_of_work>`: Identifies the specific functionality, method, or class under test. (e.g., `add_item_to_cart`, `remove_item_from_cart`, `checkout`)  
  - `<scenario>`: Describes the context, condition, or inputs of the test. (e.g., `with_valid_data`, `when_item_does_not_exist`, `with_empty_cart`)  
  - `<expected_outcome>`: Defines the anticipated result or behavior. (e.g., `returns_updated_cart`, `raises_error`, `returns_success`)

- **Examples**:  
  ```python
  def test_add_item_to_cart_with_valid_data_returns_updated_cart():
      pass

  def test_remove_item_from_cart_when_item_does_not_exist_raises_error():
      pass

  def test_checkout_with_empty_cart_raises_error():
      pass
  ```

### Edge cases
- Include specific edge cases in the test name using `edge_case_<edge_case_name>`.
- Use keywords like `with_valid_params` or `with_invalid_params` depending on the case for different parameter types.

## Fixtures and data mocks naming

When organizing your test fixtures and mock data, consistency and clarity are key. This allows developers to quickly understand the purpose of each fixture or mock, reducing confusion and maintenance overhead.

### Mock fixtures

**Naming pattern**: `mock_<subject>_<scenario>`

- **Description**:  
  When multiple variations of the same mocked functionality are needed, append a scenario descriptor to differentiate them.  
  - `<subject>` identifies the function, class, or external resource being mocked (e.g., `get_users`, `process_order`).  
  - `<scenario>` describes how this particular mock differs from the baseline (e.g., `with_valid_data`, `with_invalid_data`).

- **Examples**:  
  - `mock_get_users_with_valid_data`: A mock fixture simulating the `get_users` function returning valid data.
  - `mock_process_order_with_invalid_data`: A mock fixture simulating a function that processes orders with invalid input.

- **Best practices**:  
  - Keep scenario names concise and descriptive to highlight what distinguishes one mock from another.  
  - Centralize and import predefined data samples from `mock_data.py` to ensure consistent datasets.  
  - Reuse mock fixtures across multiple tests to maintain consistency and reduce duplication.

### Tools fixtures

**Naming pattern**: `<tool_name>`

- **Description**:  
Use this naming convention for fixtures that provide testing utilities or tools rather than mocked functionality. The `<tool_name>` should be clear and self-explanatory, indicating the utility’s purpose or function in the test environment.

- **Examples**:  
  - `client`: A fixture providing a test client instance for making API requests.
  - `mocker`: A fixture integrating `pytest-mock` features for easy mocking.
  - `logger`: A fixture providing a logging tool.
  - `db_connection`: A fixture establishing a database connection for tests.

- **Best practices**:  
  - Keep tool fixtures stateless or idempotent whenever possible.  
  - Avoid embedding business logic; these fixtures should serve as helpers or utilities to facilitate testing.
 
### Data mocks

**Naming pattern**: `<model_name>_<type>_<scenario>`

- **Description**:  
  When multiple variations of the same data model and type are needed, append a scenario descriptor to differentiate them.  
  - `<model_name>` identifies the entity (e.g., `user`, `order`, `product`).  
  - `<type>` indicates the kind of data (e.g., `response`, `payload`, `list`, `detail`).  
  - `<scenario>` describes how this particular data set differs from the baseline (e.g., `valid`, `missing_email`, `empty_list`).

- **Examples**:  
  - `user_response_valid`: A `user_response` mock with valid user data.
  - `user_response_missing_email`: A `user_response` mock where the `email` field is intentionally omitted.
  - `user_response_empty_list`: A `user_response` mock representing an empty result set.

- **Best practices**:  
  - Keep scenario names concise and descriptive to highlight what distinguishes one data set from another.  
  - Store all data mocks in a central file (e.g., `mock_data.py`) for consistency and easy maintenance.  
  - Document each scenario within the mock data file so other developers understand the differences and intended uses of each variant.


## Test directory layout
```
tests/
├── conftest.py             # Shared mocks and tool fixtures
├── mocks/
│   └── base_mock.py        # Abstract BaseMock class
├── unit_tests/             # Unit tests directory
│   ├── components_dir_1/   # Component directory (e.g., /services)
│   │   ├── conftest.py     # Shared mocks fixtures for current component directory
│   │   ├── mock_data.py    # Shared data mocks samples for current component directory
│   │   ├── test_component_dir_1_1.py  # Component test file
│   │   └── test_component_dir_1_2.py
│   │   ...                # Additional component test files
│   ├── component_dir_2/
│   │   ├── conftest.py
│   │   ├── mock_data.py
│   │   ├── test_component_dir_2_1.py
│   │   └── test_component_dir_2_2.py
│   │   ...
│   └── ...                 # Additional component directories
├── integration_tests/      # Integration tests directory (e.g., /views)
│   ├── integration_dir_1/
│   │   ├── conftest.py     # Shared data mocks samples for current integration directory
│   │   ├── mock_data.py    # Shared mocks fixtures for current integration directory
│   │   ├── test_integration_dir_1_1.py      # Integration test file
│   │   └── test_integration_dir_1_2.py
│   │   ...                 # Additional integration test files
│   ├── integration_dir_2/
│   │   ├── conftest.py
│   │   ├── mock_data.py
│   │   ├── test_integration_dir_2_1.py
│   │   └── test_integration_dir_2_2.py
│   │   ...
│   └── ...                 # Additional integration directories

```

## Test-Driven Development (TDD)

Test-Driven Development is a software development methodology in which tests are written before writing the actual code. This approach ensures that the system's functionality is continuously validated and that code changes do not introduce regressions. The process follows a simple cycle: write a failing test, implement the minimum code to pass the test, and then refactor the code for quality and maintainability. TDD encourages writing clean, testable code from the start and improves both the reliability and maintainability of the codebase.

### Red-Green-Refactor methodology

- **Red**: 
  - The first step is to write a test for a feature or functionality that does not exist yet. At this point, the test will fail because the corresponding code has not been written. The failure (Red) is intentional and serves as a signal that the code is   incomplete. This step helps to clarify the desired behavior of the system.
  - **Example**: Write a test that expects a new function, such as `add_item_to_cart()`, to return the updated cart with an item added, even though this function has not been implemented yet.

- **Green**:
  - The second step is to write the minimum amount of code necessary to make the test pass. The goal is not to write the perfect solution but simply to pass the test. Once the test passes (Green), we know that the feature works as expected in the context of the specific test case.
  - **Example**: Implement the `add_item_to_cart()` function with basic logic that adds an item to the cart. This minimal implementation ensures that the test passes, even if the solution is not optimal.

- **Refactor**:
  - The final step is to refactor the code to improve its design, structure, or performance without changing its functionality. This step is performed after the test passes and ensures that the codebase remains clean and maintainable. During this phase, the focus is on eliminating duplication, improving readability, and optimizing performance.
  - **Example**: After making the test pass, refactor the `add_item_to_cart()` function to handle edge cases (e.g., adding items to an empty cart), improve error handling, or apply design patterns for better scalability or flexibility.

### Key principles of TDD:
- **Write Tests First**: Always write a test before writing the implementation. This ensures that the code is testable and that you are focusing on the required functionality.
- **Fail First**: The test should fail initially because the functionality has not been implemented.
- **Small Iterations**: Focus on one small feature or functionality at a time, keeping the iterations short and the scope narrow.
- **Continuous Refactoring**: Refactor code regularly to keep it clean, efficient, and maintainable without changing its external behavior.
- **Confidence in Changes**: With a comprehensive suite of tests, you can make changes to the codebase with confidence, knowing that the tests will catch any regressions or broken functionality.

### Visual studio code test debugging configuration

Follow these steps to configure and debug your tests within Visual Studio Code:

1. **Install python extension**  
   Ensure you have the **Python** extension installed from the VS Code marketplace.

2. **Locate the tests directory**  
   Click the **Testing** icon in the sidebar (the beaker icon) to reveal your tests directory and test files in the UI.

3. **Update `settings.json`**  
   In the `.vscode` directory of your project, add or update the `settings.json` file with the following configuration to enable `pytest`:

   ```json
   {
     "python.testing.pytestArgs": [
       "tests"
     ],
     "python.testing.unittestEnabled": false,
     "python.testing.pytestEnabled": true
   }
4. **Add debug configuration in `launch.json`**
    ```json
    {
      "version": "0.2.0",
      "configurations": [
        {
          "name": "Debug Unit Test",
          "type": "debugpy",
          "request": "launch",
          "justMyCode": false,
          "purpose": ["debug-test"],
          "console": "integratedTerminal",
          "env": {
            "PYTEST_ADDOPTS": "--no-cov"
          }
        }
      ]
    }
5. **Run the tests**
Return to the Testing icon in the sidebar. You should now be able to run and debug your tests directly from the VS Code interface. Once your tests appear in the test explorer, you can run, debug, or view results interactively.
Make sure to put some breakpoints in the test to perform a step by step debugging.
---

## Special thanks
A heartfelt appreciation to the entire automation team. This documentation, along with its standards and practices, is a direct result of our dedication, collaboration, and continuous effort.

