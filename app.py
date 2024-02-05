from gameFunctions import generateShoe, generatePlayers, startGame


def playGame():
    # Generate random card set
    cardShoe = generateShoe()

    # Create player instances
    playerList = generatePlayers()

    # Start game loop
    startGame(cardShoe, playerList)


if __name__ == "__main__":
    playing = True
    while playing is True:
        playGame()
        while True:
            stillPlaying = input("Play again? (Y/N)")
            if stillPlaying.lower() not in "yn":
                print("Please enter Y or N to continue")
                continue
            else:
                break

        if stillPlaying.lower() == 'n':
            playing = False
