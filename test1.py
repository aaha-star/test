
language: python
python:
  - "2.7"
# command to install dependencies
install:
    - pip install flake8 flake8-respect-noqa pre-commit
# command to run tests
script:
    - make tes
print("hello")
