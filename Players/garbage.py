import random

def move(board: list, mark:int, sideLen: int) -> tuple:
    
    for a in range(len(board)):
        for b in range(len(board)):
            board[a][b] = random.randint(0,9)
    return (random.randint(0,9), random.randint(0,9))