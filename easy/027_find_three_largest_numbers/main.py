def shiftAndupdate(array, num, idx):
		for i in range(idx+1):
			if idx == i:
				array[idx] = num
			else:
				array[i] = array[i+1]
		return array

def findThreeLargestNumbers(array):
	threeLargest = [None for _ in range(3)]
	
	for num in array:
		if threeLargest[2] is None or threeLargest[2] < num:
			threeLargest = shiftAndupdate(threeLargest, num, 2)
		elif threeLargest[1] is None or threeLargest[1] < num:
			threeLargest = shiftAndupdate(threeLargest, num, 1)
		elif threeLargest[0] is None or threeLargest[0] < num:
			threeLargest = shiftAndupdate(threeLargest, num, 0)
	
	return threeLargest
	
	

if __name__ == "__main__":
	array = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
	gt = [18, 141, 541]
	
	output = findThreeLargestNumbers(array)
	
	print("The ground truth is: {}".format(gt))
	print("Your solution's output is: {}".format(output))
	print("--------------------------------------")
