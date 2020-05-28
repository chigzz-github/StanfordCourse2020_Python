"""
File: hailstones.py
-------------------
This is a file for the optional Hailstones problem, if
you'd like to try solving it.
"""


def main():
    """
    You should write your code for this program in this function.
    Make sure to delete the 'pass' line before starting to write
    your own code. You should also delete this comment and replace
    it with a better, more descriptive one.
    """
    steps = 0
    final_number = 1
    AddInput = int(input("Enter any positive number: "))

    if AddInput <= 0:
        AddInput = int(input("Enter any positive number: "))

    while AddInput != 1:
        if AddInput % 2 != 0:
            odd_result = int((3 * AddInput) + 1)
            print(str(AddInput) + " is odd, so I make 3n+1: " + str(odd_result))
            steps = steps + 1
            AddInput = odd_result
        else:
            even_result = int(AddInput / 2)
            print(str(AddInput) + " is even, so I take half: " + str(even_result))
            steps = steps + 1
            AddInput = even_result
    print("The process took " + str(steps) + " steps to reach 1")


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
