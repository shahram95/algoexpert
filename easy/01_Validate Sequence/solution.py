def isValidSubsequence(array, sequence):
    arrayIdx = 0
    sequenceIdx = 0

    while arrayIdx < len(array) and sequenceIdx < len(sequence):
        if sequence[sequenceIdx] == array[arrayIdx]:
            sequenceIdx += 1
        arrayIdx += 1
    return sequenceIdx == len(sequence)