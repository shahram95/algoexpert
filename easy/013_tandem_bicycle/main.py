def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
	redShirtSpeeds.sort()
	blueShirtSpeeds.sort()
	total_speed = 0
	
	if not fastest:
		redShirtSpeeds.sort(reverse=True)
	
	for idx in range(len(redShirtSpeeds)):
		rider1 = redShirtSpeeds[idx]
		rider2 = blueShirtSpeeds[len(blueShirtSpeeds)-idx-1]
		total_speed += max(rider1, rider2)
	
	return total_speed
	
if __name__ == "__main__":
	redShirtSpeeds = [5, 5, 3, 9, 2]
	blueShirtSpeeds = [3, 6, 7, 2, 1]
	fastest = True
	gt = 32
	
	output = tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest)
	
	print("The ground truth is: {}".format(gt))
	print("Your solution output is: {}".format(output))
	print("-----------------------------------------")
