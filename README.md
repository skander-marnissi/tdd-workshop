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
# VSCode Debugger Configuration

This `README.md` provides an explanation of the debugger configurations in the `launch.json` file for Visual Studio Code (VSCode). These configurations are set up for debugging Python applications, Celery workers, and tests.

---

## Debugger Configurations

### 1. Custom Python Debugger

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
    "OPENAPI_SPEC_PATH": "${workspaceFolder}/src/user_access_manager/openapi_spec.yaml"
  },
  "console": "integratedTerminal",
  "justMyCode": true
}
