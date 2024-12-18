import re


def cleaner(text):
	# Remove non-printable characters
	text = re.sub(r"[^\x20-\x7E]", "", text)  # Keeps printable ASCII range (space to ~)
	# Normalize spaces
	text = re.sub(r"\s+", " ", text).strip()

	return text

wordsList = []
defList = []
originalDictionary = []
definition = ""
newDict = {}
forbidden = ['\n', "", " ", "-", "\x7f"]

with open('Dictionary/dictionary.txt', 'r') as f:
	for lines in f.readlines():
		if lines not in forbidden:
			originalDictionary.append(lines)
print(list(originalDictionary))

regex_patterns = {
	'word': r"(\w+-*\w*)\s\s\n*",
	'definition': r"(\w+\s\w+)\n"
}

word = ""

for lines in originalDictionary:
	for key, value in regex_patterns.items():
		intent = key
		regex_pattern = value
		found_match = re.match(regex_pattern, lines)
		if found_match:
			if intent == 'word':
				definition = ""
				count = +1
				word = found_match.groups()[0]
				wordsList.append(word.strip(" ").strip("\n"))

		else:
			definition = definition + " " + lines.strip("\n")


		if word != "":
			newDict[word] = definition
			# defList.append(definition)


# while True:
# 	print(newDict[input("Word:  ").upper()])
print(len(list(wordsList)))
# print(list(defList))
# 
with open('Dictionary.py', 'w') as fw:
	fw.write("realDict = {\n")
	for words, definitions in newDict.items():
		fw.write(f'"{words}":"{cleaner(definitions)}",\n')
	fw.write('}')

