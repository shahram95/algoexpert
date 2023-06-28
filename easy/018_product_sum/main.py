def productSum(array, multiplier=1):
	total = 0
	
	for element in array:
		if type(element) is list:
			total += productSum(element, multiplier+1)
		else:
			total += element
	
	return multiplier*total

if __name__ == "__main__":
	array = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]
	gt = 12
	
	output = productSum(array)
	
	print("The ground truth is: {}".format(gt))
	print("Your solution output is: {}".format(output))
	print("----------------------------------------")
