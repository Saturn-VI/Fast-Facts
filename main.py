import random
from topics import topics, topic_weights, Topic, topic_set, topics_to_set

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

def random_topics(true_random=False):
    if true_random:
        choices = random.sample(topics, 5)
    else:
        # time to steal the random_letter logic
        choices = []
        choosing = True
        words_chosen = 0
        while choosing:
            temp_word_choice = random.choices(topics, weights=topic_weights, k=5)
            if temp_word_choice not in choices:
                choices.append(temp_word_choice)
                words_chosen += 1
            if words_chosen == 5:
                choosing = False
    return choices


def format(topic_inputs, letter_inputs):
    max_topic_length = 0
    for input in topic_inputs:
        if len(input) > max_topic_length:
            max_topic_length = len(input)
            max_length_topic = input

    topic_inputs.remove(max_length_topic)

    def space_balancer(length, word):
        if (length - word) % 2 == 1:
            is_odd = True

    row_1 = f"|{max_length_topic}|{}"




print(random_topics(true_random=True))
print(random_letters())