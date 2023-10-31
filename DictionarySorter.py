import re
from textcleaner import cleaner


wordsList = []
defList = []
originalDictionary = []
definition = ""
word = ""
newDict = {}

with open('dictionary.txt', 'r') as f:
	for lines in f.readlines():
		originalDictionary.append(lines)
# print(list(originalDictionary))

regex_patterns = {
	'word': r'([A-Z-]+)\n',
	'definition': r"(.+ .+ .+ .*)\n"
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
					count = +1
					word = found_match.groups()[0]
					if word != '':
						if word not in wordsList:
							wordsList.append(word)
							definition = ""
							testset = 0
						elif word in wordsList:
							testset = 1

				if intent == 'definition':
					testset = 1
					definition = definition + found_match.groups()[0] + " "


		newDict[word] = definition


with open('Dictionary.py', 'w') as fw:
	fw.write("realDict = {\n")
	for words, definitions in newDict.items():
		fw.write(f"'{words}':{cleaner(definitions)},\n")
	fw.write('}')

with open('words.txt', 'w') as fww:
	for keys in newDict.keys():
		fww.write(f"{keys}\n")
