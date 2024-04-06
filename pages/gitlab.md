## Gitlab CI

### Pipelines

Gitlab CI contains of two stages: 
- **quality**. On this stage gitlab runner checks that all linters pass without errors.
- **tests**. On this stage gitlab runner test the application with `pytest`.

![gitlab-ci-pipeline.png](gitlab-ci-pipeline.png)

### Code quality
Reports from `ruff` and `mypy` are also displayed in "Code quality" section.
If linters find any errors, they will be showed there.
![gitlab-ci-code-quality.png](gitlab-ci-code-quality.png)

### Tests
Test report is also available in a merge request. You can click on "Full reports" to 
see the result of each individual test.
![gitlab-ci-passed-tests.png](gitlab-ci-passed-tests.png)

