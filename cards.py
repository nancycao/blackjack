import random
import deck

userCards = []
dealerCards = []

def pickCard():
    randomCard = random.randint(1,13)
    while deck.getValue(randomCard) == 0:
        randomCard = random.randint(1,13)
    deck.decKey(randomCard)
    return randomCard

def userHit():
    userCard = pickCard()
    userCards.append(userCard)

def dealerHit():
    dealerCard = pickCard()
    dealerCards.append(dealerCard)

def getSumCards(cards):
    hasAce = False
    sumUserCards = 0
    for card in cards:
        if (((card == 11) or card == 12) or card == 13):
            sumUserCards += 10
        else:
            if card == 1:
                hasAce = True
            sumUserCards += card
    if hasAce:
        altSum = sumUserCards + 10
        if altSum <= 21:
            return [sumUserCards, altSum]
        else:
            return [sumUserCards]
    return [sumUserCards]

def getSumDealerCards():
    return getSumCards(dealerCards)

def getSumUserCards():
    return getSumCards(userCards)

def convertCardtoString(card):
    if card == 1:
        return 'A'
    elif card == 11:
        return 'J'
    elif card == 12:
        return 'Q'
    elif card == 13:
        return 'K'
    else:
        return str(card)

def printUserCards():
    userCardMessage = "Your cards: "
    for card in userCards:
        userCardMessage += convertCardtoString(card)
        userCardMessage += " "
    print(userCardMessage)
    sumUserCardsMessage = "Your Total: "
    sumUserCards = getSumCards(userCards)
    sumUserCardsMessage += str(sumUserCards[0])
    if len(sumUserCards) == 2:
        sumUserCardsMessage += " or " + str(sumUserCards[1])
    print(sumUserCardsMessage)

def printDealerCards(hidden):
    dealerCardMessage = "Dealer's cards: "
    if hidden:
        firstDealerCard = dealerCards[0]
        dealerCardMessage += convertCardtoString(firstDealerCard)
        dealerCardMessage += " X"
    else:
        for card in dealerCards:
            if card == 1:
                hasAce = True
            dealerCardMessage += convertCardtoString(card)
            dealerCardMessage += " "
        dealerCardMessage += '\n'
        dealerCardMessage += "Dealer's Total: "
        sumDealerCards = getSumCards(dealerCards)
        dealerCardMessage += str(max(sumDealerCards))
    print(dealerCardMessage)

def reset():
    global userCards
    global dealerCards
    userCards = []
    dealerCards = []
