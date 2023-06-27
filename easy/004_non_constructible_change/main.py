def nonConstructibleChange(coins):
	coins.sort()
	currChange = 0
	
	for coin in coins:
		if coin > currChange+1:
			return currChange+1
		currChange += coin
	
	return currChange+1

if __name__ == "__main__":
	coins = [5, 7, 1, 1, 2, 3, 22]
	gt = 20
	output = nonConstructibleChange(coins)
	
	print("The ground truth is: {}".format(gt))
	print("Your solution output is: {}".format(output))
	print("----------------------------")
