from requests import get

phrase = input("Enter the word or phrase you want to find the synonyms of: ").lower()

try:

    maximum = int(input("Enter the maximum number of synonyms you want: "))

except ValueError:

    print("Please enter a valid value.")

if maximum > 0:

    words = phrase.split(" ")

    endpointText = "".join(f"{word}+" for word in words)

    response = get(f"https://api.datamuse.com/words?ml={endpointText}&max={maximum}")

    if len(response.json()) > 0:

        print("The synonyms are-:\n")

        for ouput in response.json():

            print(f"\t{ouput['word']}")

    else:

        print("No synonyms found.")

else:

    print("Please enter a valid value.")