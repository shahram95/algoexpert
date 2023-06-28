def binarySearch(array, target):
	lp = 0
	rp = len(array)-1
	
	while lp<=rp:
		middle = (lp+rp)//2
		potentialMatch = array[middle]
		
		if potentialMatch == target:
			return middle
		elif potentialMatch>target:
			rp = middle - 1
		else:
			lp = middle + 1
	
	return -1

if __name__ == "__main__":
	array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
	target = 33
	gt = 3
	
	output = binarySearch(array,target)
	
	print("The ground truth is: {}".format(gt))
	print("Your solution result is: {}".format(output))
	print("-----------------------------------------")
