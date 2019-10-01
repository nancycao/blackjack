# blackjack
KP Fellowship Application

### Instructions for running game:
```python
python blackjack.py
```

### Design choices and any data structures or algorithms Implemented
I decided to put the game functionality within ```blackjack.py``` and handle functionality regarding the cards, including the user cards, dealer cards to draw from, in ```cards.py```. I represented the user cards, dealer cards as global variables in ```cards.py```. In restropect and with more time, I would have implemented a more general Cards object that would represent user cards or dealer cards. 

### Choice of tooling (language, libraries, test runner, etc.) and Rationale
I chose Python because the task to create a lightweight Blackjack terminal game within 3 hours. Its simple syntax and availability of libraries helped me complete the project within the timeframe. For example, I used Python's random library in order to implement the random draw of a card from a deck.
