
# Given index of an opening parenthesis in sentence, this function returns the index of the
# corresponding closing parenthesis
def match(sentence, index):

	left_count = 0 

	for position in xrange(index + 1, len(sentence)):

		char = sentence[position]

		if char == '(':
			left_count += 1
		elif char == ')':

			if (left_count == 0):
				return position
			else:	
				left_count -= 1
		
	return 'No closing parenthesis'

# test code
sentence = '(abc(def))'
result = match(sentence,0)
print result
result = match(sentence,4)
print result
sentence = 'ab(cd(ef)g'
result = match(sentence,2)
print result

#ouput:
# 9 
# 8
# No closing parenthesis
