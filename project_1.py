# Header
"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Štěpán Pala
e-mail: Palast@seznam.cz
"""

import sys
import re
from source_texts import texts
from login_data import users

DASH_SEPARTOR = '-' * 42

def print_separator():
    """Prints a separator."""
    print(DASH_SEPARTOR)

def validate_input(input_value, valid_options):
    """Validates the input value."""
    if not input_value.isdigit():
        sys.exit("The entered value is not a number, terminating program…")
    if input_value not in valid_options:
        sys.exit("You have entered an invalid number, terminating program…")

# Login verification
username = input("Please enter your username: ")
password = input("Please enter your password: ")
if users.get(username) != password:

    # User not recognized
    sys.exit("Unregistered user, terminating program…")

# Login successful
print_separator()
print(f"Welcome, {username.title()}.")
print("There are three texts to be analysed.")
print_separator()

# Text analysis
text_choice = input("Please enter 1, 2 or 3 to select a text: ")
print_separator()

# Input check
validate_input(text_choice, ["1", "2", "3"])

# Text split
index = int(text_choice) - 1
words = texts[index].split()

# Number of words
words_number = len(words)

# Titlecase words
words_title = len([word for word in words if word.istitle()])

# Uppercase words
words_upper = len([word for word in words if word.isupper() and word.isalpha()])

# Lowercase words
words_lower = len([word for word in words if word.islower()])

# Numeric strings and their sum
numeric_strings = len([word for word in words if word.isdigit()])
num_sum = sum(int(word) for word in words if word.isdigit())

# Print the results
results = {
    "words in the text": words_number,
    "titlecase words in the text": words_title,
    "uppercase words in the text": words_upper,
    "lowercase words in the text": words_lower,
    "numeric strings in the text": numeric_strings,
    "sum of all the numbers": num_sum,
}

for description, value in results.items():
    if "sum" in description:
        print(f"The {description} is {value}.")
    else:
        print(f"There are {value} {description}.")

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
print_separator()
print(f"LEN|{'OCCURENCES':^20}|NR.")
print_separator()

max_occurence = max(words_len_sorted.values())
scale_factor = 20 / max_occurence if max_occurence > 0 else 1

for idx, occurence in words_len_sorted.items():
    scaled_occurence = int(occurence * scale_factor)
    print(f"{idx:>3}|{('*' * scaled_occurence):<20}|{occurence:<3}")
