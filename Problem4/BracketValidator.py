from StackModule import Stack

# This function checks if input_string's openers and closers are properly nested
def check(input_string):

	stack = Stack()

	for char in input_string:

		if char == '{' or char == '(' or char == '[':

			stack.push(char)

		elif char == '}':

			if stack.peek() != '{':
				return False
			else:
				stack.pop()

		elif char == ')':

			if stack.peek() != '(':
				return False
			else:
				stack.pop()


		elif char == ']':

			if stack.peek() != '[':
				return False
			else:
				stack.pop()

	return stack.peek() == None

# test code
s = '{ab(cd)ef[gh]ij}'
result = check(s)
print result
# True

s = '{a[b(c]d)e'
result = check(s)
print result
# False

s = ''
result = check(s)
print result
# True

s = '{ab[cd}'
result = check(s)
print result
# False
