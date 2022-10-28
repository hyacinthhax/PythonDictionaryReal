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
    count = 0
    with open('dictionary.txt', 'r') as f:
        for lines in f.readlines():
            originalDictionary.append(lines)
        
    with open('words.txt', 'r') as fr:
        for line in originalDictionary:
            for key, value in regex_patterns.items():
                intent = key
                regex_pattern = value
                found_match = re.match(regex_pattern, line)
                if found_match:
                    if intent == 'word':
                        time.sleep(0.03)
                        deffList = []
                        count +=1
                        
                    elif intent == 'deff':
                        # print("Def Found")
                        data = found_match.groups()[0]
                        deffList.append(data)

                    elif intent == 'defcont':
                        # print("Def Found")
                        data = found_match.groups()[0]
                        deffList.append(data)
                    
                elif fr.readline(count).strip('\n') not in dictionary:
                    word = fr.readline(count).strip('\n')
                    dictionary[word] = " ".join(deffList)


run()
# print(list(dictionary))
with open('DictionaryReal.py', 'w+') as fw:
    fw.write(f'pythonDictionary = {dictionary}')