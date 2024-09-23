def checkwin(game):
    for i in range(3):
        if game[i][0] == game[i][1] == game[i][2] != "*": #checks for wins
            return True
        if game[0][i] == game[1][i] == game[2][i] != "*":  #checks for wins
            return True

    if game[0][0] == game[1][1] == game[2][2] != "*":  #checks for wins
        return True
    if game[0][2] == game[1][1] == game[2][0] != "*":  #checks for wins
        return True

    return False

def printboard(game):
    for row in game:
        print(row) #prints game board
    print()

game = [["*", "*", "*"], ["*", "*", "*"], ["*", "*", "*"]]
win = False
player1 = True

print("Game Instructions: Please input 0, 1, or 2 for row followed by 0, 1, or 2 for column. Enter the first player's name:")
x = input()
print("Enter the second player's name:")
y = input()

while not win:
    printboard(game)
    if player1:
        print(x + ", enter row number:")#prompts players to enter game coordinates (row)
    else:
        print("It's your turn, " + y + ". Enter row number:")#prompts players to enter game coordinates (row)
    row = int(input())
    print("Enter column number:")#prompts players to enter game coordinates (col)
    col = int(input())
    if 0 <= row < 3 and 0 <= col < 3:
        if game[row][col] == "*":
            game[row][col] = "X" if player1 else "O" #changes board per user coordinate input
            if checkwin(game):
                printboard(game)
                print("Congratulations " + (x if player1 else y) + ", you win!") #checks for win 
                win = True #Stops loop
            player1 = not player1
        else:
            print("Cell taken.")#message for when cell is taken
    else:
        print("Invalid input, enter numbers between 0 and 2")#message for invalid input

