Debugger configuration for python on Visual studio code:

"version": "0.2.0",
    "configurations": [
        {
            "name": "Python Debugger",
            "type": "debugpy",
            "request": "launch",
            "module": "uvicorn",
            "args": [
                "--port", "5002",
                "--host", "0.0.0.0",
                "cdp_api_foundation:get_app",
                "--reload",
        
            ],
            "env": {
                "REQUESTS_CA_BUNDLE": "paste the outputted path of 'python -m unipass' displayed path in here",
                "PYTHONPATH":"${workspaceFolder}/src",
                "OPENAPI_SPEC_PATH": "${workspaceFolder}/src/cd_usage_declaration/openapi_spec.yaml"
            },
            "console": "integratedTerminal",
            "justMyCode": true,
        }
}]
