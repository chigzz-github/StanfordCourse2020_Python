from karel.stanfordkarel import * 

"""
File: MidpointKarel.py
----------------------
When you finish writing it, MidpointKarel should
leave a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.
"""


def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    put_beeper()
    while front_is_clear():
          move()
    put_beeper()
    turn_around()
    if (front_is_clear()):
        move()
        if (beepers_present()):
            pick_beeper()
            turn_around()
            move()
        else:
              while (no_beepers_present()):
                    move()
              turn_around()
              move()
              put_beeper()

              move()
              if(front_is_blocked()):
                  turn_left()
                  turn_left()
              move()

              while no_beepers_present():
                  move()
                  if (beepers_present()):
                      turn_around()
                      move()
                      put_beeper()
                      move()
                      move()

              turn_around()
              move()
              put_beeper()

              if(front_is_clear()):
                move()
              else:
                  pick_beeper()

              while front_is_clear():
                 pick_beeper()
                 move()
              pick_beeper()
              turn_around()
           
              while no_beepers_present():
                  move()

              move()
            
              while front_is_clear():
                   pick_beeper()
                   move()

              turn_around()
              pick_beeper()
            
              while no_beepers_present():
                  move()
    else:

        pick_beeper()


def turn_around():
    turn_left()
    turn_left()





# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
