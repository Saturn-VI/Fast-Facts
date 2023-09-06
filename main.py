import random

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

topics = [
        # General
        "Science",

        # Scientists
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
        "Philosophers",

        # Units/Dimensions
        "Units",
        "Dimensions",
        "Metric Units",
        "Metric Prefixes",
        "SI Units",
        "Time",
        "Eponymous Constants",

        # Laws/Theorems/Theories/Principles
        "Laws/Theorems/Principles",
        "Eponymous Laws/Theorems/Principles",

        # Branches of Science
        "Branches of Science",
        "Ending in -iology",
        "Biology",
        "Medicine",
        "Physics",
        "Science Careers",

        # Other
        "Lab Equipment",
        "Microscope Parts",
        "Scientific Instruments",
        "Measuring Equipment",
        "Scientific Method",
        "Scientific Discoveries",
        "Scientific Inventions",
        "Scioly Events (Past/Present)",
        "Math",
        "Latin Prefixes",
        "Greek Letters",

        #Anatomy
        "Human Anatomy",
        "Human Bones",
        "Human Muscles",
        "Organs",
        "Organ Systems",
        "Parts of Human Eye",
        "Parts of Human Brain",
        "Circulatory System",
        "Digestive System",
        "Respiratory System"

        ]
topic_weights = [

        # General
        1, # Science

        # Scientists
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
        1, # Philosophers

        # Units/Dimensions
        22, # Units
        1, # Dimensions
        1, # Metric Units
        1, # Metric Prefixes
        3, # SI Units
        1, # Time
        1, # Eponymous Constants

        # Laws/Theorems/Theories/Principles
        12, # Laws/Theorems/Principles

        # Branches of Science
        2, # Eponymous Laws/Theorems/Principles
        15, # Branches of science
        2, # Ending in -iology
        1, # Biology
        1, # Medicine
        1, # Physics
        2, # Science Careers
        
        # Other
        8, # Lab Equipment
        6, # Microscope Parts
        9, # Scientific Instruments
        1, # Measuring Equipment
        4, # Scientific Method
        1, # Scientific Discoveries
        1, # Scientific Inventions
        1, # Scioly Events (Past/Present)
        2, # Math
        1, # Latin Prefixes
        1, # Greek Letters

        # Anatomy
        8, # Human Anatomy
        19, # Human Bones
        6, # Human Muscles
        11, # Organs
        3, # Organ Systems
        4, # Parts of the Human Eye
        3, # Parts of the Human Brain
        1, # Circulatory System
        1, # Digestive System
        1 # Respiratory System
        
        ]

def random_topics():
    choices = random.choices(topics, weights=topic_weights, k=5)
    return choices

print(random_topics())