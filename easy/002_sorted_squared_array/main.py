def sortedSquaredArray(array):
	lp = 0
	rp = len(array)-1
	insert_idx = len(array)-1
	output = [0 for _ in range(len(array))]
	
	while lp<=rp:
		if abs(array[lp]) >= abs(array[rp]):
			output[insert_idx] = array[lp]**2
			lp += 1
		else:
			output[insert_idx] = array[rp]**2
			rp -= 1
		
		insert_idx -= 1
	
	return output

if __name__ == "__main__":
	array = [1, 2, 3, 5, 6, 8, 9]
	output = sortedSquaredArray(array)
	gt = [1, 4, 9, 25, 36, 64, 81]
	print("The ground truth is: {}".format(gt))
	print("Your solution output is: {}".format(output))
	print("------------------------------------------")
