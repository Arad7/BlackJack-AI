import random
import math

playerIn = True
dealerIn = True


# 1: deck of cards/player dealing hand
player = True
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10,
        'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A']
playerHand = []
dealerHand = []


# 2: deal cards
def dealCard(turn):
    card = random.choice(deck)
    turn.append(card)
    deck.remove(card)


# 3: calculate the total of each hand
def total(turn):
    total = 0
    face = ['J', 'K', 'Q']
    for card in turn:
        if card in range(1, 11):
            total = total + card
        elif card in face:
            total = total + 10
        else:
            if total > 11:
                total = total + 1
            else:
                total = total + 11
    return total


# 4: check for winner
def revealDealerHand():
    if len(dealerHand) == 2:
        return dealerHand[0]
    elif len(dealerHand) > 2:
        return dealerHand[0], dealerHand[1]

def utility2(yoursum):
    percent1 = round((1/13)*100,2)
    percent2 = round((4/13)*100,2)
    if yoursum < 11:
        return("Since you have a sum of less than 11, there is a 0% chance of you busting and 0% chance of you getting blackjack")
    elif yoursum == 11:
        return("Since you have a sum of 11, there is around a " + str(percent2) + "% chance of you getting blackjack and 0% chance of you busting")
    elif yoursum > 11 and yoursum < 21:
        percent3 = round((((yoursum-10)+2)/13)*100,2)
        return("Since you have a sum of " + str(yoursum) + ", there is a " + str(percent1) + "% chance of you getting a blackjack and a " +
              str(percent3) + "% chance of you busting")

def sumDealerHand():
    check = 0
    if len(dealerHand) == 2:
        if dealerHand[0] == 'J'or dealerHand[0] == 'Q' or dealerHand[0] == 'K':
            check += 10
            return check
        elif dealerHand[0] == 'A':
            if total(dealerHand) > 11:
                check += 1
            else:
                check += 11
               
            return check
           
        else:
            return(dealerHand[0])
       
    elif len(dealerHand) > 2:
        try:
            return dealerHand[0] + dealerHand[1]
       
        except:
            if dealerHand[0] == 'J'or dealerHand[0] == 'Q' or dealerHand[0] == 'K':
                check += 10
               
            elif dealerHand[0] == 'A':
                if total(dealerHand) > 11:
                    check += 1
                else:
                    check += 11
               
            else:
                check += dealerHand[0]
            if dealerHand[1] == 'J'or dealerHand[1] == 'Q' or dealerHand[1] == 'K':
                check += 10
               
            elif dealerHand[1] == 'A':
                if total(dealerHand) > 11:
                    check += 1
                else:
                    check += 11
               
            else:
                check += dealerHand[1]
               
        return (check)


def utility(yoursum, deal):
    expectedval = 6.5
    if yoursum < 15:
        return ("AI recommends to hit")
    elif (deal + expectedval) > yoursum and (deal + expectedval) < 21:
        return ("AI recommends to hit")
    elif yoursum + expectedval > 21:
        return ("AI recommends to stay")
    else:
        return ("AI recommends to stay")


# 5: game loop
for _ in range(2):
    dealCard(dealerHand)
    dealCard(playerHand)

while playerIn or dealerIn:
    print(f"Dealer had {revealDealerHand()} and X")
    print(f"You have {playerHand} for a total of {total(playerHand)}")
    if playerIn:
        print(utility2(total(playerHand)))
        print(utility(total(playerHand), sumDealerHand()))

        stayOrHit = input("1: Stay\n2: Hit\n")
    if total(dealerHand) > 16:
        dealerIn = False
    else:
        dealCard(dealerHand)
    if stayOrHit == '1':
        playerIn = False
    else:
        dealCard(playerHand)
    if total(playerHand) >= 21:
        break
    elif total(dealerHand) >= 21:
        break
if total(dealerHand) == total(playerHand):
    print(
        f"\nYou have {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}")
    print(" It's a tie!")

else:
    if total(playerHand) == 21:
        print(
            f"\nYou have {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}")
        print("Blackjack! You win!")
    elif total(dealerHand) == 21:
        print(
            f"\nYou have {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}")
        print("Blackjack! Dealer wins!")
    elif total(playerHand) > 21:
        print(
            f"\nYou have {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}")
        print("You bust! The dealer wins.")
    elif total(dealerHand) > 21:
        print(
            f"\nYou have {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}")
        print("The dealer busts! You win.")
    elif 21 - total(dealerHand) < 21 - total(playerHand):
        print(
            f"\nYou have {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}")
        print("Dealer wins!")
    elif 21 - total(playerHand) < 21 - total(dealerHand):
        print(
            f"\nYou have {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}")
        print("You win!")
