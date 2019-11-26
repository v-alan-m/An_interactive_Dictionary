import json
from difflib import get_close_matches

# Load the JSON file into a dictionary
data = json.load(open("data.json"))

# Ask the user to enter in a word to search
def search_word():
    word = input("Enter word: ")
    return word
    
# Find the corresponding value to the key that is inserted into stdin
def translate(w):
# Make stdin entries lower case before preforming the dictionary search
    w = w.lower()
# If the key is present the return the corresponding value
    if w in data:
        return data[w]
# Return the closest word to the stdin entry if stdin entry is not a present key
    elif len(get_close_matches(w, data.keys())) > 0:
        check =  input("Did you mean %s? Enter Y if yes, or N if no: " % get_close_matches(w, data.keys())[0])
        if check == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif check == "N":
            print("This word does not exist, please enter in another word")
        else:
            print("Please enter in Y or N")
            
# If entry is unrecognisable print a statement stating so and ask for a new entry
    else:
        return "This word does not exist, please enter in another word"
    
def definition():    
    output = translate(search_word())
    if type(output) == list:
    # If output_value is a string then iterate through the list and print out the items
        for item in output:
            print(item)

definition()