---
name: copilot-agent
about: A template used for issues assigned to Copilot Coding Agent
title: "[COPILOT]"
labels: ''
assignees: ''

---

Title: Give the issue an appropriate title. 

`Example: Migrate server tests from unittest to pytest`

Body: A general overview of the issue.

`Example: We are looking to migrate from unittest to pytest to take advantage of some pytest specific features.`

Requirements: A list of requirements to complete for the issue.

```
Example:
- A new folder called `migrated_tests` will be created with the new pytest tests.
- All existing unittests are rewritten using pytest style in the `migrated_tests` folder, keeping the exact same functionality and code coverage.
- Documentation is updated, highlighting the migration and steps required to run the new tests.
- All new tests pass.
```

Existing resources: Additional information describing existing resources that would be useful to solve the issue.

```
Example:
- All existing tests exist in `server/tests`
- There is a script at `scripts/run-server-tests.sh` which is used to run tests and generate code coverage reports
```

Recommended approach: A recommended step-by-step for Copilot to use to solve the issue.

```
Example:
- Explore existing tests to determine their functionality
- Read the coverage reports to determine existing code coverage
- Recreate the tests one by one, testing along the way, to ensure compatibility
- Run all tests at the end to ensure everything passes
- Generate a code coverage report to demonstrate code coverage has been maintained
- Generate documentation of the migration and how to run the new tests
```
