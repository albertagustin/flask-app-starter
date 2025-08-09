# Flask App Starter

A Flask web application starter project with basic scaffolding for tests, using Python 3.9+ and pipenv for dependency management.

Always reference these instructions first and fallback to search or bash commands only when you encounter unexpected information that does not match the info here.

## Working Effectively

- Bootstrap and setup the repository:
  - Ensure Python 3.9+ is installed (`python3 --version`)
  - Install pipenv if not available: `pip install pipenv`
  - **CRITICAL**: pipenv may fail with network timeouts. Use pip fallback instead.
  - Install dependencies: `pip install -r requirements-dev.txt` -- takes 1 second. NEVER CANCEL. Set timeout to 60+ seconds.
  - Alternative (if pipenv works): `pipenv --python python3 install --dev` -- takes 30 seconds. NEVER CANCEL. Set timeout to 120+ seconds.

- Run the application:
  - ALWAYS set PYTHONPATH first: `export PYTHONPATH=.`
  - Start Flask development server: `PYTHONPATH=. FLASK_APP=src.app FLASK_DEBUG=1 flask run --host=127.0.0.1 --port=5001`
  - Use port 5001 instead of default 5000 to avoid conflicts
  - Alternative: `PYTHONPATH=. python runserver.py` (but may conflict on port 5000)

- Test the application:
  - **CRITICAL**: pytest 6.2.4 has compatibility issues with Python 3.12. Upgrade first: `pip install pytest>=7.0.0`
  - **CRITICAL**: Even after upgrade, pytest may still fail due to py package compatibility. Testing may not work with Python 3.12.
  - If pytest works: `PYTHONPATH=. python -m pytest test/` -- takes 5 seconds. NEVER CANCEL. Set timeout to 60+ seconds.
  - Alternative with pipenv (if both pipenv and pytest work): `pipenv run pytest test/`
  - **FALLBACK**: If testing fails, manually validate the application instead.

## Validation

- Always manually validate the Flask application after making changes:
  - Start the application with: `PYTHONPATH=. FLASK_APP=src.app FLASK_DEBUG=1 flask run --host=127.0.0.1 --port=5001`
  - Test the hello world endpoint: `curl -s http://127.0.0.1:5001/helloworld`
  - Expected response: `{"msg": "Hello World!"}`
  - ALWAYS run through at least one complete API request scenario after making changes.

- Linting and formatting:
  - **CRITICAL**: flake8 3.9.2 has compatibility issues with Python 3.12. Skip linting if it fails.
  - **CRITICAL**: autopep8 1.5.7 has compatibility issues with Python 3.12. Skip formatting if it fails.
  - The CI workflow (.github/workflows/flask-app-starter.yml) has commented out linting steps due to these issues.

## Common Tasks

### Dependencies and Python Version Issues
- The Pipfile specifies python_version = "3.9" but the application works with Python 3.12
- When using pipenv with Python 3.12, expect warnings about Python version mismatch - these can be ignored
- **CRITICAL**: pipenv frequently fails with network timeouts. Use pip with requirements-dev.txt instead.
- **CRITICAL**: pytest and related tools have compatibility issues with Python 3.12 due to old package versions

### Running Commands
```bash
# Setup (choose one approach, pip is more reliable)
pip install -r requirements-dev.txt      # ~1 second, reliable
# OR (if pipenv works and no network issues)  
pipenv --python python3 install --dev    # ~30 seconds, may timeout

# Run application
export PYTHONPATH=.
FLASK_APP=src.app FLASK_DEBUG=1 flask run --host=127.0.0.1 --port=5001

# Test application  
curl -s http://127.0.0.1:5001/helloworld

# Run tests (may fail with Python 3.12 compatibility issues)
pip install pytest>=7.0.0               # attempt to fix pytest
PYTHONPATH=. python -m pytest test/     # may still fail due to py package
```

### Project Structure Reference
```
├── Pipfile                             # pipenv dependencies
├── Pipfile.lock                        # locked versions
├── requirements.txt                    # production dependencies  
├── requirements-dev.txt                # development dependencies
├── runserver.py                        # development server wrapper
├── src/
│   ├── app.py                          # Flask application factory
│   ├── views/                          # Blueprint routes
│   │   └── hello_world.py              # /helloworld endpoint
│   └── helpers/                        # reusable logic
├── test/
│   ├── fixtures/                       # pytest fixtures
│   ├── unit/                           # unit tests
│   │   └── views/test_hello_world.py   # tests for hello_world endpoint
│   └── integration/                    # integration tests
└── .github/workflows/                  # CI/CD pipelines
```

### Key Files Content

#### src/app.py
Contains `create_app()` function that:
- Creates Flask app instance
- Registers all blueprints from src.views module
- Configures DEBUG mode from environment

#### src/views/hello_world.py
Blueprint with single GET route `/helloworld` that returns JSON:
```python
@bp.route('/helloworld', methods=['GET'])
def hello_world():
    response = jsonify({'msg': 'Hello World!'})
    response.status_code = 200
    return response
```

#### test/unit/views/test_hello_world.py
Single test that validates the /helloworld endpoint:
- Tests 200 status code
- Tests JSON response format
- Tests correct message content

## Known Issues and Workarounds

1. **Network Timeouts**: pipenv frequently fails with network timeouts
   - Fix: Use `pip install -r requirements-dev.txt` instead
   - Error: `ReadTimeoutError: HTTPSConnectionPool(host='pypi.org', port=443): Read timed out.`

2. **Python Version Compatibility**: Project specified for 3.9 but works with 3.12
   - Use `pipenv --python python3` to force current Python version
   - Ignore version mismatch warnings

3. **pytest Compatibility**: Version 6.2.4 fails with Python 3.12
   - Attempt fix: `pip install pytest>=7.0.0`
   - Error: `AttributeError: 'EntryPoints' object has no attribute 'get'`
   - **CRITICAL**: Even after upgrade, may still fail due to py package (1.10.0) compatibility

4. **flake8 Compatibility**: Version 3.9.2 fails with Python 3.12  
   - Skip linting if it fails
   - Error: `AttributeError: 'EntryPoints' object has no attribute 'get'`

5. **autopep8 Compatibility**: Version 1.5.7 fails with Python 3.12
   - Skip formatting if it fails  
   - Error: `ModuleNotFoundError: No module named 'lib2to3'`

6. **Import Issues**: Python can't find src module without PYTHONPATH
   - Always run: `export PYTHONPATH=.` before running application or tests
   - Alternative: `PYTHONPATH=. command`

7. **Port Conflicts**: Default Flask port 5000 may be in use
   - Use port 5001: `flask run --host=127.0.0.1 --port=5001`
   - Update test URLs accordingly

## Development Workflow

1. **Setup new environment**:
   ```bash
   pip install -r requirements-dev.txt  # 1 second, timeout 60s, reliable
   # OR (if no network issues)
   pipenv --python python3 install --dev  # 30 seconds, timeout 120s, may fail
   ```

2. **Make code changes** in src/ directory

3. **Test changes** (may not work with Python 3.12):
   ```bash
   export PYTHONPATH=.
   pip install pytest>=7.0.0  # attempt fix
   python -m pytest test/      # 5 seconds, timeout 60s, may still fail
   ```

4. **Run application**:
   ```bash
   export PYTHONPATH=.
   FLASK_APP=src.app FLASK_DEBUG=1 flask run --host=127.0.0.1 --port=5001
   ```

5. **Manual validation** (ALWAYS do this since automated tests may fail):
   ```bash
   curl -s http://127.0.0.1:5001/helloworld
   # Should return: {"msg": "Hello World!"}
   ```

6. **Always validate your changes work end-to-end before finishing**

## CI/CD Notes

- GitHub Actions workflow runs on Ubuntu latest with Python 3.9
- Tests run with `pipenv run pytest test/` 
- Linting steps are commented out due to compatibility issues
- Workflow includes custom GitHub Actions examples (test-custom-action, test-composite-action)