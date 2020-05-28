from karel.stanfordkarel import *


"""
File: TripleKarel.py
--------------------
When you finish writing this file, TripleKarel should be
able to paint the exterior of three buildings in a given
world, as described in the Assignment 1 handout. You
should make sure that your program works for all of the 
Triple sample worlds supplied in the starter folder.
"""


def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.

 """

    while left_is_blocked():
           put_beeper()
           move()
    turn_left()
    move()
    while left_is_blocked():
        put_beeper()
        move()
    turn_left()
    move()
    left_blocked_karel()
    turn_right()
    while left_is_blocked():
        put_beeper()
        move()
    turn_left()
    move()
    while left_is_blocked():
        put_beeper()
        move()
    turn_left()
    move()
    left_blocked_karel()
    turn_right()
    while left_is_blocked():
        put_beeper()
        move()
    turn_left()
    move()
    while left_is_blocked():
        put_beeper()
        move()
    turn_left()
    move()
    left_blocked_karel()



def turn_right():
    turn_left()
    turn_left()
    turn_left()

def left_blocked_karel():
    while left_is_blocked():
           put_beeper()
           move()

def turn_left_karel_left_blocked():
    left_blocked_karel()
    turn_left()

# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
