import re


# We define the lists and Dict's, We only need the definition, originalDictionary, and newDict to function properly
wordsList = []
defList = []
originalDictionary = []
definition = ""
newDict = {}

# We next generate the originalDictionary, a 100,000+ line Download line for line
with open('Dictionary/dictionary.txt', 'r') as f:
	for lines in f.readlines():
		originalDictionary.append(lines)
# print(list(originalDictionary))
# I define regex patterns for words everything else is a definition
regex_patterns = {
	'word': r"(\w+)\n",
}

# Next we open the list of the dictionary to regex
for lines in originalDictionary:
	# Making sure none are empty
	if lines != "\n":
		for key, value in regex_patterns.items():
			# We declare a test set to try for when we have a new word
			testset = 0
			intent = key
			regex_pattern = value
			# We find a match on the regex pattern
			found_match = re.match(regex_pattern, lines)
			if found_match:
				if intent == 'word':
					# We clear the definition as we need more than one. Also count += 1, used in development
					definition = ""
					count = +1
					# We matched the word to a group that we call
					word = found_match.groups()[0]
					# wordList was used in Development
					wordsList.append(word)
					# We reset the testset
					testset = 0
			
			# We find the rest of the definition with else after if statement. So testset == 1
			else:
				testset = 1
				definition = definition + " " + lines.strip('\n')
	# defList was used in testing, and newDict replaced it.
	newDict[word] = definition
	# defList.append(definition)

# Run this to do single word definitions
# while True:
# 	print(newDict[input("Word:  ").upper()])
# print(len(list(wordsList)))
# print(list(defList))
# 
# Run this to create a realDictionary in python for later
with open('Dictionary.py', 'w') as fw:
	fw.write('RealDict = {\n')
	for words, definitions in newDict.items():
		fw.write(f"{words}:{definitions},\n")
	fw.write('}')
