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
