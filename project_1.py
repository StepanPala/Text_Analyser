# Header
"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Štěpán Pala
e-mail: Palast@seznam.cz
"""

import re
from source_texts import texts
from login_data import users

# Login verification
username = input("Please enter your username: ")
if users.get(username) != input("Please enter your password: "):

    # User not recognized
    print("Unregistered user, terminating program…")

# Login successful
else:
    print(
        f"{'-' * 42}\n"
        f"Welcome, {username.title()}.\n"
        f"There are three texts to be analysed.\n"
        f"{'-' * 42}"
        )

    # Text analysis
    allowed_input = input("Please enter 1, 2 or 3 to select a text: ")
    print(f"{'-' * 42}")

    # Input check
    # Not a number
    if not allowed_input.isdigit():
        print("The entered value is not a number, terminating program…")

    # Wrong number
    elif allowed_input not in ["1", "2", "3"]:
        print("You have entered an invalid number, terminating program…")

    else:
        # Text split
        index = int(allowed_input) - 1
        words = texts[index].split()

        # Number of words
        words_number = len(words)

        # Titlecase words
        words_title = len([titlecase for titlecase in words if titlecase.istitle()])

        # Uppercase words
        words_upper = len(
            [uppercase for uppercase in words if uppercase.isupper() and uppercase.isalpha()]
            )

        # Lowercase words
        words_lower = len([lowercase for lowercase in words if lowercase.islower()])

        # Numeric strings and their sum
        numeric_strings = len([numeric for numeric in words if numeric.isdigit()])
        num_sum = sum(int(numeric) for numeric in words if numeric.isdigit())

        # Print the results
        print(
            f"There are {words_number} words in the text.\n"
            f"There are {words_title} titlecase words in the text.\n"
            f"There are {words_upper} uppercase words in the text.\n"
            f"There are {words_lower} lowercase words in the text.\n"
            f"There are {numeric_strings} numeric strings in the text.\n"
            f"The sum of all the numbers is {num_sum}."
            )

        # Graphical representation
        # Words length and number
        words_len = {}
        for word in words:
            # Removes unwanted characters
            word_clean = re.sub(r"[^a-zA-Z0-9]", "", word.strip())
            length = len(word_clean)
            words_len.setdefault(length, 0)
            words_len[length] += 1
            words_len_sorted = dict(sorted(words_len.items()))

        # Print the chart
        print(
            f"{'-' * 42}\n"
            f"LEN|{'OCCURENCES':^20}|NR.\n"
            f"{'-' * 42}\n"
        )
        for idx, occurence in words_len_sorted.items():
            print(
                f"{idx:>3}|{('*' * int(occurence)):<20}|{occurence:<3}"
            )
