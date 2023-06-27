def classPhotos(redShirtHeights, blueShirtHeights):
	redShirtHeights.sort(reverse=True)
	blueShirtHeights.sort(reverse=True)
	
	front_row = "RED" if redShirtHeights[0] < blueShirtHeights[0] else "BLUE"
	
	for idx in range(len(redShirtHeights)):
		redShirtHeight = redShirtHeights[idx]
		blueShirtHeight = blueShirtHeights[idx]
		
		if front_row == "RED":
			if redShirtHeight >= blueShirtHeight:
				return False
		
		else:
			if blueShirtHeight >= redShirtHeight:
				return False
		
	return True

if __name__ == "__main__":
	redShirtHeights = [5, 8, 1, 3, 4]
	blueShirtHeights = [6, 9, 2, 4, 5]
	gt = True
	
	output = classPhotos(redShirtHeights, blueShirtHeights)
	
	print("The ground truth is: {}".format(gt))
	print("Your solution output is: {}".format(output))
	print("---------------------------------------------")
