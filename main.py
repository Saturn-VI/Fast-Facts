import random
from topics import topics, topic_weights, Topic, topic_set, topics_to_set
from flask import Flask, render_template

letters = 'ABCDEFGJIJKLMNOPQRSTUVWXYZ'

app = Flask(__name__, static_folder='static')

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

def space_balancer(length, word): # formats words below the max length
    if (length - len(word)) % 2 == 1:
        space_left = " " * int((length-len(word))/2+0.5)
        space_right = " " * int((length-len(word))/2-0.5)
    else:
        space_left = " " * int((length-len(word))/2)
        space_right = " " * int((length-len(word))/2)

    return(f"{space_left}{word}{space_right}")

def format(topic_inputs, letter_inputs):
    max_topic_length = 0
    for input in topic_inputs:
        if len(input) > max_topic_length:
            max_topic_length = len(input)
            max_length_topic = input

    topic_inputs.remove(max_length_topic)

    

    topic_row = f"| |{max_length_topic}|{space_balancer(len(max_length_topic), topic_inputs[0])}|{space_balancer(len(max_length_topic), topic_inputs[1])}|{space_balancer(len(max_length_topic), topic_inputs[2])}|{space_balancer(len(max_length_topic), topic_inputs[3])}|"
    row_1 = f"|{letter_inputs[0]}|{' ' * len(max_length_topic)}|{' ' * len(max_length_topic)}|{' ' * len(max_length_topic)}|{' ' * len(max_length_topic)}|{' ' * len(max_length_topic)}|"
    row_2 = f"|{letter_inputs[1]}|{' ' * len(max_length_topic)}|{' ' * len(max_length_topic)}|{' ' * len(max_length_topic)}|{' ' * len(max_length_topic)}|{' ' * len(max_length_topic)}|"
    row_3 = f"|{letter_inputs[2]}|{' ' * len(max_length_topic)}|{' ' * len(max_length_topic)}|{' ' * len(max_length_topic)}|{' ' * len(max_length_topic)}|{' ' * len(max_length_topic)}|"
    row_4 = f"|{letter_inputs[3]}|{' ' * len(max_length_topic)}|{' ' * len(max_length_topic)}|{' ' * len(max_length_topic)}|{' ' * len(max_length_topic)}|{' ' * len(max_length_topic)}|"
    row_5 = f"|{letter_inputs[4]}|{' ' * len(max_length_topic)}|{' ' * len(max_length_topic)}|{' ' * len(max_length_topic)}|{' ' * len(max_length_topic)}|{' ' * len(max_length_topic)}|"

    spacer_row = "=" * len(topic_row)

    return [spacer_row, topic_row, spacer_row, row_1, spacer_row, row_2, spacer_row, row_3 ,spacer_row, row_4, spacer_row, row_5, spacer_row]



for row in format(random_topics(true_random=True), random_letters()):
    print(f"{row}")




# Server stuff

@app.route("/")
def index():
    pass


@app.route("/api", methods=["GET"])
def api():
    pass


app.run(host="127.0.0.1", port="5500")