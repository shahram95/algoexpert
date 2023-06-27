#!/bin/bash -e

FLD_NAME=$1

mkdir ${FLD_NAME}
touch ${FLD_NAME}"/main.py"
touch ${FLD_NAME}"/question.md"
touch ${FLD_NAME}"/test_cases.json"
cp -r 000_two_number_sum"/test_case.py" ${FLD_NAME}/ 
