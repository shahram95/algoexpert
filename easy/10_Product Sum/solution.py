def productSum(array, multiplier=1):
    total = 0

    for element in array:
        if type(element) is list:
            total += productSum(element, multiplier+1)
        else:
            total += element
    return total*multiplier