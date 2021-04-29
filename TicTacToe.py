"""
Notes:
The working directory will be script's directory, wherever it is run from
Does not import

"""
#no importing 
if __name__ != "__main__":
    import sys
    sys.exit("This file is not meant to be imported, please stop")    

#imports
import os
import importlib

#this function changes the working directory to the script directory
def scriptDir():
    path = __file__
    
    while path[-1] != "\\" and path[-1] != "/":
        
        path = path[:-1]
        if path == "":
            return
    os.chdir(path)
scriptDir()
#ok, I should move my function invokations to the bottom
dir_path = os.getcwd()


#Whenever a player is removed automaticly.
#however if player is not created yet, put in none and just raise it
class playerFailed(Exception):
        

    def __init__(self, player, anounce=False, innnerException= None):
            self.player = player

            if(anounce):
                try:
                    print(player.path + " raised an error, and has been disqualified!")
                except AttributeError:
                    print("something happened, and somone is in trouble.")
            if innnerException != None and (hasattr(innnerException, 'args')):
                
                print("the exception was:\n" + str(innnerException.args))
            if player != None:
                players.remove(player)
            super()

class player:

    @staticmethod
    def fromStrArr(arr: list):
        newArr = []
        for s in arr:
            if s[0] == "_":
                continue
            print(s)
            
            try:
                newArr.append(player(s))
            except playerFailed:

                continue
        return newArr
    def __init__(self, path:str):
        self.path = path 
        self.score = 0
        
        assert type(path) == str
        
        try:
            if(self.path[-3:] == ".py"):
                self.module = importlib.import_module( ("Players." + self.path)[:-3])
        except BaseException as e:
            self.module = None
            raise playerFailed(None, anounce=True, innnerException=e)
    def __str__(self):
        return self.path

def getWaysToWin(n: int) -> list:
    #a tic tac toe board must be at least 3 squares
    assert n >= 3
    ways = []
    for a in range(n):
        horizantal = []
        vertical = []
        for b in range(n):
            horizantal.append((b,a))
            vertical.append((a,b))
        ways.append(horizantal)
        ways.append(vertical)
    diagonal = []
    backDiagonal = []
    for i in range(n):
        diagonal.append((i,i))
        backDiagonal.append((i, n-i-1))
    ways.append(diagonal)
    ways.append(backDiagonal)
    
    return ways
def roundRobin(l: list ) -> list:
    a = 0
    b = 0
    matches = []
    while a < len(l):
        b = a + 1
        
        while b < len(l) :
            matches.append((l[a], l[b]))
            matches.append((l[b], l[a]))
            b += 1
        a += 1
    return matches

def makeBoard(n: int) -> list:
    board = []
    for a in range(n):
        row = []
        for col in range(n):
            row.append(0)
        board.append(row)
    return board
def match(player1: player, player2: player, n: int):
    def isLegalMove(board, move, mark, marks):
        try:
            if board[move[0]][move[1]] != 0:
                return False
        except IndexError:
            return False
        if not mark in marks:
            return False
        
        
        return True
    
    board = makeBoard(n)
    waysToWin = getWaysToWin(n)
    nextPlayer = {
        player1: (player2, 2),
        player2: (player1, 1)
    }
    activePlayer = player1
    
    while 0 in sum(board, []):
        if(activePlayer == player1):
            mark = 1
        else:
            mark = 2
        try:    
            nextMove = activePlayer.module.move(list(board), mark, n)
            
        except SystemExit:
            print("Somone tried to use Os.exit() this is a No-no")
        except Exception as e:
            raise playerFailed(activePlayer, anounce=True, innnerException=e)
        except BaseException as e:
            print("Ok, somone was trying to mess this up. Who did this?")
            raise playerFailed(activePlayer, anounce=True, innnerException=e)  
            
        if isLegalMove(board,nextMove, mark, marks):
            board[nextMove[0]][nextMove[1]] = mark
        else:
            if activePlayer is player1:
                print(f"{player2.path} Won a game because {player1.path} made an Illegal Move!")
                return False
            elif activePlayer is player2:
                print(f"{player1.path} Won a game because {player2.path} made an Illegal Move!")
                return True
        for way in waysToWin:
            won = True
            for pos in way:
                if board[pos[0]][pos[1]] != mark:
                    won = False
            if won:
                printBoard(board)
                if activePlayer is player1:
                    return True
                elif activePlayer is player2:
                    return False
        activePlayer = nextPlayer[activePlayer][0]
    printBoard(board)
    

    return None
def play(n, currentPlayers = None):
    global players
    
    
    if currentPlayers == None:
        currentPlayers = players
    minScore = min(currentPlayers,key=lambda x: x.score).score
    if minScore < 1:
        minScore = 1
    ways = getWaysToWin(n)
    matches = roundRobin( currentPlayers )
    for player1, player2 in matches:
        try:
            result = match(player1, player2, n)
            
        except playerFailed as e:
            return play(n, currentPlayers)
        def increment(x):
            x.score += 1
        if(result == True):
            player2.score -= 1
        elif(result == False):
            player1.score -= 1
    
    players = sorted(players,key=lambda y: -y.score)
    while min(currentPlayers, key=lambda x: x.score).score < minScore:
        for p in players:
            p.score += 1
    print(f"After round #{n-2} the players scores are:")
    for player in players:
        print(f"  {player.path}: {player.score}")
    highestScore = max(players, key=lambda X: X.score).score
    nextPlayers = []
    for p in currentPlayers:
        if p.score == highestScore:
            nextPlayers.append(p)
    if len(nextPlayers) != 1:
        return play(n + 1, nextPlayers)
    else:
        message = f"The final ScoreBoard Was:"
        print(message)
    longestName = len(max(players, key= lambda Y: len(Y.path)).path)

    for index, p in enumerate(players):
        print(f"  {index}.  { p.path.rjust(longestName, ' ')}: {p.score}")

def printBoard(board):
    #makes a 1d board
    assert len(board) > 1
    
    #Ok, I'm a math nerd
    line = "-" * (4 * len(board) -1) + "\n"
    boardAsText = []
    for a,row in enumerate(board):
        numberRow = ""
        for b, col in enumerate(row):
            numberRow += f" {marks[col]} |"
        numberRow = numberRow[:-1] + "\n"
        boardAsText.append(numberRow)
    print(line.join(boardAsText))



#variable declarations
 

message = """
 1 | 2 | 3
-----------
 4 | 5 | 6
-----------
 7 | 8 | 9 
"""

"""
f(2) = 7 = 8 - 1
f(3) = 11 = 12 - 1
f(4) = 15 = 16 - 1
f(x) = 4 * (x) - 1 domain: {x > 1}
 1 
 1 | 2
-------
 3 | 4
 1 | 2 | 3 | 4
---------------
 5 | 6 | 7 | 8 | 9
 ------------------

"""
marks = {
    1:"X",
    2:"O",
    0:" ",
    "X": 1,
    "O": 2,
    " ": 0
}
"""
test things, eliminated later
print(roundRobin(["a",'b','c','d']))

print(getWaysToWin(3))
printBoard([
    [2,2,2],
    [2,1,1],
    [1,1,1]])
print("the cells are numbered like this: \n", message)
"""
players = os.listdir("./Players")


players = player.fromStrArr(players)

play(3)



print("this program has gone to the end!")

