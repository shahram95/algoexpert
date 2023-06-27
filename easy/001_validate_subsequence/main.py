def isValidSubsequence(array,sequence):
	array_idx = 0
	sequence_idx = 0
	
	while array_idx < len(array) and sequence_idx < len(sequence):
		if array[array_idx] == sequence[sequence_idx]:
			sequence_idx += 1
		array_idx += 1
	
	return len(sequence) == sequence_idx

if __name__ == "__main__":
	array = [5, 1, 22, 25, 6, -1, 8, 10]
	sequence = [1, 6, -1, 10]
	output = isValidSubsequence(array,sequence)
	print("The ground truth is: {}".format(True))
	print("Your solution output is: {}".format(output))
	print("--------------------------------------------")
