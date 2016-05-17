'''
	queue.py
'''

class Queue:
	def __init__(self, size=10):
		self.queue = []
		self.size = size
		self.head = 0
		self.tail = 0

	def isEmpty(self):
		return self.tail == 0

	def isFull(self):
		if (self.tail - self.head) == self.size:
			return True
		else:
			return False

	def frist(self):
		if self.isEmpty():
			print "error: queue is empty"
			return
		else:
			return self.queue[self.head]

	def last(self):
		if self.isEmpty():
			print "error: queue is empty"
			return
		else:
			return self.queue[self.tail-1]

	def enqueue(self, x):
		if self.isFull():
			print "error: queue is full"
			return
		else:
			self.tail += 1
			self.queue.append(x)

	def dequeue(self):
		if self.isEmpty():
			print "erroe: queue is empty"
			return
		else:
			self.tail -= 1
			return self.queue.pop(0)

	def show(self):
		print self.queue

if __name__ == '__main__':
	q = Queue(3)
	q.enqueue(1)
	q.enqueue(2)
	q.enqueue(3)
	q.enqueue(4)
	q.show()
	q.dequeue()
	q.show()