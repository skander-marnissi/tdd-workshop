Debugger configuration for python on Visual studio code:

"configurations": [
        {
            "name": "Custom Python Debugger",
            "type": "debugpy",
            "request": "launch",
            "module": "uvicorn",
            "args": [
                "--port", "PORT_NUMBER",
                "--host", "0.0.0.0",
                "cdp_api_foundation:get_app",
                "--reload",
            ],
            "env": {
                "REQUESTS_CA_BUNDLE": "paste the outputted path of 'python -m unipass' displayed path in here"
                "PYTHONPATH":"${workspaceFolder}/src",
                "OPENAPI_SPEC_PATH": "${workspaceFolder}/src/user_access_manager/openapi_spec.yaml"
            },
            "console": "integratedTerminal",
            "justMyCode": true,
        },
        {
            "name": "Custom Celery Debugger",
            "type": "debugpy",
            "request": "launch",
            "module": "celery",
            "args": [
                "-A", "user_access_manager.celery.workers",
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
            "justMyCode": false,
            "purpose": ["debug-test"],
            "console": "integratedTerminal",
            "env": {
              "PYTEST_ADDOPTS": "--no-cov"
            }
          }
    ]
# VSCode debugger configuration

This `README.md` provides an explanation of the debugger configurations in the `launch.json` file for Visual Studio Code (VSCode). These configurations are set up for debugging Python applications, Celery workers, and tests.

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
This configuration is designed to debug a Python application running with Uvicorn.

#### **Configuration Details**:
```json
{
        "name": "Custom Celery Debugger",
        "type": "debugpy",
        "request": "launch",
        "module": "celery",
        "args": [
        "-A", "dirr_containing_openapi_file.celery.workers",
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
