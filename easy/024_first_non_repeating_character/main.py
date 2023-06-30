from collections import Counter
print("here")
def firstNonRepeatingCharacter(string):
	letter_freq = Counter(string)
	
	for letter, count in zip(letter_freq.keys(), letter_freq.values()):
		if count == 1:
			return string.index(letter)
	return -1

if __name__ == "__main__":
	print("here")
	string = "abcdcaf"
	gt = 1
	
	output = firstNonRepeatingCharacter(string)
	
	print("The ground truth is: {}".format(gt))
	print("Your solutions output is: {}".format(output))
	print("---------------------------------")
