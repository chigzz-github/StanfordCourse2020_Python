"""
File: khansole_academy.py
-------------------------
Add your comments here.
"""

import random


def main():
    """
    You should write your code for this program in this function.
    Make sure to delete the 'pass' line before starting to write
    your own code. You should also delete this comment and replace
    it with a better, more descriptive one.
    """
    MIN_RANDOM = 10
    MAX_RANDOM = 99
    correct = 0
    while correct != 3:
        NUM_RANDOM1 = random.randint(MIN_RANDOM, MAX_RANDOM)
        NUM_RANDOM2 = random.randint(MIN_RANDOM, MAX_RANDOM)
        print("What is " + str(NUM_RANDOM1) + "+" + str(NUM_RANDOM2))
        addition = NUM_RANDOM1 + NUM_RANDOM2
        AddInput = int(input("Your Answer: "))
        correct = correct + 1
        if addition == AddInput:
            print("Correct!. You have got " + str(correct) + " right answer")
        else:
            correct = 0
            print("Incorrect. The expected answer is: " + str(addition))
    if correct == 3:
        print("Congratulations! You mastered addition.")



# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
