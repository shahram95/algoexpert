def sortedSquaredArray(array):
    out = [0] * len(array)
    lp = 0
    rp = len(array)-1
    insertIdx = len(array)-1

    while lp<=rp:
        if abs(array[lp]) < abs(array[rp]):
            out[insertIdx] = array[rp]**2
            rp -=1
        else:
            out[insertIdx] = array[lp]**2
            lp += 1
        insertIdx -=1
    return out