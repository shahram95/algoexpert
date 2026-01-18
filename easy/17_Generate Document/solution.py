from collections import Counter

def generateDocument(characters, document):
    character_dict = Counter(characters)
    document_dict = Counter(document)

    for char,count in document_dict.items():
        if count > character_dict.get(char,0):
            return False
    return True