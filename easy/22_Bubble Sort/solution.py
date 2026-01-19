def bubbleSort(array):
    counter = 0
    isSorted = False

    while not isSorted:
        isSorted = True

        for i in range(len(array)-1-counter):
            if array[i] > array[i+1]:
                array = swap(i,i+1,array)
                isSorted = False
        counter += 1
    return array

def swap(i,j,array):
    array[i], array[j] = array[j], array[i]
    return array