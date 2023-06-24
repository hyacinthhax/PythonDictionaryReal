from results import *
import random


# We import a wordList to make selections and randoms
wordList = []
with open('words.txt', 'r') as f:
    for data in f.read().split('\n'):
        data = data.strip('\n')
        wordList.append(data)

# We Loop through and select a random word if empty string
while True:
    print("Welcome to the Free Dictionay. Type your word and get a definition...")
    word = input("-->")
    try:
        if word == "":
            randnumber = random.randint(0, 94251)
            randomword = wordList[randnumber]
            print(f"{randomword}:{list(realDict[randomword])}")
        elif word != "":
            print(f"{word.upper()}: {realDict[word.upper()][0]}")

        input("Enter to Continue...  ")

    except KeyError:
        print(f"{word} Not Found in realDict...  ")
