from collections import Counter

def generateDocument(characters, document):
	characters_freq = Counter(characters)
	document_freq = Counter(document)
	
	for letter in document_freq.keys():
		if characters_freq.get(letter,0) < document_freq.get(letter,0):
			return False
	
	return True


if __name__ == "__main__":
	characters = "Bste!hetsi ogEAxpelrt x "
	document = "AlgoExpert is the Best!"
	gt = True
	
	output = generateDocument(characters, document)
	
	print("The ground truth is: {}".format(gt))
	print("Your solution output is: {}".format(output))
	print("------------------------------------")
