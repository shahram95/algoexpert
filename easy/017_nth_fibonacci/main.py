import math

def getNthFib(n):
	sqrt5 = math.sqrt(5)
	phi = (1+sqrt5)/2
	psi = (1-sqrt5)/2
	
	nth_term = int((phi**(n-1) - psi**(n-1))/sqrt5)
	return nth_term

if __name__ == "__main__":
	n = 2
	gt = 1
	
	output = getNthFib(n)
	
	print("The ground truth is: {}".format(gt))
	print("Your solution output is: {}".format(output))
	print("---------------------------------------")
	
	n = 6
	gt = 5
	
	output = getNthFib(n)
	
	print("The ground truth is: {}".format(gt))
	print("Your solution output is: {}".format(output))
	print("---------------------------------------")
