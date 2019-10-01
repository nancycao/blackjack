deck = {}

def intializeDeck():
    global deck
    for i in range(1, 14):
        deck[i] = 4

def getValue(key):
    global deck
    return deck[key]

def decKey(key):
    global deck
    deck[key] -= 1
