import re


def cleaner(text):
    removespace = ['"']
    removenon = ["'", ';', ',', '(', ')', '[', ']', '{', '}', '`']
    raw_text = []
    clean_text = []
    finished_text = []
    # OPTION 1
    # with open(text, 'r') as f:
    # for data in f.readlines():
    # raw_text.append(data)
    # OPTION 2
    # for lines in text.split('\n'):
        # raw_text.append(lines)
    # print(list(raw_text))

    for sentences in text.split():
        for letters in sentences:
            # re.sub(" +", " ", letters)
            if letters in removespace:
                new = letters.replace(letters, ' ')
                clean_text.append(new)

            elif letters in removenon:
                new = letters.replace(letters, '')
                clean_text.append(new)

            elif letters not in removenon and letters not in removespace:
                clean_text.append(letters.lower())

    # print(clean_text)
    new = ''.join(clean_text)
    newest = re.sub(" +", " ", new)
    finished_text.append(newest)
    # print(list(finished_text))
    return finished_text


# cleaner('sherlock.txt')