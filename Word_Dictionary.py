# have a Python dictionary that has a key/value pair that represents a word and  its definition
# collect input from the user, input is a word
# check if the word is in the dictionary


# We install PyDictionary
from PyDictionary import PyDictionary

dictionary = PyDictionary()

while True:
    word = input("Enter your word: ")
    if word  == "":
        break
    print(dictionary.meaning(word))
