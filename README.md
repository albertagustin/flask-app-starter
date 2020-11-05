# Flask App Starter

A basic Flask App Starter used as a base for my personal/work projects. It incorporates various setup and examples based on my own personal experiences bulding Flask apps.

## Pre-Reqs

1. [vscode](https://code.visualstudio.com/)
2. [git](https://git-scm.com/)
3. [Python 3.8+](https://www.python.org/)
4. [pipenv](https://pipenv.pypa.io/en/latest/)
5. [direnv](https://direnv.net/)

## Dev Setup

```bash
# clone the repo
git clone https://github.com/albertagustin/flask-app-starter.git

# setup the python environment
pipenv install          # only app dependencies

pipenv install --dev    # app + dev dependencies

# running dev server
pipenv shell            # enable the python virtual env
python runserver.py     # runs the dev server

# testing
pytest test
```

## Project Structure

```bash
.
├── Dockerfile
├── Jenkinsfile
├── Pipfile
├── Pipfile.lock
├── Procfile                                     # PCF Procfile
├── README.md
├── flask_app_starter.http                       # vscode REST Client file
├── manifest.yml                                 # PCF manifest
├── runserver.py
├── src                                          # primary source code
│   ├── app.py
│   ├── helpers                                  # helper classes
│   │   ├── base_helper.py
│   │   ├── flask_helper.py
│   │   └── sample_helper.py
│   └── views                                    # api endpoints
│       └── sample.py
└── test                                         # testing source code
    ├── conftest.py                              # pytest conftest
    ├── files                                    # test files
    │   ├── ip_fail.json
    │   └── ip_success.json
    ├── fixtures                                 # pytest fixtures
    │   ├── app_fixtures.py
    │   ├── helpers
    │   │   └── sample_helper_fixtures.py
    │   └── views
    │       └── __init__.py
    ├── helpers                                  # helper fixtures
    │   └── fixtures_helper.py
    ├── integration                              # integration tests
    │   └── __init__.py
    └── unit                                     # unit tests
        ├── helpers
        │   └── test_sample_helper.py
        └── views
            └── test_sample.py
```

## Scaffolding & Examples

This app has scaffolding and examples for the following:

- Python 3.8+ virtual environment using `pipenv`.
- Python linting using `flake8` and `autopep8`.
- Basic [Flask](https://flask.palletsprojects.com/en/1.1.x/) app w/ simple project structure and auto-reloading dev server.
- Unit testing using:
  - [pytest](https://docs.pytest.org/en/stable/)
  - [pytest-flask](https://pytest-flask.readthedocs.io/en/latest/)
  - [requests-mock](https://requests-mock.readthedocs.io/en/latest/)
- Testing concepts:
  - [fixtures](https://docs.pytest.org/en/stable/fixture.html)
  - [monkeypatching](https://docs.pytest.org/en/stable/monkeypatch.html)
- Production Deployment using:
  - [Gunicorn HTTP Server](https://gunicorn.org/)
  - [Docker](https://www.docker.com/)
  - [Pivotal Cloud Foundry](https://www.cloudfoundry.org/)

## CI/CD

## Production Server
