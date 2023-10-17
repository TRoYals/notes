---
title: 03python项目搭建流程
date: 2023-06-24 23:59
article: false
---

1. 安装 [[02Poetry]]
2. > poetry new sample_template
3. > poetry shell
4. > poetry add **packages**
5. > poetry install  
   > \[可选]
6. > poetry add mypy --dev
7. > poetry add flake8 --dev
8. > poetry add pytest --dev
9. 写一个 Makefile

```
.PHONY: format lint tests integration_tests

format:
	poetry run black .
	poetry run isort .

lint:
	poetry run mypy .
	poetry run black . --check
	poetry run isort . --check
	poetry run flake8 .

tests:
	poetry run pytest tests/unit_tests

integration_tests:
	poetry run pytest tests/integration_tests
```

5. 创造一个.flake8

```
[flake8]
exclude =
    .venv
    __pycache__
    notebooks
# Recommend matching the black line length (default 88),
# rather than using the flake8 default of 79:
max-line-length = 88
extend-ignore =
    # See https://github.com/PyCQA/pycodestyle/issues/373
    E203,


```

6. .gitignore  
   需要涵盖以下几个方面的内容  
   [gitignore.io - Create Useful .gitignore Files For Your Project](https://www.toptal.com/developers/gitignore/)  
   mac 还需要放 DS.Store
