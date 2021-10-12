# Importing the necessary function from the module.
from requests import get

# Getting the user input.
phrase = input("Enter the word or phrase you want to find the synonyms of: ").lower()

try:

    maximum = int(input("Enter the maximum number of synonyms you want: "))

# If the user enters a string instead of an integer, this message is printed out instead of the program crashing with an error.
except ValueError:

    print("Please enter a valid value.")

if maximum > 0:

    # Getting the list of words in the phrase.
    words = phrase.split(" ")

    # Creating the url for the api request.
    endpointText = "".join(f"{word}+" for word in words)

    # Getting the json response from the api.
    response = get(f"https://api.datamuse.com/words?ml={endpointText}&max={maximum}")

    if len(response.json()) > 0:

        # Output.
        print("The synonyms are-:\n")

        for ouput in response.json():

            print(f"\t{ouput['word']}")

    # If no synonyms are found for the word/phrase that the user entered, this message is printed out instead of the program terminating.
    else:

        print("No synonyms found.")

# If the user doesnt enter a natural number, this message is printed out instead of the program terminating.
else:

    print("Please enter a valid value.")