from StackModule import Stack

class Queue():

	def __init__(self):
		self.inStack = Stack()
		self.outStack = Stack()

	def enqueue(self, item):
		self.inStack.push(item)

	def dequeue(self):

		if self.outStack.peek() != None:
			return self.outStack.pop()
		elif self.inStack.peek() == None:
			return None
		else:

			while self.inStack.peek() != None:
				item = self.inStack.pop()
				self.outStack.push(item)

			return self.outStack.pop()

# test code

q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print q.dequeue()
q.enqueue(40)
q.enqueue(50)
print q.dequeue()
print q.dequeue()
print q.dequeue()
print q.dequeue()

# output:
# 10
# 20
# 30
# 40
# 50
