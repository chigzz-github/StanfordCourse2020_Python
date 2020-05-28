"""
File: nimm.py
-------------------------
Add your comments here.
"""


def main():
    """
    You should write your code for this program in this function.
    Make sure to delete the 'pass' line before starting to write
    your own code. You should also delete this comment and replace
    it with a better, more descriptive one.
    """
    stones_left = 20
    player_turn = 1
    while stones_left != 0:
        print("There are " + str(stones_left) + " stones left")
        if player_turn == 1:
            stones_left_player = int(
                input("Player " + str(player_turn) + " would you like to remove 1 or 2 stones? "))
            player_turn = player_turn + 1
        else:
            stones_left_player = int(
                input("Player " + str(player_turn) + " would you like to remove 1 or 2 stones? "))
            player_turn = player_turn - 1
        while (stones_left_player < 1) | (stones_left_player > 2):
            stones_left_player = int(input("Please enter 1 or 2: "))
        stones_left = stones_left - stones_left_player
        print("")
        if stones_left == 0:
            print("Player " + str(player_turn) + " wins!")



# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
