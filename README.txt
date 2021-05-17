This Repository Contains the Instructions for the TicTacToe Bot Battle. 
Note: This Game is slightly modified. We will start with a regular TicTacToe board, but if there is no winner, the board will be change to a 4x4 and then to a 5x5 etc. (Make sure to account for this

When TicTacToe.py is run, it will find the scripts in the players folder and pit them against each other calling their move method. 

Instructions:
You will create a python file for your bot it has the following requirements:
 -it will be named "{YourName+LastInitial}.py"
 -it will implement a method called move described bellow
 -it will only use code that you are liscenced to used
 -you are allowed to use parts of someone else's code, as long as you have permission (Through a liscense or otherwise)
 -You are allowed to use any code in this repository
 
 Implementation:
in your code you will diffine a method named move (something like this)

def move(board: list, mark: int, sideLen: int) -> tuple:
  pass

board: this parameter will be a list containing lists that represent the rows (0 is the top row)
       each list will then contain numbers

       0 means the square is empty
       1 means that there is an X
       2 means that there is an O
       
mark:  this tells you which number you are playing as

sideLen: this tells you how manny rows and columns the Tic-Tac-Toe board has. This number will start at 3 and will 

return value: 
  the function will return a tuple with the move you make in the form (Row, Column)
  
Note: We start from a 3x3 grid and if there is no winner then there is a 4x4 grid, 5x5 grid, ect., ect., (Untill a winner emerges)

Scoring:

Losing: -1 points
Tie/Win: 0 points (Tic Tac Toe is a Zero Sum game)

However, at the end of a round I add point to the people still in to keep the scores positive

Disqualification:

  If any of the following conditions are not met, your program will be diqualified. if your program is disqualified, then if will be pushed out of the round and will not resieve any points. I really hope that this won't cause any problems with scoring
  -The program must be Error Free and not throw any uncaught exceptions
  -A program must always make a legal move.
  -If the program hangs, I may intterupt the execution, and the program will be disqualified
Lisence:
  By submitting the code you are giving me a lisense to use the code in relation to the competition.

  
  FYI: This will be using python 3.9 <---
  In order to submit your code please use this google form:
    https://forms.gle/U53mA48cXDLbATRk7
