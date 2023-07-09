import random
import time

VALUES = {'A': 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 'T': 10, 'J': 10, 'Q': 10, 'K': 10}
deck = []
dealer_cards = []
player_cards = []
hide = True

def print_intro():
    print('\n\n\n*** LET\'S PLAY BLACKJACK ***\n\n\n')
    time.sleep(3)
    print('\n\n\n*** Press Enter To Continue ***\n\n\n')
    input()
# 
def enough_cards_in(deck):
    if len(deck) > 20:
        return True
    
def shuffle(deck, num_of_decks = 3):
    deck.clear()
    for i in range(4 * num_of_decks):
        for card in VALUES.keys():
            deck.append(card) 
    random.shuffle(deck)
    print('\n\n\n   SHUFFLING DECK...\n\n\n')
    time.sleep(2)  

def deal(cards):
    card = deck[0]
    deck.remove(card)
    cards.append(card)

def card_sum(cards):
    sum = 0
    for card in cards:
        sum += VALUES[card]
    if sum < 12 and 'A' in cards:
        sum += 10
    return sum

def print_cards(hide_card=False):
    print('\n\n\n')
    if hide_card == True:
        print(f'Dealer has [?] [{dealer_cards[1]}]')
        if dealer_cards[1] == 'A':
            print('    Dealer Total is: 11')
        else:
            print(f'    Dealer Total is: {VALUES[dealer_cards[1]]}')
        print('Player has', end='')
        for card in player_cards:
            print(' [' + str(card) + ']', end='')
        print(f'\n    Player Total is: {card_sum(player_cards)}')
    else:
        print('Dealer has', end='')
        for card in dealer_cards:
            print(f' [{card}]', end='')
        print(f'\n    Dealer Total is: {card_sum(dealer_cards)}')
        print('Player has', end='')
        for card in player_cards:
            print(f' [{card}]', end='')
        print(f'\n    Player Total is: {card_sum(player_cards)}')  

def check_blackjack(cards):
    if ('A' in cards) and (card_sum(cards) == 21):
        return True
    else:
        return False
    
def bust(cards):
    return card_sum(cards) > 21

def initial_deal():
    while True:
        if not enough_cards_in(deck):
            shuffle(deck)
        dealer_cards.clear()
        player_cards.clear()
        deal(player_cards)
        deal(dealer_cards)
        deal(player_cards)
        deal(dealer_cards)
        if check_blackjack(player_cards) and check_blackjack(dealer_cards):
            print('\n\n\n*** DEALER & PLAYER BLACKJACK ***\n\n\n')
            time.sleep(2)
            print('\n\n\n*** TIE ***')
        elif check_blackjack(dealer_cards):
            print_cards(hide)
            time.sleep(2)
            print_cards()
            time.sleep(2)
            print('\n\n\n*** DEALER BLACKJACK ***\n\n\n')
            time.sleep(2)
            print('\n\n\n*** YOU LOSE ***\n\n\n')
            time.sleep(2)
            continue
        elif check_blackjack(player_cards):
            print_cards(hide)
            time.sleep(2)
            print('\n\n\n*** PLAYER BLACKJACK ***\n\n\n')
            time.sleep(2)
            print('\n\n\n*** YOU WIN ***\n\n\n')
            time.sleep(2)
            continue
        
        else:
            break

def player_hit():
    while True:
        print_cards(hide)
        if bust(player_cards):
            time.sleep(2)
            break
        elif card_sum(player_cards) == 21:
            time.sleep(2)
            break
        ans = input('(H)IT  or  (S)TAND: ')
        if ans.lower() == 's':
            break
        elif ans.lower() == 'h':
            deal(player_cards)
            continue
        else:
            print('\n\n\nIncorrect Input\n\n\n')
            time.sleep(2)
            continue

def dealer_hit():
    cards = dealer_cards
    if not bust(player_cards):
        print_cards()   
        time.sleep(2)
        while not bust(cards):
            while card_sum(cards) < 17  or (card_sum(cards) == 17 and 'A' in cards):
                if card_sum(cards) != 21:
                    deal(cards)
                    print_cards()
                    time.sleep(2)
                else:
                    break
            break    

def determine_winner():
    if bust(player_cards):
        print('\n\n\n*** PLAYER BUST ***\n\n\n')
        time.sleep(2)
        print('\n\n\n*** YOU LOSE ***\n\n\n')
        time.sleep(2)
    elif bust(dealer_cards):
        print('\n\n\n*** DEALER BUST ***\n\n\n')
        time.sleep(2)
        print('\n\n\n*** YOU WIN ***\n\n\n')
        time.sleep(2)
    else:
        print('\n\n*** DEALER TOTAL: ' + str(card_sum(dealer_cards)) + ' ***\n')
        print('*** PLAYER TOTAL: ' + str(card_sum(player_cards)) + ' ***\n\n')
        time.sleep(2)
        if card_sum(dealer_cards) > card_sum(player_cards):
            print('\n\n\n*** YOU LOSE ***\n\n\n')
            time.sleep(2)
        elif card_sum(dealer_cards) < card_sum(player_cards):
            print('\n\n\n*** YOU WIN ***\n\n\n')
            time.sleep(2)
        elif card_sum(dealer_cards) == card_sum(player_cards):
            print('\n\n\n*** IT\'S A TIE ***\n\n\n')
            time.sleep(2)
            
def main():
    print_intro()
    while True:
        initial_deal()
        player_hit()
        dealer_hit()
        determine_winner()

main()










        
    
  


    





