# VSCode debugger configuration

This documentation provides an explanation of the debugger configurations in the `launch.json` file for Visual Studio Code (VSCode). These configurations are set up for debugging Python applications, Celery workers, and tests with `pytest`.

---

## Summary
- [Debugger configurations](#required-tests)
  - [Unit tests](#unit-tests)
  - [Integration tests](#integration-tests)
- [Test dependencies](#test-dependencies)
  - [Testing dependency](#testing-dependency)
  - [Coverage](#coverage)
  - [Mocks and stubbing](#mocks-and-stubbing)
  - [Performance and stress testing](#performance-and-stress-testing)
  - [Specialized testing](#specialized-testing)
- [Test configuration](#test-configuration)
  - [Test configurations](#test-configurations)
  - [Pytest configuration](#pytest-configuration)
- [Tests naming patterns](#tests-naming-patterns)
  - [Test files](#test-files)
  - [Test methods](#test-methods)
  - [Edge cases](#edge-cases)
- [Tests directory layout](#tests-directory-layout)
- [Mocking](#mocking)
  - [General guidelines](#general-guidelines)
  - [Mocking third-Party Systems](#mocking-third-party-systems)
  - [Database mocking Options](#database-mocking-options-to-be-studied)
- [Fixtures and data mocks naming](#fixtures-and-data-mocks-naming)
  - [Mock fixtures](#mock-fixtures)
  - [Tools fixtures](#tools-fixtures)
  - [Data mocks](#data-mocks)
- [Test coverage](#test-coverage)
  - [Coverage requirements](#coverage-requirements)
  - [Coverage configuration](#coverage-configuration)
  - [Checking coverage](#checking-coverage)
- [Test-Driven development (TDD)](#test-driven-development-tdd)
  - [Red-Green-refactor Methodology](#red-green-refactor-methodology)
  - [Key principles of TDD](#key-principles-of-tdd)
- [Visual studio code test debugging configuration](#visual-studio-code-test-debugging-configuration)
- [Special thanks](#special-thanks)

---

## Debugger configurations

### 1. Custom Python debugger

#### **Purpose**:
This configuration is designed to debug a Python application running with Uvicorn.

#### **Configuration Details**:
```json
{
        "name": "Custom Python Debugger",
        "type": "debugpy",
        "request": "launch",
        "module": "uvicorn",
        "args": [
        "--port", "PORT_NUMBER",
        "--host", "0.0.0.0",
        "cdp_api_foundation:get_app",
        "--reload"
        ],
        "env": {
        "REQUESTS_CA_BUNDLE": "paste the outputted path of 'python -m unipass' displayed path in here",
        "PYTHONPATH": "${workspaceFolder}/src",
        "OPENAPI_SPEC_PATH": "${workspaceFolder}/src/dirr_containing_openapi_file/openapi_spec.yaml"
        },
        "console": "integratedTerminal",
        "justMyCode": true
}
```

#### **Explanation**:
- **`name`**: The identifier for this configuration (`Custom Python Debugger`).
- **`type`**: Specifies the debugger type (`debugpy` for Python debugging).
- **`request`**: Defines the debug request type (`launch` starts the application).
- **`module`**: The Python module to run (`uvicorn`).
- **`args`**: Command-line arguments for Uvicorn:
  - `--port`: Port number for the application.
  - `--host`: Host address (default `0.0.0.0`).
  - `cdp_api_foundation:get_app`: Specifies the app callable.
  - `--reload`: Enables auto-reloading for development.
- **`env`**: Environment variables:
  - `REQUESTS_CA_BUNDLE`: CA bundle path generated via `python -m unipass`.
  - `PYTHONPATH`: Sets the Python module search path.
  - `OPENAPI_SPEC_PATH`: Path to the OpenAPI specification file.
- **`console`**: Use the integrated terminal for output.
- **`justMyCode`**: Debug only user code (`true`).

### 2. Custom Celery debugger

#### **Purpose**:
This configuration is tailored for debugging Celery workers.

#### **Configuration Details**:
```json
{
        "name": "Custom Celery Debugger",
        "type": "debugpy",
        "request": "launch",
        "module": "celery",
        "args": [
        "-A", "dirr_containing_celery_launch_file.celery.workers",
        "worker",
        "--loglevel","INFO",
        "--concurrency","2",
        "-P","solo"
        ],
        "env": {
        "PYTHONPATH":"${workspaceFolder}/src",
        },
        "console": "integratedTerminal",
        "justMyCode": true,
 }
```

#### **Explanation**:
- **`name`**: The identifier for this configuration (`Custom Celery Debugger`).
- **`type`**: Specifies the debugger type (`debugpy` for Python debugging).
- **`request`**: Defines the debug request type (`launch` starts the application).
- **`module`**: The Python module to run (`celery`).
- **`args`**: Command-line arguments for Celery:
  - `-A`: Specifies the application (`app_name.celery.worker`).
  - `worker`: Runs the Celery worker process.
  - `--loglevel`: Logging level for Celery (`INFO).
  - `--concurrency`: Number of worker processes (`2`).
  - `-P`: Pool type (solo).
- **`env`**: Environment variables:
  - `PYTHONPATH`: Sets the Python module search path.
- **`console`**: Use the integrated terminal for output.
- **`justMyCode`**: Debug only user code (`true`).

### 3. Custom test debugger

#### **Purpose**:
This configuration is designed to debug python tests.

#### **Configuration Details**:
```json
 {
        "name": "Custom Test Debugger",
        "type": "debugpy",
        "request": "launch",
        "purpose": ["debug-test"],
        "env": {
        "PYTEST_ADDOPTS": "--no-cov"
        },
        "console": "integratedTerminal",
        "justMyCode": false
}
```

#### **Explanation**:
- **`name`**: The identifier for this configuration (`Custom Test Debugger`).
- **`type`**: Specifies the debugger type (`debugpy` for Python debugging).
- **`request`**: Defines the debug request type (`launch` starts the application).
- **`purpose`**: Designated purpose for test debugging.
- **`env`**: Environment variables:
  - `PUTEST_ADDOPTS`: Adds additional options for pytest (`--no-cov` disables coverage reports).
- **`console`**: Use the integrated terminal for output.
- **`justMyCode`**: Debug only user code (`false`).
  
##### <ins>**Note**:</ins>
To run correctly this configuration you will have to install the `Python` extension on VSCode.

### 4. Example of whole debbug configuration in `launch.json` file
```json
{
    "version": "VERSION",
    "configurations": [
        {
                "name": "Custom Python Debugger",
                "type": "debugpy",
                "request": "launch",
                "module": "uvicorn",
                "args": [
                "--port", "5000",
                "--host", "0.0.0.0",
                "cdp_api_foundation:get_app",
                "--reload"
                ],
                "env": {
                "REQUESTS_CA_BUNDLE": "paste the outputted path of 'python -m unipass' displayed path in here",
                "PYTHONPATH": "${workspaceFolder}/src",
                "OPENAPI_SPEC_PATH": "${workspaceFolder}/src/dirr_containing_openapi_file/openapi_spec.yaml"
                },
                "console": "integratedTerminal",
                "justMyCode": true
        },
        {
                "name": "Custom Celery Debugger",
                "type": "debugpy",
                "request": "launch",
                "module": "celery",
                "args": [
                "-A", "dirr_containing_celery_launch_file.celery.workers",
                "worker",
                "--loglevel","INFO",
                "--concurrency","2",
                "-P","solo"
                ],
                "env": {
                "PYTHONPATH":"${workspaceFolder}/src",
                },
                "console": "integratedTerminal",
                "justMyCode": true,
         },
         {
                "name": "Custom Test Debugger",
                "type": "debugpy",
                "request": "launch",
                "purpose": ["debug-test"],
                "env": {
                "PYTEST_ADDOPTS": "--no-cov"
                },
                "console": "integratedTerminal",
                "justMyCode": false
        }
    ]
}
