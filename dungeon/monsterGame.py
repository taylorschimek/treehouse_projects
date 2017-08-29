import random
import sys
import os

# draw grid

# pick random location for player
# pick random location for exit
# pick random location for the monster
# draw the player in the grid
# take input for movement
# move player, unless invalid move (past edges of grid)
# check for win/loss
# clear screen and redraw the grid

CELLS = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0),
         (0, 1), (1, 1), (2, 1), (3, 1), (4, 1),
         (0, 2), (1, 2), (2, 2), (3, 2), (4, 2),
         (0, 3), (1, 3), (2, 3), (3, 3), (4, 3),
         (0, 4), (1, 4), (2, 4), (3, 4), (4, 4)]

def getLocations():
    return random.sample(CELLS, 3)

def movePlayer(player, move):
    # get the player's location
    x, y = player
    # if move == LEFT, x-1
    if move == "LEFT":
        x -= 1
    # if move == RIGHT, x+1
    if move == "RIGHT":
        x += 1
    # if move == UP, y-1
    if move == "UP":
        y -= 1
    # if move == DOWN, y+1
    if move == "DOWN":
        y += 1
    return x, y

def getMoves(player):
    moves = ["LEFT", "RIGHT", "UP", "DOWN"]
    # if player's y == 0, they can't move up
    if player[1] == 0:
        del moves[2]
    # if player's y == 4, they can't move down
    if player[1] == 4:
        del moves[3]
    # if player's x == 0, they can't move left
    if player[0] == 0:
        del moves[0]
    # if player's x == 4, they can't move right
    if player[0] == 4:
        del moves[1]
    return moves


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def drawMap(player):
    print(" _"*5)
    tile = "|{}"

    for cell in CELLS:
        x, y = cell
        if x < 4:
            lineEnd = ""
            if cell == player:
                output = tile.format("X")
            else:
                output = tile.format("_")
        else:
            lineEnd = "\n"
            if cell == player:
                output = tile.format("X|")
            else:
                output = tile.format("_|")
        print(output, end=lineEnd)


def main():
    monsterIsAt, doorIsAt, playerIsAt = getLocations()
    playing = True

    while playing:
        clear()
        drawMap(playerIsAt)
        print("You're currently in room {}".format(playerIsAt))
        goodMoves = getMoves(playerIsAt)
        print("You can move {}".format(goodMoves))

        move = input("> ")
        move = move.upper()

        if move == 'QUIT':
            print("\n ** See you next time! ** \n")
            break
            #sys.exit()
        # Good move? Change the player position
        elif move in goodMoves:
            playerIsAt = movePlayer(playerIsAt, move)
            if playerIsAt == doorIsAt:
                print("\n ** You win!!  You found the door!! ** \n")
                playing = False
                #playAgain()
            # On the monster? They lose!
            if playerIsAt == monsterIsAt:
                print("\n ** The monster got you.  You lose! ** \n")
                playing = False
                #playAgain()
        else:
            input("\n ** You can't go that way! **\n")
    else:
        if input("Play again?  [Y/n] ").lower() != "n":
            main()



print("Welcome to the dungon!")
print("Enter QUIT anytime to QUIT")
print("There is a hidden exit and a hidden monster.  Find the exit before you find the monster.")
input("Press ENTER to begin.")
main()
