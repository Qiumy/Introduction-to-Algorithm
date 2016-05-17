'''
	single linked list
'''

class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class SingleLinkedList:
	def __init__(self):
		self._head = None

	def isEmpty(self):
		return self._head == None

	def size(self):
		cur = self._head
		cnt = 0
		while cur:
			cnt += 1
			cur = cur.next
		return cnt
	def add(self, x):
		'''
		insert x before head
		'''
		tmp = ListNode(x)
		tmp.next = self._head
		self._head = tmp

	def append(self, x):
		'''
		append x at the tail
		'''
		tmp = ListNode(x)
		if self.isEmpty():
			self._head = tmp
		else:
			cur = self._head
			while cur.next:
				cur = cur.next
			cur.next = tmp

	def isFound(self, x):
		cur = self._head
		while cur:
			if cur.val == x:
				return True
			cur = cur.next
		return False

	def index(self, x):
		cur = self._head
		cnt = 0
		while cur:
			if cur.val == x:
				return cnt
			cur = cur.next
			cnt += 1
		return -1

	def remove(self, x):
		cur = self._head
		pre = None
		while cur:
			if cur.val == x:
				if not pre:
					self._head = cur.next
				else:
					pre.next = cur.next
				break
			else:
				pre = cur
				cur = cur.next

	def insert(self, pos, x):
		if pos == self.size():
			self.append(x)
		elif pos > self.size():
			print "error: pos is out of index"
		elif pos == 0:
			self.add(x)
		else:
			tmp = ListNode(x)
			cnt = 1
			cur = self._head
			while cnt < pos:
				cur = cur.next
				cnt += 1
			cur.next, tmp.next = tmp, cur.next

	def show(self):
		cur = self._head
		while cur:
			print cur.val,
			cur = cur.next
		print

if __name__ == '__main__':
	l = SingleLinkedList()
	l.append(1)
	l.append(2)
	l.append(3)
	l.show()
	print l.size()
	l.remove(2)
	l.show()
			