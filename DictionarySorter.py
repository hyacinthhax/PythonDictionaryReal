import re
from textcleaner import cleaner


wordsList = []
defList = []
originalDictionary = []
definition = ""
newDict = {}

with open('Dictionary/dictionary.txt', 'r') as f:
	for lines in f.readlines():
		originalDictionary.append(lines)
# print(list(originalDictionary))
    
regex_patterns = {
	'word': r"(\w+)\n",
}

for lines in originalDictionary:
	if lines != "\n":
		for key, value in regex_patterns.items():
			testset = 0
			intent = key
			regex_pattern = value
			found_match = re.match(regex_pattern, lines)
			if found_match:
				if intent == 'word':
					definition = ""
					count = +1
					word = found_match.groups()[0]
					wordsList.append(word)
					testset = 0

			else:
				testset = 1
				definition = definition + " " + lines.strip('\n')
	newDict[word] = definition
	# defList.append(definition)


# while True:
# 	print(newDict[input("Word:  ").upper()])
# print(len(list(wordsList)))
# print(list(defList))
# 
with open('Dictionary.py', 'w') as fw:
	fw.write("realDict = {\n")
	for words, definitions in newDict.items():
		fw.write(f"'{words}':{cleaner(definitions)},\n")
	fw.write('}')
