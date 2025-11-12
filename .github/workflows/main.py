name: Python CI

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  build:

    runs-on: ubuntu-latest

    steps:
    - name: Checkout репозитория
      uses: actions/checkout@v3

    - name: Установить Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.10'

    - name: Установить зависимости
      run: |
        python -m pip install --upgrade pip
        pip install pytest

    - name: Запустить тесты
      run: |
        pytest tests/
