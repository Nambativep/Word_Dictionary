# write the signature of the function
def main():
    # create a variable word dictionary and store key value pairs
    word_dictionary =  {
        "hi": "a way of greeting",
        "eyes": "an organ for seeing",
        "earth": "a planet in space",
        "God": " a supreme spirit being resident in heaven, "
               "believed by all and sundry to be the creator of the universe",
        "Api": "Application User Interface"
    }
    while True:
        word = input("Enter a word: ")
        if word == "":
            break
        if word in word_dictionary:
            print(word, ":", word_dictionary[word])

main()


