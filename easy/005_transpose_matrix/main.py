def transposeMatrix(matrix):
	numRows = len(matrix)
	numCols = len(matrix[0])
	
	matrixT = [[0 for _ in range(numRows)] for _ in range(numCols)]
	
	for i in range(numRows):
		for j in range(numCols):
			matrixT[j][i] = matrix[i][j]
	
	return matrixT

if __name__=="__main__":
	matrix = [[1, 2]]
	gt = [ [1], [2] ]
	output = transposeMatrix(matrix)
	print("The ground truth is: {}".format(gt))
	print("Your solution output is: {}".format(output))
