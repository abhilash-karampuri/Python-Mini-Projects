#create mine game using python

'''
Note: create a 16blocks land where each block has a possibility of having a gold coin, silver coin or a bomb and two users need to play the game.
You should select any one block for each turn if user get gold coin he get 100 points if user get silver coin he get 50 points. If user get a bomb opponent 
will be winner if user who got bomb will be defeated even if he have high score.'''

import random
game = 1
land=[]
for block in range(1,17):
    land.append(block)
scorep1 = 0
scorep2 = 0

gold_blocks = random.sample(land, 4)
silver_blocks = [block for block in land if block not in gold_blocks]
silver_blocks = random.sample(silver_blocks, 4)
bomb_block = random.choice([block for block in land if block not in gold_blocks + silver_blocks])

while game == 1:
    print("***************************************************")
    p1 = int(input("Player1 Dig a block: "))
    print("***************************************************")
    if p1 in land:
        land.remove(p1)
        print("Remaining Blocks are:", land)
    else:
        print("Block already removed! Try again.")
        continue

    if p1 in gold_blocks:
        print("Player1, You won a Gold coin")
        scorep1 += 100
        print("Player1 Your score is", scorep1)
    elif p1 in silver_blocks:
        print("Player1, You won a Silver coin")
        scorep1 += 50
        print("Player1 Your score is", scorep1)
    elif p1 == bomb_block:
        print("Player1 is defeated and Player 2 wins, Now Player2 can take all gold and silver coins that Player1 is having and score of player2 is", scorep2)
        scorep1 = 0
        scorep2 = 0
        print("It's a tie!")
        break
    else:
        print("Oops! You dig an empty block.")
        print("Player1 Your score is still", scorep1)

    print("***************************************************")
    p2 = int(input("Player2 Dig a block: "))
    print("***************************************************")
    if p2 in land:
        land.remove(p2)
        print("Remaining Blocks are:", land)
    else:
        print("Block already removed! Try again.")
        continue

    if p2 in gold_blocks:
        print("Player2, You won a Gold coin")
        scorep2 += 100
        print("Player2 Your score is", scorep2)
    elif p2 in silver_blocks:
        print("Player2, You won a Silver coin")
        scorep2 += 50
        print("Player2 Your score is", scorep2)
    elif p2 == bomb_block:
        print("Player2 is defeated and Player 1 wins, Now Player1 can take all gold and silver coins that Player2 is having and score of player1 is", scorep1 + scorep2)
        scorep1 = 0
        scorep2 = 0
        break
    else:
        print("Oops! You dig an empty block.")
        print("Player2 Your score is still", scorep2)

    if len(land) == 0:
        print("Game Over! All blocks removed.")
        if scorep1 > scorep2:
            print("Player 1 wins with a score of", scorep1)
        elif scorep2 > scorep1:
            print("Player 2 wins with a score of", scorep2)
        else:
            print("It's a tie!")
        break