Problem: Openers and Closers Validator

Problem Definition:
Given an input string, check if the openers and closers are properly nested.
‘{’, ‘(’, ’[’ are openers.
‘}’, ’)’, ’]’ are closers.
Example: 
‘{[]}’ should return True.
‘{(]}’ should return False.

Solution:
In BracketValidator.py, check(input_string) solves the problem in O(n) time and space.