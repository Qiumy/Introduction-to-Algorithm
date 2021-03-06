'''
search tree
'''

class TreeNode:
	def __init__(self, data):
		self.left = None
		self.right = None
		self.parent = None
		self.data = data

	def createNode(self, data):
		return TreeNode(data)

	def inOrder(self):
		if self.left:
			self.left.inOrder()
		print self.data,
		if self.right:
			self.right.inOrder()

	def tree_search(self, data):
		if self==None or self.data==data:
			return self
		if data < self.data and self.left:
			return self.left.tree_search(data)
		elif data >= self.data and self.right:
			return self.right.tree_search(data)

	def iterative_tree_search(self, data):
		cur = self
		while cur != None and data != cur.data:
			if data < cur.data:
				cur = cur.left
			else:
				cur = cur.right
		return cur

	def tree_minimum(self):
		if self.left:
			return self.left.tree_minimum()
		else:
			return self

	def tree_maximum(self):
		if self.right:
			return self.right.tree_maximum()
		else:
			return self

	def tree_successor(self):
		cur = self
		if cur.right != None:
			return cur.right.tree_minimum()
		else:
			p = cur.parent
			while p and p.right == cur:
				cur = p
				p = p.parent
			return p

	def tree_predecessor(self):
		cur = self
		if cur.left != None:
			return cur.left.tree_maximum()
		else:
			p = cur.parent
			while p and p.left == cur:
				cur = p
				p = p.parent
			return p

	def tree_insert(self, data):
		cur = self
		while cur:
			if data < cur.data:
				next_node = cur.left
			else:
				next_node = cur.right
			if next_node:
				cur = next_node
			else:
				break

		t_node = self.createNode(data)
		if data < cur.data:
			cur.left = t_node
			cur.left.parent = cur
		else:
			cur.right = t_node
			cur.right.parent = cur
		return t_node

	def tree_delete(self, root):
		cur = self
		if cur.left == None or cur.right == None:
			y = cur
		else:
			y = cur.tree_successor()

		if y.left == None:
			x = y.right
		else:
			x = y.left

		if x != None:
			x.parent = y.parent

		if y.parent == None:
			root = x
		elif y == y.parent.left:
			y.parent.left = x
		else:
			y.parent.right = x

		if y != cur:
			cur.data = y.data
		return root

if __name__ == '__main__':
	root = TreeNode(6)
	root.tree_insert(5)
	root.tree_insert(7)
	root.tree_insert(2)
	root.tree_insert(3)
	root.tree_insert(8)
	root.inOrder()
	print
	test = root.tree_search(2)
	print test
	test.tree_delete(root)
	root.inOrder()