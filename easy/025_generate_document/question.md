## Generate Document

You are given a string of available characters and a string representing a document that you need to generate. Write a function that determines if you can generate the document using the available characters. If you can generate the document, your function should return *true*; otherwise, it should return *false*.

You are only able to generate the document if the frequency of unique characters in the characters string is greater than or equal to the frequency of unique characters string. For example, if you are given *characters = "abcabc"* and *document = "aabbccc"* you cannot generate the document because you are missing one *c*.

The document that you need to create may contain any characters, including special characters, capital letters, numbers, and spaces. 

Note: You can always generate the empty string ("").

''' Sample Input
characters = "Bste!hetsi ogEAxpelrt x "
document = "AlgoExpert is the Best!"
'''

''' Sample Output
output = True
'''
