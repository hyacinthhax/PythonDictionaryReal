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
        randnumber = random.randint(0, 103136)
        word = wordList[randnumber]
        input("Press Enter To Continue...  ")
        print(f"{word}:{list(realDict[word])}")


run()
