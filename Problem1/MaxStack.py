from StackModule import Stack

class MaxStack():

	def __init__(self):
		self.stack = Stack()
		self.maxes = Stack()

	def push(self, item):

		self.stack.push(item)

		if self.maxes.peek() == None:
			self.maxes.push(item)
		elif item >= self.maxes.peek():
			self.maxes.push(item)

	def pop(self):

		item = self.stack.pop()

		if item == None:
			return None
		elif item == self.maxes.peek():
			self.maxes.pop()

	def peek(self):
		return self.stack.peek()

	def getMax(self):
		return self.maxes.peek()

# test code
stack = MaxStack()
stack.push(10)
stack.push(9)
stack.push(8)
stack.push(20)
stack.push(15)
print stack.getMax()
stack.pop()
stack.pop()
print stack.getMax()
print stack.peek()

# output:
# 20
# 10
# 8
