from results import *
import random


wordList = []
with open('words.txt', 'r') as f:
    for data in f.read().split('\n'):
        data = data.strip('\n')
        wordList.append(data)

def run():
    # print(len(list(wordList)))
    # This secttion is for instant run
    while True:
        randnumber = random.randint(0, 94251)
        try:
            randomword = wordList[randnumber]
            word = input("Press Enter To Continue...  \nOr Ask a Follow up word...  >")
            if word == "":
                print(f"{randomword}:{list(realDict[randomword])}")
            elif word != "":
                print(f"{word.upper()}: {list(realDict[word.upper()])}")

        except KeyError:
            print(f"{word} Not Found in realDict...  ")
            return run()


run()
