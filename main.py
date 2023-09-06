from random import randint

letters = 'ABCDEFGJIJKLMNOPQRSTUVWXYZ'

def random_letters():
    return_letters = []
    adding = True
    lettersAdded = 0
    while adding:
        letter_choice = letters[randint(0, 25)]
        if letter_choice not in return_letters: # adds letter if it doesn't already exist
            return_letters.append(letter_choice)
            lettersAdded += 1
        if lettersAdded == 5: # limits letters added to 5
            adding = False
            
    return return_letters

