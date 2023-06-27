def minimumWaitingTime(queries):
	minimumWaitTime = 0
	queries.sort()
	
	for idx, query in enumerate(queries):
		queries_left = len(queries) - (idx+1)
		minimumWaitTime += queries_left*query
	
	return minimumWaitTime
	
if __name__ == "__main__":
	queries = [3, 2, 1, 2, 6]
	gt = 17
	output = minimumWaitingTime(queries)
	
	print("The ground truth is: {}".format(gt))
	print("Your solution output is: {}".format(output))
