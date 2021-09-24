def main_tic_tac_toe():
    def instructions():
        print(""" WELCOME TO THE


 _   _   _             _   _    _             _    _    __
/_  \ / \ /   /           /   \ /  _  \  /  _/           /   \  /  _  \  /   _\  
   / \     | | |  /       _       / \     |  _  | |  /        _      / \     |  /   \  | |   \     
   | |     | | |  \__    \_\     | |     | |  | | |  \_    \_\     | |     |  \/  | |   /_
   \_/     \_/ \_\               \/     \/  \/  \_\               \/      \/   \_\


    GAME CODED BY: ERUDITE					 
    THIS WILL BE A BATTLE BETWEEN A HUMAN MIND AND AN ARTIFICIAL INTELLIGENCE(COMPUTER)	

    INSTRUCTIONS:
	1: YOU CAN MAKE YOUR MOVE BY ENTERING A NUMBER IN BETWEEN 0-8. 
	2: THE NUMBER WILL CORRESPOND TO THE BOARD POSITION AS ILLUSTRATED.


                    0 | 1 | 2
                    ---------
                    3 | 4 | 5
                    ---------
                    6 | 7 | 8

	3: CONDITION OF WINNING THE GAME:
	   WINNER WILL BE DECIDED ON THE BASIS OF WHOEVER SO FIRST FILL THEIR RESPECTIVE SIGN ON THE BOARD'S POSITION
	   THREE CONSECUTIVE IN ROW OR COLUMN OR EITHER IN DIAGONAL.
	4: PLAY YOUR WITH YOUR BEST MOVES.


    """)

    # instructions()

    ttt_Board = [0, 1, 2, 3, 4, 5, 6, 7, 8]  # Creating Dummy Board

    def display_board(ttt_Board):  # Display board function definition
        print(" __")
        print("||", ttt_Board[0], "||", ttt_Board[1], "||", ttt_Board[2])
        print(" __")
        print("||", ttt_Board[3], "||", ttt_Board[4], "||", ttt_Board[5])
        print(" __")
        print("||", ttt_Board[6], "||", ttt_Board[7], "||", ttt_Board[8])
        print(" __")

        # display_board(ttt_Board)

    # Chance given to Player to enter the choice
    def choose_player(ttt_Board):
        valid_move = False
        while (not valid_move):
            choice = int(input("PLAYER: PLEASE SELECT YOUR CHOICE TO MAKE A MOVE ON THE BOARD: \n >> "))
            if (choice < 0 or choice > 8):
                print("please select in b/w 0-8 ")
                continue

            if (ttt_Board[choice] != "X" and ttt_Board[choice] != "O"):

                if (b == "Y"):
                    ttt_Board[choice] = "X"
                else:
                    ttt_Board[choice] = "0"

                valid_move = True
            else:
                print("SORRY THE POSTION IS ALREADY OCCUPIED BY :,", ttt_Board[choice])

        return win_direction(ttt_Board)

    # Chance given to Computer to enter the choice
    import random
    def choose_computer(ttt_board):
        valid_move = False
        while (not valid_move):
            random.seed()
            choice = random.randint(0, 8)
            if (ttt_Board[choice] != "X" and ttt_Board[choice] != "O"):
                if (b == "Y"):
                    ttt_Board[choice] = "0"
                else:
                    ttt_Board[choice] = "X"
                print("COMPUTER MADE THE MOVE")
                valid_move = True

        return win_direction(ttt_Board)

    # Deciding the Vertical Winning Conditions
    def win_vertical(ttt_board):
        winner = False
        if (ttt_Board[0] == ttt_Board[3] == ttt_Board[6]):
            winner = True
        elif (ttt_Board[1] == ttt_Board[4] == ttt_Board[7]):
            winner = True
        elif (ttt_Board[2] == ttt_Board[5] == ttt_Board[8]):
            winner = True

        return winner

    # Deciding the Horizontal Winning Conditions
    def win_horizontal(ttt_board):
        winner = False
        if (ttt_Board[0] == ttt_Board[1] == ttt_Board[2]):
            winner = True
        elif (ttt_Board[3] == ttt_Board[4] == ttt_Board[5]):
            winner = True
        elif (ttt_Board[6] == ttt_Board[7] == ttt_Board[8]):
            winner = True

        return winner

    # Deciding the Diagonal Winning Conditions
    def win_diagonal(ttt_board):
        winner = False
        if (ttt_Board[0] == ttt_Board[4] == ttt_Board[8]):
            winner = True
        elif (ttt_Board[2] == ttt_Board[4] == ttt_Board[6]):
            winner = True

        return winner

    # Which Direction you won the game
    def win_direction(ttt_board):
        game_winner = False
        if (win_vertical(ttt_board) == True):
            game_winner = True
        elif (win_horizontal(ttt_board) == True):
            game_winner = True
        elif (win_diagonal(ttt_board) == True):
            game_winner = True

        return game_winner

    # DECISION MAKING ON WHO SHOULD START THE GAME
    start = input("DO YOU LIKE START THE GAME HERE: (Y/N) \n>> ")
    if start == "Y":
        print("GREAT YOU ARE THE ONE WHO IS GOING TO GO FIRST:  ")
    elif start == "N":
        print("AS YOU DECIDED TO NOT START FIRST, GIVING COMPUTER THE FIRST MOVE:  ")

    # DECIDE THE ALTERNATE CHANCES
    turn = 0
    won = False
    while (not won and turn < 9):
        if start == "Y":
            if turn % 2 == 0:
                won = choose_player(ttt_Board)
            else:
                won = choose_computer(ttt_Board)

            turn = turn + 1
            display_board(ttt_Board)

        if start == "N":
            if turn % 2 == 0:
                won = choose_computer(ttt_Board)
            else:
                won = choose_player(ttt_Board)

            turn = turn + 1
            display_board(ttt_Board)

    print(turn)
    turn = turn - 1
    C = input("want to continue:(Y/N) \n ")
    if (not won):
        print("HELLO IT IS A TIE!!!")
    if start == "Y":
        if turn % 2 == 0 and (won):
            print("CONGRATULATIONS !!!! YOU WON THE GAME")
            # if(C=="Y"):
            #     main_tic_tac_toe()
            # else:
            #     return
    elif won:
        print("COMPUTER AGAIN DID IT, AND WON THE GAME")
        if (C == "Y"):
            main_tic_tac_toe()

    if start == "N":
        if turn % 2 == 0 and (won):
            print("COMPUTER AGAIN DID IT, AND WON THE GAME")
            if (C == "Y"):
                main_tic_tac_toe()

        elif won:
            print("CONGRATULATIONS !!!! YOU WON THE GAME")
            if (C == "Y"):
                main_tic_tac_toe()
            else:
                print("thank you")


b = input("please type yes if you lice char X:(Y/N) \n ")
main_tic_tac_toe()