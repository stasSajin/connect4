# connect4
I assume you have a Python installed.


To get started, follow these steps:
1. Run `make local-setup`. This will install poetry and set up a local venv. It will also install library dependencies from the lock file.
2. Run `make tests`. This will run the tests. If things run, it means that your setup is complete.
3. Run `streamlit run connect4/game.py`. This will run the game in the browser.

### Improvements
There are some improvements that can be made to the game.
* AI Bot: is designed to be super simple and prevent a user form winning or capitalizing on putting a puck in a winning position. A better algorithm would be to use [minimax](https://en.wikipedia.org/wiki/Minimax).
* Validators: I don't do much to validate game configuration inputs. Those needs to be tested through a validator class.
