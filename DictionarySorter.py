import re

# Dictionary Setup
dictionary = {}

regex_patterns = {
    'word': r'([A-Z-]+)\n',
    'restricted': r'-+'
}

def parseDefinition(definition_line):
    definition = definition_line.strip()  # Remove leading and trailing whitespace
    definition = re.sub(r'[^\w\s.,-]', '', definition)  # Remove unwanted characters
    return definition

def joinAndCleanDefinitions(definitions):
    joined_definitions = ' '.join(definitions)  # Join definitions into a single string
    split_definitions = [d.strip() for d in re.split(r'\d+\.', joined_definitions) if d.strip()]  # Split by numbers and remove empty lines
    return split_definitions

import re

def parseDictionary():
    with open('Dictionary/dictionary.txt', 'r') as f:
        lines = f.readlines()

    current_word = None
    prev_word = None
    current_definitions = []
    begin_count = 0

    for line in lines:
        for words in line:
                words.replace('-', '')
        word_match = re.search(regex_patterns['word'], line)
        if word_match:
            word = word_match.group(1).strip()
            if not re.search(r'[-]{2,100}', word):
                print(begin_count)
                # Exclude words with hyphens, --, or ---
                if prev_word is not None or begin_count > 0:
                    prev_word = current_word
                current_word = word
                begin_count += 1
                if current_word not in dictionary:
                    dictionary[current_word] = []
                    current_definitions = []

                elif current_word in dictionary:
                    current_definitions = []

        elif not word_match:
            definition = parseDefinition(line)
            current_definitions.append(definition)
            my_set = set(dictionary[current_word])
            my_set.update(current_definitions)
            dictionary[current_word] = list(my_set)

    for words in dictionary.keys():
        print(words)
        joined_and_cleaned_definitions = joinAndCleanDefinitions(dictionary[words])
        if joined_and_cleaned_definitions:
            dictionary[words] = joined_and_cleaned_definitions


def saveDictionaryToFile():
    with open("Dictionary.py", 'w') as wb:
        wb.write("dictionary = {\n")
        for words, defs in dictionary.items():
            wb.write(f"'{words}': {defs}, \n")

        wb.write("}")

def main():
    parseDictionary()
    saveDictionaryToFile()

if __name__ == "__main__":
    main()

