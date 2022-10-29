import re
import time
from PyDictionary import PyDictionary

# Dictionary Setup

dictionary = {}
originalDictionary = []
wordList = []

regex_patterns = {
    'word': r'(\w+)\n',
    'deff': r'(\d.*|Defn.*)\n',
    'defcont': r'(\w+\w*)\n'
    }


def run():
    deffList = []

    def innerFunction(word):
        if word != "":
            print(word)
            dictionary[word] = " ".join(deffList)

    with open('dictionary.txt', 'r') as f:
        for lines in f.readlines():
            originalDictionary.append(lines)
        
    with open('words.txt', 'r') as fr:
        count = 0
        for line in originalDictionary:
            for key, value in regex_patterns.items():
                intent = key
                regex_pattern = value
                found_match = re.match(regex_pattern, line)
                if found_match:
                    if intent == 'word':
                        word = found_match.groups()[0]
                        count +=1
                        innerFunction(word)
                        deffList = []
                        # time.sleep(0.01)
                        
                        
                    else:
                        data = line.strip('\n')
                        if data not in deffList:
                            deffList.append(data)

                
                else:
                    data = line.strip('\n')
                    if data not in deffList:
                        deffList.append(data)


run()
print(list(dictionary))


with open('DictionaryReal.py', 'a') as fw:
    fw.write('pydictionary = {\n')
    for key, value in dictionary.items():
        fw.write(f'{key}: {value},\n')
    fw.write('}')
