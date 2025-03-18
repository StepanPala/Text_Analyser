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

def validate_input(input_value: str, valid_options: list) -> bool:
    """
    Validates the input value and prints error messages.

    Args:
        input_value: The input value to be validated.
        valid_options: A list of valid options.

    Returns:
        bool: True if the input is valid, False otherwise.
    """
    if not input_value.isdigit():
        print("The entered value is not a number, terminating program…")
        return False
    if input_value not in valid_options:
        print("You have entered an invalid number, terminating program…")
        return False
    return True

def analyse_text(input_text: str) -> dict[str, int]:
    """
    Analyses the given text and returns statistics.

    Args:
        input_text: The text to be analysed.

    Returns:
        dict: A dictionary with the statistics.
    """
    input_words = input_text.split()
    words_number = len(input_words)
    words_title = sum(1 for word in input_words if word.istitle())
    words_upper = sum(1 for word in input_words if word.isupper() and word.isalpha())
    words_lower = sum(1 for word in input_words if word.islower())
    numeric_strings = [int(word) for word in input_words if word.isdigit()]
    num_sum = sum(numeric_strings)
    return{
        "words in the text": words_number,
        "titlecase words in the text": words_title,
        "uppercase words in the text": words_upper,
        "lowercase words in the text": words_lower,
        "numeric strings in the text": len(numeric_strings),
        "sum of all the numbers": num_sum,
    }

def generate_and_print_chart(word_list: list[str]):
    """
    Generates and prints a chart with word lengths.

    Args:
        word_list: A list of words to generate the chart from.
    """
    words_len = {}
    for word in word_list:
        # Removes unwanted characters
        word_clean = re.sub(r"[^a-zA-Z0-9]", "", word.strip())
        length = len(word_clean)
        words_len.setdefault(length, 0)
        words_len[length] += 1
    words_len_sorted = dict(sorted(words_len.items()))

    print_separator()
    print(f"LEN|{'OCCURENCES':^20}|NR.")
    print_separator()

    max_occurence = max(words_len_sorted.values())
    scale_factor = 20 / max_occurence if max_occurence > 0 else 1

    for idx, occurence in words_len_sorted.items():
        scaled_occurence = int(occurence * scale_factor)
        print(f"{idx:>3}|{('*' * scaled_occurence):<20}|{occurence:<3}")

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

# Input check
while True:
    text_choice = input("Please enter 1, 2 or 3 to select a text: ")
    print_separator()
    if validate_input(text_choice, ["1", "2", "3"]):
        break # Exit the loop if the input is valid
    print_separator()
    sys.exit()

# Text split
index = int(text_choice) - 1
text = texts[index]

# Analyse text
results = analyse_text(text)

# Print the results
for description, value in results.items():
    if "sum" in description:
        print(f"The {description} is {value}.")
    else:
        print(f"There are {value} {description}.")

if __name__ == "__main__":
    words = text.split()
    generate_and_print_chart(words)
