from shoeClass import Shoe
from cardClass import Card
import settings as CONFIG
from playerClass import Player

import time


ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
suits = ('\u2660', '\u2665', '\u2666', '\u2663')


def generateCards(deckCount=1):
    allCards = []
    for _ in range(deckCount):
        cards = [[Card(suit, value) for value in ranks] for suit in suits]
        flattenedCards = [card for suit in cards for card in suit]
        allCards += flattenedCards

    return allCards


def generateShoe(deckCount=CONFIG.DECK_COUNT):
    cardShoe = Shoe(generateCards(deckCount))

    return cardShoe


def generatePlayers(playerCount=CONFIG.PLAYER_COUNT):
    playerList = []
    while len(playerList) < playerCount - 1:
        playerList.append(Player(f'Player {len(playerList) + 1}'))
    playerList.append(Player('Dealer'))

    return playerList


def startGame(cardShoe, playerList):
    players = playerList[:-1]
    dealer = playerList[-1]
    playingGame = True
    while playingGame is True:
        while len(playerList[-1].cards) < 2:
            for player in playerList:
                player.draw(cardShoe)
                time.sleep(.5)

        for player in players:
            print(f'{player}\nYou have {player.count}.  '
                  f'Dealer shows {dealer.cards[0].number}')
            if player.count == 21:
                print(f'{player.name} has BLACKJACK!\n')
                player.stay = True
                continue

            while player.stay is False and player.busted is False:
                decision = input(CONFIG.INPUT_MSG)

                match decision.lower():
                    case 'd':
                        player.draw(cardShoe)
                        player.stay = True
                        print(f'{player.name} doubled down for...'
                              f'{player.cards[-1].number},  for a total of '
                              f'{player.count}!\n')

                    case 'h':
                        player.draw(cardShoe)
                        print(f'{player}\nYou have {player.count}.  '
                              f'Dealer shows {dealer.cards[0].number}')
                        if player.count > 21:
                            player.busted = True
                            print(f'{player.name} BUSTED!')

                        elif player.count == 21:
                            player.stay = True

                        continue

                    case 's':
                        player.stay = True
                        print(f'{player.name} stays on {player.count}\n')

                    case _:
                        print('\nOnly "S", "D", or "H" are accepted\n')
                        continue

        while dealer.stay is False and dealer.busted is False:
            print(dealer)
            print(f'Dealer has {dealer.count}')
            if dealer.count < 17:
                dealer.draw(cardShoe)

            elif dealer.count == 17:
                if '11' in [str(card.value) for card in dealer.cards]:
                    dealer.draw(cardShoe)

                else:
                    dealer.stay = True

            else:
                dealer.stay = True

            if dealer.count > 21:
                dealer.busted = True
                print(f'{dealer}\n{dealer.name} BUSTED!')

        playingGame = False

    winners = [player for player in players if (
        player.busted is False and player.count > dealer.count) or (
            dealer.busted is True and player.busted is False)]
    pushes = []
    if dealer.busted is not True:
        pushes = [
            f'\t\t{player.name}' for player in players if (
                player.count == dealer.count)]
    # Print list of players who beat dealer
    if len(winners) == 0 and len(pushes) == 0:
        print('Dealer wipded the floor with everyone!')

    else:
        if len(winners) > 0:
            print('Winners:')
            winnerNames = "\n".join(
                [f'\t{player.name}' for player in winners])
            print(winnerNames)
        if len(pushes) > 0:
            print('Pushed:')
            print('\n'.join(pushes))

    # Print finished hand results to verify results
    print()
    print(*playerList, sep="\n")


def stillPlaying():
    while True:
        playing = input("Play again? (Y/N)")
        if playing.lower() not in "yn":
            print("Please enter Y or N to continue")
            continue
        else:
            if playing.lower() == 'n':
                return False
            else:
                return True
