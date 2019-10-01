import cards
import deck

stopGame = False

'''
Deals two cards to user and dealer.
'''
def start():
    for i in range(2):
        cards.userHit()
        cards.dealerHit()

'''
Game logic for user's HIT and STAND actions.
'''
def userPlay():
    global stopGame
    print("Enter h for HIT or s for STAND.")
    action = str(input())
    if action == "h":
        cards.userHit()
        checkPlayerBusted()
    if action == "s":
        stopGame = True

'''
Evaluates and prints game result.
'''
def end():
    if cards.getSumUserCards()[0] > 21:
        print("You busted!")
        cards.printUserCards()
    else:
        dealerPlay()
        cards.printUserCards()
        cards.printDealerCards(False)
        if (cards.getSumDealerCards()[0] > 21):
            print("You win! Dealer busted!")
        else:
            if max(cards.getSumDealerCards()) > max(cards.getSumUserCards()):
                print("Dealer wins!")
            elif max(cards.getSumDealerCards()) < max(cards.getSumUserCards()):
                print("You win!")
            else:
                print("Tie!")

'''
Determines whether player wants to play again.
Runs game again if player wants to play again.
'''
def playAgain():
    global userCards
    global dealerCards
    global stopGame
    print("Play again? Enter y for YES. Any other input is NO.")
    action = str(input())
    if action == "y":
        cards.reset()
        deck.intializeDeck()
        stopGame = False
        print('\n')
        main()

'''
Checks if player busted.
If player busted, updates stopGame.
'''
def checkPlayerBusted():
    global stopGame
    if cards.getSumUserCards()[0] > 21:
        stopGame = True
    return stopGame

'''
Game logic for dealer's actions after player has finished their turn.
'''
def dealerPlay():
    over17 = False
    while not over17:
        sumDealerCards = cards.getSumDealerCards()
        if sumDealerCards[0] >= 17:
            over17 = True
        elif len(sumDealerCards) == 2:
            if sumDealerCards[1] >= 17:
                over17 = True
        else:
            cards.dealerHit()

def main():
    global stopGame
    deck.intializeDeck()
    start()
    while not stopGame:
        cards.printDealerCards(True)
        cards.printUserCards()
        userPlay()
        print('\n')
    end()
    playAgain()

main()
