import random

def deal_cards(deck, num_players):
    hands = [[] for _ in range(num_players)]
    for i in range(7):
        for j in range(num_players):
            card = deck.pop()
            hands[j].append(card)
    return hands

def create_deck():
    ranks = [str(i) for i in range(2, 11)] + ['J', 'Q', 'K', 'A']
    suits = ['C', 'D', 'H', 'S']
    deck = [rank + suit for suit in suits for rank in ranks]
    random.shuffle(deck)
    return deck

def print_hand(hand):
    print('Your hand:')
    for card in hand:
        print(card)

def get_card_value(card):
    rank = card[:-1]
    if rank.isdigit():
        return int(rank)
    elif rank == 'A':
        return 14
    elif rank == 'K':
        return 13
    elif rank == 'Q':
        return 12
    elif rank == 'J':
        return 11
    else:
        return 0

def go_fish():
    deck = create_deck()
    num_players = int(input('Enter number of players (2-5): '))
    while num_players < 2 or num_players > 5:
        num_players = int(input('Invalid number of players. Enter a number between 2 and 5: '))
    hands = deal_cards(deck, num_players)
    player_scores = [0] * num_players
    turn = 0
    while any(score < 4 for score in player_scores):
        current_player = turn % num_players
        print('Player', current_player+1, "'s turn")
        print_hand(hands[current_player])
        chosen_rank = input('Choose a rank to ask for: ')
        while chosen_rank not in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']:
            chosen_rank = input('Invalid rank. Choose a rank to ask for: ')
        chosen_rank_cards = [card for card in hands[(current_player+1)%num_players] if card.startswith(chosen_rank)]
        if not chosen_rank_cards:
            print('Go fish!')
            new_card = deck.pop()
            print('You drew', new_card)
            hands[current_player].append(new_card)
            if get_card_value(new_card) == get_card_value(chosen_rank):
                print('Lucky draw! Go again.')
                continue
        else:
            for card in chosen_rank_cards:
                hands[(current_player+1)%num_players].remove(card)
                hands[current_player].append(card)
            print('Player', current_player+1, 'took', len(chosen_rank_cards), chosen_rank+'s')
            player_scores[current_player] += len(chosen_rank_cards)
        turn += 1
    print('Game over!')
    for i, score in enumerate(player_scores):
        print('Player', i+1, 'scored', score, 'points.')
    winners = [i+1 for i, score in enumerate(player_scores) if score == max(player_scores)]
    if len(winners) == 1:
        print('Player', winners[0], 'wins!')
    else:
        print('Players', ', '.join(map(str, winners)), 'tie!')


go_fish()