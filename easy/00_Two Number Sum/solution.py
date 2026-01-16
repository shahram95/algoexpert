def twoNumberSum(array, targetSum):
    num_dict = dict()

    for num in array:
        comp = targetSum - num
        if comp in num_dict:
            return [comp, num]
        num_dict[num] = True
    return []