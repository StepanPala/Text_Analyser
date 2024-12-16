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
if users.get(username) == input("Please enter your password: "):
    print(
        f"{"-" * 42}\n"
        f"Welcome, {username.title()}.\n"
        f"There are three texts to be analysed.\n"
        f"{"-" * 42}"
        )
  
    # Text analysis
    allowed_input = input("Please enter 1, 2 or 3 to select a text: ")

    print(f"{"-" * 42}")

    # Correct input
    if allowed_input.isdigit() and int(allowed_input) in (1, 2, 3):
        
        # Number of words
        index = int(allowed_input) - 1
        words_number = len(texts[index].split())
        print(f"There are {words_number} words in the text.")

        # Titlecase words
        words_title = 0
        for titlecase in texts[index].split():
            if titlecase.istitle():
                words_title += 1
        print(f"There are {words_title} titlecase words in the text.")

        # Uppercase words
        words_upper = 0
        for uppercase in texts[index].split():
            if uppercase.isupper() and uppercase.isalpha():
                words_upper += 1
        print(f"There are {words_upper} uppercase words in the text.")

        # Lowercase words
        words_lower = 0
        for lowercase in texts[index].split():
            if lowercase.islower():
                words_lower += 1
        print(f"There are {words_lower} lowercase words in the text.")

        # Numeric strings
        num_strings = 0
        for numeric in texts[index].split():
            if numeric.isdigit():
                num_strings += 1
        print(f"There are {num_strings} numeric strings in the text.")

        # Sum of all numbers
        numeric_list = []
        for numeric in texts[index].split():
            if numeric.isdigit():
                numeric_list.append(int(numeric))
        num_sum = sum(numeric_list)        
        print(f"The sum of all the numbers is {(num_sum)}.")

        # Graphical representation
        # Words length
        words_len = {}
        for words in texts[index].split():

            # Remove unwanted characters
            words_clean = words.strip(",.?!")

            # Calculate length and number of words
            length = len(words_clean)
            if not length in words_len:
                words_len[length] = 1
            else:
                words_len[length] += 1

        # Convert to list and sort the list
        words_list = list(words_len.items())
        words_list.sort()
        
        # Print the result
        print(
            f"{"-" * 42}\n"
            f"LEN|{"OCCURENCES":^20}|NR.\n"
            f"{"-" * 42}\n"
        )
        for idx, occurence in words_list:
            print(
                f"{idx:>3}|{("*" * int(occurence)):<20}|{occurence:<3}"
            )
  
    # Not a digit
    elif not allowed_input.isdigit():
        print("The entered value is not a number, terminating program…")

    # Wrong digit
    else:
        print("You have entered an invalid number, terminating program…")
        
# User not recognized
else:
    print("Unregistered user, terminating program…")