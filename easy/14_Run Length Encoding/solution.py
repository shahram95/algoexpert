def runLengthEncoding(string):
    currLength = 1
    outStr = ''

    for idx in range(1,len(string)):
        currentChar = string[idx]
        previousChar = string[idx-1]

        if currentChar != previousChar or currLength == 9:
            outStr += str(currLength)
            outStr += previousChar
            currLength = 0
        currLength += 1
    
    outStr += str(currLength)
    outStr += string[-1]
    return outStr