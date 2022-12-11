# Geting the virtual environment set up

I set up the environment for testing with TOX. We will use both Pytest and Unittest. Not an expert in either but I think it's a good idea to use both. I put an example `basic.py` we used in class some time ago to start the coverage.

Yo must follow the instructions below to get the environment set up. Or find the ones for your OS. I'm using a Mac.

---

## VS Code for Mac

- Open the terminal in your project folder (in VS Code)
- python3 -m venv venv
- source .venv/bin/activate
- pip install -r requirements.txt

---

## Tox

I'm using Python 3.11 but in requiremts.txt I put both 3.11 and 3.10 so it will not matter what version you have installed.
But i recommand you to upgrade to 3.11, is faster and the error messages are better.

- run **tox** in the terminal

---

## Pytest

- run tox or next command if you don't want to use tox
- run **pytest** in the terminal

---

## Unittest

- run tox or next command if you don't want to use tox
- run **python -m unittest** in the terminal

---

Back to [Frontpage](../README.md)