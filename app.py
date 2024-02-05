from gameFunctions import generateShoe, generatePlayers, startGame, stillPlaying


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
        if stillPlaying() is False:
            break
