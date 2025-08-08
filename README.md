# VSCode debugger configuration

This documentation provides an explanation of the debugger configurations in the `launch.json` file for Visual Studio Code (VSCode). These configurations are set up for debugging Python applications, Celery workers, and tests with `pytest`.

---

## Summary
- [Debugger configurations](#debugger-configurations)
  - [Custom Python debugger](#1-custom-python-debugger)
  - [Custom Celery debugger](#2-custom-celery-debugger)
  - [Custom test debugger](#3-custom-test-debugger)
- [Configuration example](#configuration-example)
- [Run your debbuger](#run-your-debugger)
  - [Step 1](#step-1)
  - [Step 2](#step-2)
  - [Step 3](#step-3)
  
  
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

## Configuration example
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
```
## Run your debugger

### Step 1
After setting your configuration click on the `Run and Debug` icon locate on the left sidebar (or by shortcut `Ctrl+Shift+D`) to open the debug view. 

### Step 2
On the top of the view you will find a dropdown list containing your different configuration, chose one debug configuration and press `Start Debugging` button (or by shortcut `F5`).
[Image]

### Step 3
Check if your debugger is running well in your terminal.
[image-step-3-1]

You can then put some breakpoints, run your scripts and follow the process step by step.
[image-step-3-2]


```yaml
spec:
  replicas: 1
  selector:
    matchLabels:
      app: celery-worker
  template:
    metadata:
      labels:
        app: celery-worker
    spec:
      containers:
      - name: worker
        image: your-celery-image
        command: ["celery", "-A", "your_project", "worker", "--loglevel=info"]
        livenessProbe:
          exec:
            command: ["/bin/sh", "-c", "python3 /path/to/celery-healthcheck.py"]
          initialDelaySeconds: 10
          periodSeconds: 30
          failureThreshold: 3
        readinessProbe:
          exec:
            command: ["/bin/sh", "-c", "python3 /path/to/celery-healthcheck.py"]
          initialDelaySeconds: 5
          periodSeconds: 10
          failureThreshold: 2
```
______

Slide 1 — Title Slide

Title:
🚀 Why We Should Switch to Poetry

Subtitle:
A Modern Approach to Python Dependency Management

Notes:
Set the tone — this is a pragmatic pitch, not just a hype talk.

⸻

Slide 2 — The Current Situation

Title:
🔧 Python Project Management Today

Content (Bullets):
	•	pip + requirements.txt is basic and manual
	•	No built-in project metadata management
	•	Dependency conflicts are common
	•	Manual version pinning & updates
	•	Separate tools for packaging (e.g., setuptools)

Notes:
Explain the fragmented tooling landscape with classic pip workflows.

⸻

Slide 3 — What is Poetry?

Title:
🛠️ Poetry — The All-in-One Tool

Content (Bullets):
	•	Dependency management + packaging + publishing
	•	Single source of truth: pyproject.toml
	•	Reproducible installs with poetry.lock
	•	Virtual environment management included
	•	Built-in version resolver

Notes:
Highlight it’s not just a package manager — it’s a complete ecosystem.

⸻

Slide 4 — Key Advantages for Developers

Title:
👩‍💻 Why Developers Love Poetry

Content (Bullets):
	•	Simple commands for adding/removing packages
	•	Automatic dependency resolution
	•	Consistent environments across dev/test/CI
	•	Simplifies onboarding new developers
	•	Clean pyproject.toml for project config

Notes:
Focus on daily workflow improvements.

⸻

Slide 5 — Advantages for Teams & CI/CD

Title:
🤝 Why Teams & Pipelines Love Poetry

Content (Bullets):
	•	Lockfile guarantees reproducibility
	•	Easy integration with CI/CD
	•	Standardized project layout
	•	Compatible with modern Python build tools
	•	Easier dependency upgrades & tracking

Notes:
Position Poetry as a reliability & governance tool for teams.

⸻

Slide 6 — Addressing Common Objections

Title:
❓ Common Questions & Misconceptions

Content (Bullets):
	•	✅ “It works with pip” — Yes, Poetry can export requirements.txt
	•	✅ “Learning curve?” — Simple commands, great docs
	•	✅ “Mature enough?” — Used in production by major projects
	•	✅ “Performance?” — Faster dependency resolution with new resolver

Notes:
Preempt resistance by clearing misconceptions.

⸻

Slide 7 — Summary & Recommendation

Title:
🚩 Why We Should Adopt Poetry

Content (Bullets):
	•	Unified tool simplifies development & maintenance
	•	Reduces risk of dependency conflicts
	•	Eases project setup, onboarding, and CI/CD integration
	•	Future-proof with modern Python standards

Bottom Line:
👉 Let’s pilot Poetry in our next project!

Slide 6 — Poetry vs. Pipenv

Title:
⚖️ Poetry vs. Pipenv — Key Differences


| Feature                  | Poetry                        | Pipenv                     |
|--------------------------|-------------------------------|-----------------------------|
| **Project Metadata**     | ✅ Built-in (PEP 621)         | ❌ Needs setup.cfg or other tools |
| **Dependency Resolver**  | ✅ Fast & reliable             | ⚠️ Known resolver issues      |
| **Packaging & Build**    | ✅ Included (PEP 517 compliant) | ❌ Not designed for packaging |
| **Virtual Environment**  | ✅ Integrated & automatic      | ✅ Integrated                 |
| **Popularity & Adoption**| 📈 Growing & stable           | 📉 Declining since 2021      |
| **CLI Experience**       | ✅ Intuitive & consistent      | ⚠️ Sometimes confusing        |
| **Python Version Control** | ✅ Integrated in pyproject.toml | ✅ Managed with Pipfile      |

Notes:
Explain that while Pipenv was promising, it didn’t evolve — Poetry is actively maintained, follows Python packaging standards, and works both for libraries and apps.



USER STORY

Who ?: Automation Team
What ?: Want to plan a meeting to have feedback from other tribes about difficulties to update DMAP
Why ?: To decide if we will suggest a new process to Security team.

FUNCTIONAL DETAILS

The Automation Team must plan a meeting with other tribes' member when they will be back from holidays (plan now for the future while their calendars are not completely full)












Hi everyone,

Hope you’re all doing well and enjoying the summer!

The Automation Team would like to plan a short meeting (post-holidays) with members from different tribes to gather your feedback on the current difficulties in updating DMAP. The goal is to understand the pain points and decide whether we should propose a new process to the Security team.

We’re reaching out now to make sure we can find a slot before everyone’s calendars start to fill up again. Could you please let us know your general availability for the end of August / early September?

Looking forward to hearing from you!

Best regards,
[Your Name]
On behalf of the Automation Team
