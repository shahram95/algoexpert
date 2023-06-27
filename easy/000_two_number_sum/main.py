def twoNumberSum(array, targetSum):
	idx_mapping = dict()
	
	for idx, num in enumerate(array):
		comp = targetSum - num
		
		if comp in idx_mapping:
			return [comp,num]
		else:
			idx_mapping[num] = idx
	
	return []

if __name__ == "__main__":
	array = [3, 5, -4, 8, 11, 1, -1, 6]
	targetSum = 10
	gt = [-1,11]
	
	output = twoNumberSum(array, targetSum)
	
	print("Ground truth is: {}".format(gt))
	print("Your solution output is: {}".format(output))
