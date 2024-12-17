{
    "python.testing.pytestArgs": [
        "tests"
    ],
    "python.testing.unittestEnabled": false,
    "python.testing.pytestEnabled": true
}
{
    // Use IntelliSense to learn about possible attributes.
    // Hover to view descriptions of existing attributes.
    // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
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
       }]
}
