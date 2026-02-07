print("games are hard to make")
#this is my code you can probably tell lol ik i could do it better idk how tho

#board
board=[
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]]

""" later implementable
boardsize = input("what size board do you want? ")
if boardsize=="3x3":
    print("3x3 board selected")
    board=[
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]
elif boardsize=="4x4":
    print("4x4 board selected")
    board=[
        [" ", " ", " ", " "],
        [" ", " ", " ", " "],
        [" ", " ", " ", " "],
        [" ", " ", " ", " "]
    ]
elif boardsize=="5x5":
    print("5x5 board selected")
    board=[
        [" ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " "]
    ]
else:
    print("invalid board size, defaulting to 3x3")
    board==[
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]
"""
    

#players 
player1 = input("Is player 1 X or T? ").upper()
player2 = ""
if player1=="X":
    player2="T"
elif player1=="T":
    player2="X"
else:
    print("invalid choice, defaulting to X")
    player1="X"
    player2="T"

print("player 1 is", player1)
print("player 2 is", player2)

#win conditions
def check_win(board):
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True
    # Check columns
    for col in range(len(board[0])):
        if all(board[row][col] == board[0][col] and board[0][col] != " " for row in range(len(board))):
            return True
    # Check diagonals
    if all(board[i][i] == board[0][0] and board[0][0] != " " for i in range(len(board))):
        return True
    if all(board[i][len(board)-1-i] == board[0][len(board)-1] and board[0][len(board)-1] != " " for i in range(len(board))):
        return True
    return False

#game start
game_over = False
while game_over == False:
    board=[
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]
    
    print("Current Board:")
    
    for row in board:
        print("|".join(row))
    
    #player 1 turn
    print("player 1's turn")
    row = int(input("enter row number (starting from 0): "))
    col = int(input("enter column number (starting from 0): "))
    if board[row][col]==" ":
        board[row][col]=player1
    else:
        print("invalid move, try again")
        continue
    if IndexError:
        print("invalid move, try again")
        continue
    #check win
    if check_win(board):
        print("player 1 wins!")
        break

    #player 2 turn
    print("player 2's turn")
    row = int(input("enter row number (starting from 0): "))
    col = int(input("enter column number (starting from 0): "))
    if board[row][col]==" ":
        board[row][col]=player2
    else:
        print("invalid move, try again")
        continue
    if IndexError:
        print("invalid move, try again")
        continue
    #check win
    if check_win(board):
        print("player 2 wins!")
        break


#idk what to put next just yet