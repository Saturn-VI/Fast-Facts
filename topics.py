
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
        "Respiratory System",

        # Cells/Genetics
        "Cells",
        "Genetics",
        "Cell Structures",
        "Cell Structures in Plant Cells",
        "Cell Structures in Animal Cells",
        "Cell Structures in Eukaryotic Cells",
        "Types of Cells in Human Body",
        "Cell Division",
        "DNA",
        "Nucleotides",
        "Heredity",

        # Biochemistry
        "Enzymes",
        "Hormones",
        "Neurotransmitters",
        "Amino Acids",

        # Names
        #this will be fun!!!
        "Animals",
        "Bacteria",
        "Pathogens",
        "Viruses",
        "Protists",
        "Trees",
        "Deciduous",
        "North American Trees",
        "Reptiles",
        "Reptile Orders",
        "Dinosaurs",
        "North American Dinosaurs",
        "Amphibians",
        "Amphibian Orders",
        "Plants",
        "Plant Phyla",
        "Flowers",
        "Flowering Plants",
        "Edible Herbs",
        "Submerged Aquatic Vegitation",
        "Birds",
        "Birds of Prey",
        "State Birds",
        "Insects",
        "Insect Anatomy",
        "Spiders",
        "Mammals",
        "Marsupials",
        "Marine",
        "Whales",
        "Primates",
        "Dog Breeds",
        "African Mammals",
        "North American Mammals",
        "Michigan Mammals",
        "Fish",
        "Fungi",
        "Mushrooms",
        "Fruit",
        "Stone Fruit",
        "Vegetables",
        "Root Vegitables",
        "Invasive Species",
        "Invasive Species of Michigan",
        "Aquatic Plants",
        "Poisonous or Venomous Animals",
        "Vertebrates",
        "Land Vertebrates",
        "Invertebrates",
        "Endagered Species",
        "Unicellular Organisms",
        "Animals with Antlers",
        "Domesticated Animals",
        "Prehistoric Aquatic Animals",
        "Coral",
        "Aquatic",
        "Nocturnal Animals",
        "Exctinct Animals",
        "Marine Animals",

        # Taxonomy
        "Taxonomy",

        # Evolution
        "Evolution",

        # Ecology
        "Ecology",
        "Biomes",
        "Terrrestrial Biomes",
        "Ecosystems",
        "Abiotic Factors",
        "Biogeochemical Cycles",
        "Water Cycle",
        "Soil Types",
        "Pollution",
        "Population Factors in Size",
        "Symbiotic Relationships",
        "Food Webs",
        "Trophic Levels",

        # Botany
        "Botany",
        "Plant Parts",
        "Parts of Flowers",

        # Epidemiology
        "Epidemiology",
        "Diseases/Disorders",
        "Human Diseases",
        "Infectious Diseases",
        "Cancers",
        "Foodboorne Diseases",
        "Genetic Disorders",
        "Viral Diseases",
        "Neurological Diseases/Disorders",
        "Immunology",

        # Other (biology)
        "Found in Human Blood",
        "Fingerprinting",
        "Nutrition",
        "Items Listed on FDA Nutrition Facts Label",
        "Medical",
        "Zoology",

        # Chemistry
        "Chemistry",

        # Elements
        "Elements",
        "Metals",
        "Semimetals",
        "Nonmetals",
        "Elements Discovered After 1900",
        "Elements Named After Places",
        "Manmade Elements",
        "Noble Gases",

        # Compounds
        "Compounds",
        "Organic Compounds",
        "Compound Acids",

        # Matter
        "Matter",
        "States of Matter",
        "Phase Changes",
        "Properties of Matter",

        # Other (chemistry)
        "Chem Lab",
        "Chem Lab Equipment",
        "Gases",
        "Types of Chemical Reactions"

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
        1, # Respiratory System
        
        # Cells/Genetics
        2, # Cells
        9, # Genetics
        19, # Cell Structures
        1, # Cell Structures in Plant Cells
        1, # Cell Structures in Animal Cells
        1, # Cell Structures in Eukaryotic Cells
        1, # Types of Cells in Human Bodies
        2, # Cell Division
        2, # DNA
        1, # Nucleotides
        1, # Heredity

        # Biochemistry
        1, # Enzymes
        1, # Hormones
        1, # Neurotransmitters
        1, # Amino Acids

        # Names
        1, # Animals
        5, # Bacteria
        1, # Pathogens
        1, # Viruses
        1, # Protists
        7, # Trees
        1, # Deciduous Trees
        1, # Trees of North America
        8, # Reptiles
        1, # Reptile Orders
        12, # Dinosaurs
        1, # North American Dinosaurs
        5, # Amphibians
        1, # Amphibian Orders
        3, # Plants
        1, # Plant Phyla
        3, # Flowers
        1, # Flowering Plants
        1, # Edible Herbs
        1, # Submerged Aquatic Vegetation
        4, # Birds
        1, # Birds of Prey
        1, # State Birds
        5, # Insects
        1, # Insect Anatomy
        1, # Spiders
        9, # Mammals
        2, # Marsupials
        1, # Marine
        1, # Whales
        2, # Primates
        1, # Dog Breeds
        1, # Mammals of Africa
        1, # Mammals of North America
        1, # Mammals of Michigan
        3, # Fish
        1, # Fungi
        1, # Mushrooms
        1, # Fruits
        1, # Stone Fruitt
        2, # Vegetables
        1, # Root Vegetables
        3, # Invasive Species
        1, # Invasive Species of Michigan
        1, # Invasive Aquatic Plants
        1, # Poisonous or Venomous Animals
        3, # Vertebrates
        1, # Land Vertebrates
        2, # Invertebrates
        4, # Endagered Species
        1, # Unicellular Organisms
        1, # Animals with Antlers
        1, # Domesticated Animals
        1, # Prehistoric Aquatic Animals
        1, # Coral
        2, # Aquatic
        1, # Nocturnal Animals
        1, # Extinct Animals
        3, # Marine


        3, # Taxonomy

        3, # Evolution

        # Ecology
        8, # Ecology
        9, # Biomes
        1, # Terrestrial Biomes
        2, # Ecosystems
        2, # Abiotic Factors
        1, # Biogeochemical Cycles
        2, # Water Cycle 
        1, # Soil Types
        2, # Pollution
        1, # Population Factors in Size
        1, # Symbiotic Relationships
        1, # Food Webs
        1, # Trophic Levels

        # Botany
        1, # Botany
        3, # Plant Parts
        1, # Parts of Flowers

        # Epidemiology
        1, # Epidemiology
        11, # Diseases/Disorders
        2, # Human Diseases
        1, # Infectious Diseases
        2, # Cancers
        2, # Foodborne Diseases
        3, # Genetic Disorders
        1, # Viral Diseases
        1, # Neurological Disorders
        1, # Immunology

        # Other (Biology)
        1, # Found in Human Blood
        1, # Fingerprinting
        1, # Nutrition
        1, # Items Listed on FDA Nutrition Facts Label
        1, # Medical
        1, # Zoology

        # Chemistry
        6, # Chemistry

        # Elements
        37, # Elements
        7, # Metals
        1, # Semimetals
        2, # Nonmetals
        1, # Elements Discovered After 1900
        1, # Elements Named After Places
        1, # Manmade Elements
        2, # Noble Gases

        # Compounds
        1, # Compounds
        1, # Organic Compounds
        1, # Compound Acids

        # Matter
        2, # Matter
        3, # States of Matter
        2, # Phase Changes
        1, # Properties of Matter

        # Other (Chemistry)
        1, # Chem Lab
        2, # Chem Lab Equipment
        1, # Gases
        1 # Type of Chemical Reaction


        ]
