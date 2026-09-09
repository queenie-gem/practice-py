print("Welcome to Tic Tac Toe!")

def main_game():
    # function to create the board
    def create_board():
        Board = [[" ", " ", " "],
                [" ", " ", " "],
                [" ", " ", " "]]
        return Board

    board = create_board()
    # print(board)


    # Function to display the board
    def display_board(board):
        print("Current Board:")
        print(f' {board[0][0]} | {board[0][1]} | {board[0][2]} ')
        print(" -----------")
        print(f' {board[1][0]} | {board[1][1]} | {board[1][2]} ')
        print(" -----------")
        print(f' {board[2][0]} | {board[2][1]} | {board[2][2]} ')

    # display_board(board)

    # function to get player input
    def get_player_input(board, player):
        move = input(f"Player {player}, enter your move  (1-9): ")

        # check if the input is valid
        if move not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            print("Invalid input. Please enter a number between 1 and 9.")
            return get_player_input(board, player)

        if move == "1" and board[0][0] not in ["X", "O"]:
            board[0][0] = player
        elif move == "2" and board[0][1] not in ["X", "O"]:
            board[0][1] = player
        elif move == "3" and board[0][2] not in ["X", "O"]:
            board[0][2] = player
        elif move == "4" and board[1][0] not in ["X", "O"]:
            board[1][0] = player
        elif move == "5" and board[1][1] not in ["X", "O"]:
            board[1][1] = player
        elif move == "6" and board[1][2] not in ["X", "O"]:
            board[1][2] = player
        elif move == "7" and board[2][0] not in ["X", "O"]:
            board[2][0] = player
        elif move == "8" and board[2][1] not in ["X", "O"]:
            board[2][1] = player
        elif move == "9" and board[2][2] not in ["X", "O"]:
            board[2][2] = player
        else:
            print("Invalid input. Please enter a number between 1 and 9.") 
            return get_player_input(board, player)


    def check_winner(board, player):
        # check rows
        if board[0][0] == player and board[0][1] == player and board[0][2] == player:
            return player
        if board[1][0] == player and board[1][1] == player and board[1][2] == player:
            return player
        if board[2][0] == player and board[2][1] == player and board[2][2] == player:
            return player


        # check columns
        if board[0][0] == player and board[1][0] == player and board[2][0] == player:
            return player   
        if board[0][1] == player and board[1][1] == player and board[2][1] == player:
            return player
        if board[0][2] == player and board[1][2] == player and board[2][2] == player:
            return player

        
        # check diagonals
        if board[0][0] == player and board[1][1] == player and board[2][2] == player:
            return player
        if board[0][2] == player and board[1][1] == player and board[2][0] == player:
            return player


    # check for draw
    def check_draw(board):
        if board[0][0] != " " and board[0][1] != " " and board[0][2] != " " and \
            board[1][0] != " " and board[1][1] != " " and board[1][2] != " " and \
            board[2][0] != " " and board[2][1] != " " and board[2][2] != " ":
            return  "Draw!"
        
    # def reset_board(board):
    #     if check_draw(board) == "Draw!":
    #         board[0][0] = " "
    #         board[0][1] = " "
    #         board[0][2] = " "
    #         board[1][0] = " "
    #         board[1][1] = " "
    #         board[1][2] = " "
    #         board[2][0] = " "
    #         board[2][1] = " "
    #         board[2][2] = " "
            


    display_board(board) 
    player = "X"
    winner = None


    while winner is None:

        # get player input
        get_player_input(board, player)

        # display the board
        display_board(board)

        # check for winner
        winner = check_winner(board, player)

        # check for draw
        if winner is None:
            winner = check_draw(board)

        # switch player
        if player == "X":
            player = "O"
        else:
            player = "X"        

    if check_draw(board) == "Draw!":
        print("It's a draw!")
    else:        
        print(f"Player {winner} wins!")
        

is_playing = True
while is_playing:
    main_game()
    choice = input("Do you want to play again: yes/no: ")

    if (choice != "yes"):
         is_playing = False
         print("Thanks for playing")