from Dictionary import realDict
import random



def run():
    wordList = list(realDict.keys())
    max_num = len(list(realDict.keys()))
    # print(len(list(wordList)))
    # This secttion is for instant run
    while True:
        randnumber = random.randint(0, max_num)
        try:
            randomword = wordList[randnumber]
            word = input("Press Enter To Continue...  \nOr Ask a Follow up word...  >")
            if word == "":
                print(f"{randomword}:{realDict[randomword]}")
            elif word != "":
                print(f"{word.upper()}: {realDict[word]}")

        except KeyError:
            print(f"{word} Not Found in realDict...  ")
            return run()


run()
