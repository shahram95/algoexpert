def tournamentWinner(competitions, results):
	score_dict = dict()
	
	for competition, result in zip(competitions,results):
		winner = competition[int(not(result))]
		score_dict[winner] = score_dict.get(winner,0)+3
	
	return max(score_dict, key=score_dict.get)

if __name__ == "__main__":
	competitions = [
			["HTML", "C#"],
			["C#", "Python"],
			["Python", "HTML"]]
	results = [0, 0, 1]
	gt = "Python"
	
	output = tournamentWinner(competitions, results)
	
	print("The ground truth is: {}".format(gt))
	print("Your solution result is: {}".format(output))
	print("--------------------------------------------")
