import json
from main import classPhotos

with open("test_cases.json") as file:
	data = json.load(file)

total_test_cases = data["total_test_cases"]
total_test_cases_passed = 0

for i in range(1,total_test_cases+1):
	key="test_case_{}".format(i)
	test_case = data[key]
	
	output = classPhotos(test_case["redShirtHeights"],test_case["blueShirtHeights"])
	print("Your solution is: {}".format(output))
	print("The ground truth is: {}".format(test_case["output"]))
	print("------------------------")
	
	total_test_cases_passed += 1 if output == test_case["output"] else 0

print("{}/{} tests cases passed.".format(total_test_cases_passed,total_test_cases))
