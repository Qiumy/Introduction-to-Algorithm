'''
	stack
'''

class Stack:
	def __init__(self, size = 10):
		self.stack = []
		self.size = size
		self.top = -1

	def setSize(self, size):
		self.size = size

	def isEmpty(self):
		if self.top == -1:
			return True
		else:
			return False

	def top(self):
		if self.isEmpty():
			print "error: stack is empty"
			return
		else:
			return self.stack[self.top]

	def pop(self):
		if self.isEmpty():
			print "error: stack is empty"
			return
		else:
			self.top -= 1
			return self.stack.pop()

	def isFull(self):
		if self.top+1 == self.size:
			return True
		else:
			return False

	def push(self, x):
		if self.isFull():
			print "error: stack is full"
			return
		else:
			self.top += 1
			self.stack.append(x)

	def show(self):
		print self.stack

if __name__ == '__main__':
	s = Stack(3)
	s.push(1)
	s.push(2)
	s.push(3)
	s.show()
	s.pop()
	s.show()
	s.push(6)
	s.push(4)
