def semordnilap(words):
	output = list()
	wordList = set(words)
	
	for word in words:
		reverse = word[::-1]
		
		if reverse in wordList and reverse != word:
			output.append([word, reverse])
			words.remove(word)
			words.remove(reverse)
	return output

if __name__ == "__main__":
	words = ["diaper", "abc", "test", "cba", "repaid"]
	gt = [["diaper", "repaid"], ["abc", "cba"]]
	
	output = semordnilap(words)
	
	print("The ground truth is: {}".format(gt))
	print("Your solutions output is: {}".format(output))
	print("-------------------------------------")
