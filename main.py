from random import randint

letters = 'ABCDEFGJIJKLMNOPQRSTUVWXYZ'

def random_letters():
    return_letters = [] # defining stuff
    adding = True
    lettersAdded = 0

    while adding:
        letter_choice = letters[randint(0, 25)]
        if letter_choice not in return_letters: # adds letter if it doesn't already exist
            return_letters.append(letter_choice)
            lettersAdded += 1
        if lettersAdded == 5: # limits letters added to 5
            adding = False
            
    return return_letters # returns the letters

# Topic info from https://docs.google.com/spreadsheets/d/1gZIRPB9HAy40yGv7lJ9B4XWgIovPfImd1WzFet4s1tA/edit

topics = [
        "Science",
        "Scientists",
        "Female Scientists",
        "16th-19th Century Scientists",
        "Astronomers",
        "Astronauts",
        "NASA Astronauts",
        "Biologists",
        "Chemists",
        "Physicists",
        "Nobel Laureates",
        "Aviators",
        "Inventors",
        "Philosophers"
        ]
topic_weights = [
        1, # Science
        29, # Scientists
        4, # Female Scientists
        1, # 16th-19th Century Scientists
        1, # Astronomers
        1, # Astronauts
        1, # NASA Astronauts
        1, # Biologists
        4, # Chemists
        5, # Physicists
        3, # Nobel Laureates
        1, # Aviators
        1, # Inventors
        1 # Philosophers
        ]

def random_topics():
    random.choices(topics, weights=topic_weights, k=5)