# constants
WIN_COMBOS = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
BOARD = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]


def make_board():
    """This function creates the board"""
    print("--- Noughts and Crosses ---")
    print(f'{BOARD[0]:<2}: {BOARD[1]:<2}: {BOARD[2]:>1}')
    print("..........")
    print(f'{BOARD[3]:<2}: {BOARD[4]:<2}: {BOARD[5]:>1}')
    print("..........")
    print(f'{BOARD[6]:<2}: {BOARD[7]:<2}: {BOARD[8]:>1}')


def main():
    # Main menu
    print("*" * 50)
    print("Welcome to our Noughts and Crosses Game!")
    print("*" * 50)
    play_loc_list1 = []
    play_loc_list2 = []
    # Get player's names
    player_1 = input("Enter the name of the first player:\n> ")
    player_2 = input("Enter the name of the second player:\n> ")
    while True:
        turn = 1
        # Player 1 turn
        while turn == 1:
            print("Hi", player_1)
            while True:
                make_board()
                while True:
                    # User input validation loop:
                    loc_x = input("Cross location(choose 1 - 9):\n> ")
                    if not loc_x.isdigit() or int(loc_x) not in range(10):
                        print('>>> Invalid input!')
                        continue
                    else:
                        loc_x = int(loc_x)
                        break  # break User input validation loop:

                # Check if position is empty:
                if BOARD[loc_x - 1] == 'X' or BOARD[loc_x - 1] == 'O':
                    print('>>> Position taken, try again!')
                    continue
                else:
                    BOARD[loc_x - 1] = "X"
                    break  # Break player 1 turn:

            # Check win combos:
            loc_attempt = loc_x - 1
            play_loc_list1.append(loc_attempt)
            play_loc_list1.sort()
            for i in range(0, len(WIN_COMBOS)):
                if WIN_COMBOS[i] == play_loc_list1:
                    print("You have won!")
                    break

        make_board()
        turn = 2
        # Player 2 turn:
        while turn == 2:
            print("Hi", player_2)
            while True:
                make_board()
                while True:
                    # User input validation loop:
                    loc_y = input("Noughts location(choose 1 - 9):\n> ")
                    if not loc_y.isdigit() or int(loc_y) not in range(10):
                        print('>>> Invalid input')
                        continue
                    else:
                        loc_y = int(loc_y)
                        break  # break User input validation loop:

                # Check if position is empty:
                if BOARD[loc_y - 1] == 'X' or BOARD[loc_y - 1] == 'O':
                    print('>>> Position taken, try again!')
                    continue
                else:
                    BOARD[loc_y - 1] = "O"
                    break  # Break player 2 turn:

            # Check win combos:
            loc_attempt = loc_y - 1
            play_loc_list2.append(loc_attempt)
            play_loc_list2.sort()
            for i in range(0, len(WIN_COMBOS)):
                if WIN_COMBOS[i] == play_loc_list2:
                    print("You have won!")
                    break

            make_board()
            turn = 1


if __name__ == '__main__':
    main()
