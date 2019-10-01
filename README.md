# blackjack
KP Fellowship Application

### Instructions for running game:
```python
python blackjack.py
```

### Design choices and any data structures or algorithms Implemented
I decided to put the game functionality within ```blackjack.py```. I handled the card functionality regarding the user cards and dealer cards in ```cards.py```. I handled the card deck functionality in ```deck.py```. 
In ```deck.py```, I represented the deck of cards I would draw from as a dictionary with the card values as keys and the number of cards left in the deck as its value. 
I represented the user cards, dealer cards as global variables in ```cards.py```. In restropect and with more time, I would have implemented a more general Cards object that would represent user cards or dealer cards. The current card functions would then be class functions to modify the Cards object. 
Lastly, I put the overall game logic in ```blackjack.py```.

### Choice of tooling (language, libraries, test runner, etc.) and Rationale
I chose Python because the task to create a lightweight Blackjack terminal game within 3 hours. Its simple syntax and availability of libraries helped me complete the project within the timeframe. For example, I used Python's random library in order to implement the random draw of a card from a deck. With more time, I would have tested this code by implementing unit tests for functions such as ```getSumCards()``` to check if its output is what I expected.
