def isPalindrome(string):
	lp = 0
	rp = len(string)-1
	
	while lp<=rp:
		if string[lp] != string[rp]:
			return False
		lp += 1
		rp -= 1
	
	return True


if __name__ == "__main__":
	string = "abcdcba"
	gt = True
	
	output = isPalindrome(string)
	
	print("The ground truth is: {}".format(gt))
	print("The solution of output is: {}".format(output))
