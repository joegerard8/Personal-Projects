#Joseph Gerard
#OIT Programming Challenge
#This program is a game of TicTacToe where the user plays against the computer. The computer makes its decisions randomly. 

#library necessary for the computers decision making
import random 

#creating the dictionary that serves as the framework for the displayed board
boardDictionary = {
    "1" : "-",
    "2" : "-",
    "3" : "-",
    "4" : "-",
    "5" : "-",
    "6" : "-",
    "7" : "-",
    "8" : "-",
    "9" : "-"
}

#list of user decisions which is used to check if the user wins the game or not. 
userDecisions = []
#list of computer decisions which is used to check if the computer won the game or not
computerDecisions = []
# a list of possible computer interactions that make the computer feel more real. 
computerInteractions = [("I think I'll go here."), ("Hmm. I'll try this."), ("Let's see, I wonder if this will work.")]
#an example board that shows which number the user should input for each square on the tic tac toe box
exampleBoard = "1 2 3\n4 5 6\n7 8 9"
#list of all possible win combinations
listOfWins = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]

#prints out the board with the proper X's, O's or dashes depending on the point at which the game is at
def display_board():
    print(f"{boardDictionary['1']} {boardDictionary['2']} {boardDictionary['3']} \n{boardDictionary['4']} {boardDictionary['5']} {boardDictionary['6']}\n{boardDictionary['7']} {boardDictionary['8']} {boardDictionary['9']}")

#function that checks if a player has won. 
def check_winner():
    #checks each item in the list of wins, goes through each number in the user has choosen and checks if there is a winning match
    for item in listOfWins:
        if all(pos in userDecisions for pos in item):
            print("\nYou won! Well done!")
            return True
        # checks each item in the list of winning combinations, goes through the numbers the computer has choosen to see if there is a winning match. 
        elif all(pos in computerDecisions for pos in item):
            print("\nYou lost! Better luck next time!")
            return True
        # if there is no winning combination and the the board is full, returns that the game was a tie. 
    if len(userDecisions) + len(computerDecisions) == 9:
        print("\nIt was a tie! Cat's scratch!")
        return True
    return False

#function that determines what happens on the users turn
def user_turn():
    print("\n")
    display_board()
    decision = str(input("\nEnter the number where you would like to place your X: ")) #asks the user where they want to place their mark. 
    while decision not in boardDictionary.keys(): #checks if the input is a possible input. 
        print("Invalid input, please enter a proper number.")
        decision = str(input("\nEnter the number where you would like to place your X: "))

    if boardDictionary[decision] != "X" and boardDictionary[decision] != "O": #if the input is valid, it adds an x in the corresponding spot, then adds the number to be checked against winning combinations
        boardDictionary[decision] = "X"
        userDecisions.append(int(decision))
    else:
        while boardDictionary[decision] == "X" or boardDictionary[decision] == "O": #checks if the spot has already been filled, if so gives the user another chance. 
            print("This spot is already filled, please try another spot.")
            decision = str(input("Enter the number where you would like to place your X: "))
        boardDictionary[decision] = "X"
        userDecisions.append(int(decision))

def computer_turn(): #function that determines what happens on the computers turn
    decision = str(random.randrange(1, 10)) #chooses a random number between 1 and 9 for the computers turn
    while boardDictionary[decision] == "X" or boardDictionary[decision] == "O": # if the choosen number is unavailable, the computer trys again until it gets an available number
        decision = str(random.randrange(1, 10))
    boardDictionary[decision] = "O" #places the O wherever the computer ends up, and adds their number to their list of decisions made
    computerDecisions.append(int(decision))
    print(f"\n{random.choice(computerInteractions)}")

#function that determines which player goes first.
def who_first():
    first = input("Would you like to go first? Y/N: ").upper() #allows the user to choose if they will go first or not 
    while first != "Y" and first != "N" :
        print("Invalid input. Try again.")
        first = input("Would you like to go first? Y/N: ").upper()
    if first == "Y":
        return 1
    elif first == "N":
        return 2

#initiates the code, asks if the user wants to play. 
play = input("Do you want to play Tic Tac Toe? Y/N: ").upper()

#logic for the game, as long as the user wants to play, it will continue this logic. 
while play == "Y":
    oneOrTwo = who_first() #runs the who first function
    #prints the example board for the players reference
    print("The board is numbered as followed. When prompted, enter the number where you would like to place your mark.")
    print(exampleBoard)
    #logic for if the player wants to go first, does their turn first then the computer
    if oneOrTwo == 1:
        while not check_winner():
            user_turn()
            if check_winner():
                break
            computer_turn()
    # logic if the user wants to go second, computer goes first, then the user goes. 
    elif oneOrTwo == 2:
        while not check_winner():
            computer_turn()
            if check_winner():
                break
            user_turn()
    # once the game has ended, asks if the user wants to play again. 
    play = input("Do you want to play again? Y/N: ").upper()
    # if the user wants to play again, it clears all of theirs and the computers decisions, and resets the dictionary. 
    if play.upper() == "Y" :
        userDecisions.clear()
        computerDecisions.clear()
        boardDictionary = {
    "1" : "-",
    "2" : "-",
    "3" : "-",
    "4" : "-",
    "5" : "-",
    "6" : "-",
    "7" : "-",
    "8" : "-",
    "9" : "-"
}
# if the user enters N, the program ends. 
if play == "N":
    print("Exiting the program. Goodbye!")