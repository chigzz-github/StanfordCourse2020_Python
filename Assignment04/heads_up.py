import random

# the name of the file to read in!
FILE_NAME = 'cswords.txt'

def main():

    # import the cswords.txt file, which is variable FILE_NAME as a list - function?

    # words is a list of words in the file
    words = load_data()

    # print out every word in the list
    while True:
        input('Press enter for next word: ')
        print(" ")
        # get a random word - function?
        next_word = get_random_word(words)

        # print out one random word every time we press enter
        print(next_word)


def get_random_word(words):
    random_word = random.choice(words)
    return random_word

def load_data():
    words = []

    file = open(FILE_NAME)
    for line in file:
        words.append(line.strip())
    return words

if __name__ == '__main__':
    main()