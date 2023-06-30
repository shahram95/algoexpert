def commonCharacters(strings):
	smallestString = min(strings, key=len)
	potentialCommonCharacters = list(set(smallestString))
	buffer_lst = potentialCommonCharacters.copy()
	
	for string in strings:
		for char in potentialCommonCharacters:
			if char not in set(string):
				buffer_lst.remove(char)
		potentialCommonCharacters = buffer_lst.copy()
	
	return potentialCommonCharacters
	
if __name__ == "__main__":
	strings = ["abc", "bcd", "cbad"]
	gt = ["b", "c"]
	
	output = commonCharacters(strings)
	
	print("The ground truth is: {}".format(gt))
	print("You solution output is: {}".format(output))
	print("-----------------------------")
