import random
from topics import topics, topic_weights

letters = 'ABCDEFGJIJKLMNOPQRSTUVWXYZ'

def random_letters():
    return_letters = [] # defining stuff
    adding = True
    lettersAdded = 0

    while adding:
        letter_choice = letters[random.randint(0, 25)]
        if letter_choice not in return_letters: # adds letter if it doesn't already exist
            return_letters.append(letter_choice)
            lettersAdded += 1
        if lettersAdded == 5: # limits letters added to 5
            adding = False
            
    return return_letters # returns the letters

# Topic info from https://docs.google.com/spreadsheets/d/1gZIRPB9HAy40yGv7lJ9B4XWgIovPfImd1WzFet4s1tA/edit

def random_topics():
    choices = random.choices(topics, weights=topic_weights, k=5)
    return choices

print(random_topics())