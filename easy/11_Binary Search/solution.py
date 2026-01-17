def binarySearch(array, target):
    lp = 0
    rp = len(array)-1

    while lp<=rp:
        middle = (lp+rp)//2

        if array[middle] == target:
            return middle
        elif array[middle] > target:
            rp = middle-1
        else:
            lp = middle+1
    return -1