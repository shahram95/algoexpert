def ceaserCipherEncryptor(string,key):
	string = list(string)
	alphabet_string = list("abcdefghijklmnopqrstuvwxyz")
	
#	if key>26:
#		key %= 26
	
	for idx, char in enumerate(string):
		alpha_idx = alphabet_string.index(char)
		alpha_idx = alpha_idx + key
#		alpha_idx = alpha_idx if alpha_idx<26 else alpha_idx-26
		alpha_idx %= 26
		string[idx] = alphabet_string[alpha_idx]
	
	return "".join(string)

if __name__ == "__main__":
	string = "xyz"
	key = 2
	gt = "zab"
	
	output = ceaserCipherEncryptor(string,key)
	
	print("The ground truth is: {}".format(gt))
	print("Your solution's output is: {}".format(output))
	print("---------------------------------")
