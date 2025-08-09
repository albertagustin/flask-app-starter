# Flask App Starter

A starter for a simple Flask app that I use for my projects with integration of pytest and basic scaffolding for tests.

## Project Setup

1. Install python, pyenv

2. Install python virtual env, pkgs, enable shell

   ```bash
   pipenv install --dev

   pipenv shell
   ```

3. Run the tests

   ```bash
   pytest test/

   >>
      ================================================================================================= test session starts =================================================================================================
      platform darwin -- Python 3.13.0, pytest-8.4.1, py-1.11.0, pluggy-1.5.0
      rootdir: /flask-app-starter
      plugins: requests-mock-1.8.0, flask-1.2.0
      collected 1 item

      test/unit/views/test_hello_world.py .
   ```

4. Run the local dev server, make a call

   ```bash
   python runserver.py

   >>
      * Serving Flask app "src.app" (lazy loading)
      * Environment: production
         WARNING: This is a development server. Do not use it in a production deployment.
         Use a production WSGI server instead.
      * Debug mode: on
      * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
      * Restarting with stat
      * Debugger is active!
      * Debugger PIN: 151-649-030
      127.0.0.1 - - [04/Apr/2021 18:43:28] "GET /helloworld HTTP/1.1" 200 -
      ...

   curl --request GET \
      --url http://127.0.0.1:5000/helloworld

   >>
      {
         "msg": "Hello World!"
      }
   ```

5. Make code changes, see the changes

   ```bash
   * Detected change in '/flask-app-starter/src/views/hello_world.py', reloading
   * Restarting with stat
   * Debugger is active!
   * Debugger PIN: 151-649-030
   127.0.0.1 - - [04/Apr/2021 18:44:47] "GET /helloworld HTTP/1.1" 200 -

   curl --request GET \
      --url http://127.0.0.1:5000/helloworld

   >>
      {
         "msg": "Hello You!"
      }
   ```

## Directory Structure

```bash
├── Pipfile
├── Pipfile.lock
├── README.md
├── docs                                  # documentation
├── runserver.py                          # wrapper for the dev server
├── src
│   ├── app.py                            # define Flask app
│   ├── helpers                           # re-usable logic
│   └── views                             # flask routes
├── test
│   ├── files                             # files useful for testing/mocks
│   ├── fixtures                          # pytest fixtures
│   ├── helpers                           # test helpers
│   ├── integration                       # integration tests
│   └── unit                              # unit tests
│       └── conftest.py                   # pytest conftest
└── test.http                             # vscode rest-client file
```
