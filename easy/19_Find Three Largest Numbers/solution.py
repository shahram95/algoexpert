def findThreeLargestNumbers(array):
    ThreeNumbers = [None for _ in range(3)]

    for num in array:
        if ThreeNumbers[2] is None or ThreeNumbers[2] < num:
            ThreeNumbers = shiftAndUpdate(ThreeNumbers, num, 2)
        elif ThreeNumbers[1] is None or ThreeNumbers[1] < num:
            ThreeNumbers = shiftAndUpdate(ThreeNumbers, num, 1)
        elif ThreeNumbers[0] is None or ThreeNumbers[0] < num:
            ThreeNumbers = shiftAndUpdate(ThreeNumbers, num, 0)
    return ThreeNumbers

def shiftAndUpdate(array, num, idx):
    for i in range(idx+1):
        if i == idx:
            array[i] = num
        else:
            array[i] = array[i+1]
    return array