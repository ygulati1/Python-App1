import json
from difflib import get_close_matches 
data = json.load(open("data.json", "r"))

def translate(word):
    if word in data:
       return data[word]
    elif word.lower() in data:
        word = word.lower()
        return data[word]
    elif word.upper() in data:
        word = word.upper()
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(word, data.keys())[0])
        if yn == "Y" or yn == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == "N" or yn == "n" : 
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."

word = input("Enter words: ")

output = (translate(word))
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)