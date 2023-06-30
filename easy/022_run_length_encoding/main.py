def runLengthEncoding(string):
	new_str = ""
	currentRunLength = 1
	
	for i in range(1, len(string)):
		currentCharacter = string[i]
		previousCharacter = string[i-1]
		
		if currentCharacter != previousCharacter or currentRunLength == 9:
			new_str += str(currentRunLength)
			new_str += previousCharacter
			currentRunLength = 0
		
		currentRunLength += 1
	
	new_str += str(currentRunLength)
	new_str += string[len(string)-1]
	
	return new_str

if __name__ == "__main__":
	string = "AAAAAAAAAAAAABBCCCCDD"
	gt = "9A4A2B4C2D"
	
	output = runLengthEncoding(string)
	
	print("The ground truth is: {}".format(gt))
	print("Your solution output is: {}".format(output))
	print("-------------------------------------")
