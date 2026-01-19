def commonCharacters(strings):
    potentialCommonCharacters = list(set(min(strings, key=len)))
    buffer = potentialCommonCharacters.copy()

    for string in strings:
        for char in potentialCommonCharacters:
            if char not in string:
                buffer.remove(char)
        potentialCommonCharacters = buffer.copy()
    return potentialCommonCharacters