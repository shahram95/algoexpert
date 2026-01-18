from collections import Counter

def firstNonRepeatingCharacter(string):
    count_dict = Counter(string)
    for char,count in count_dict.items():
        if count == 1:
            return string.index(char)
    return -1
