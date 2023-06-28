import json
from main import getNthFib

with open("test_cases.json") as file:
	data = json.load(file)

total_test_cases = data["total_test_cases"]
total_test_cases_passed = 0

for i in range(1,total_test_cases+1):
	key="test_case_{}".format(i)
	test_case = data[key]
	
	output = getNthFib(test_case["n"])
	print("Your solution is: {}".format(output))
	print("The ground truth is: {}".format(test_case["output"]))
	
	
	total_test_cases_passed += 1 if output == test_case["output"] else 0
	pf_str = "Passed" if output == test_case["output"] else "Failed"
	print("Test case {}: {}".format(i, pf_str))
	print("------------------------")
	
print("{}/{} tests cases passed.".format(total_test_cases_passed,total_test_cases))
