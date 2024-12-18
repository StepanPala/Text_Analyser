# Header
"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Štěpán Pala
e-mail: Palast@seznam.cz
"""

# Source texts
texts = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley.''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

# Registered users
users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

# Login verification
username = input("Please enter your username: ")
if users.get(username) != input("Please enter your password: "):
    
    # User not recognized
    print("Unregistered user, terminating program…")
    exit()

# Login successful
else:
    print(
        f"{"-" * 42}\n"
        f"Welcome, {username.title()}.\n"
        f"There are three texts to be analysed.\n"
        f"{"-" * 42}"
        )
  
    # Text analysis
    allowed_input = input("Please enter 1, 2 or 3 to select a text: ")
    print(f"{"-" * 42}")

    # Input check
    # Not a number
    if not allowed_input.isdigit():
        print("The entered value is not a number, terminating program…")
        exit()

    # Wrong number
    if allowed_input not in ["1", "2", "3"]:
         print("You have entered an invalid number, terminating program…")
         exit()

    else:
        # Text split
        index = int(allowed_input) - 1
        words = texts[index].split()
        
        # Number of words
        words_number = len(words)
        
        # Titlecase words
        words_title = [titlecase for titlecase in words if titlecase.istitle()]
        words_title_num = len(words_title)
        
        # Uppercase words
        words_upper = [uppercase for uppercase in words if uppercase.isupper() and uppercase.isalpha()]
        words_upper_num = len(words_upper)
        
        # Lowercase words
        words_lower = [lowercase for lowercase in words if lowercase.islower()]
        words_lower_num = len(words_lower)
        
        # Numeric strings and their sum
        numeric_strings = [numeric for numeric in words if numeric.isdigit()]
        numeric_strings_num = len(numeric_strings)
        num_sum = sum(int(numeric) for numeric in numeric_strings)
        
        # Print the results
        print(
            f"There are {words_number} words in the text.\n"
            f"There are {words_title_num} titlecase words in the text.\n"
            f"There are {words_upper_num} uppercase words in the text.\n"
            f"There are {words_lower_num} lowercase words in the text.\n"
            f"There are {numeric_strings_num} numeric strings in the text.\n"
            f"The sum of all the numbers is {num_sum}."
            )
        
        # Graphical representation
        # Words length and number
        words_len = {}
        for word in words:
            word_clean = word.strip(",.?!")
            if word_clean:
                length = len(word_clean)
                if length in words_len:
                    words_len[length] += 1
                else:
                    words_len[length] = 1
        words_len_sorted = dict(sorted(words_len.items()))
                
        # Print the chart
        print(
            f"{"-" * 42}\n"
            f"LEN|{"OCCURENCES":^20}|NR.\n"
            f"{"-" * 42}\n"
        )
        for idx, occurence in words_len_sorted.items():
            print(
                f"{idx:>3}|{("*" * int(occurence)):<20}|{occurence:<3}"
            )