'''
red black tree
'''

class TreeNode:
	def __init__(self, data):
		self.left = None
		self.right = None
		self.parent = None
		self.data = data
		self.color = 'red' 
		#初始化为red而不是balck看第5条黑高变化不好调节，而red要好些

	def createNode(self, data):
		return TreeNode(data)

	def left_rotate(self, root):
		'''
		围绕self转root根结点
		'''
		x = self
		y = x.right

		if y == None:
			return
		b = y.left
		# x and b
		x.right = b
		if b != None:
			b.parent = x
		# y and x.parent
		y.parent = x.parent
		if x.parent == None:
			root = y
		elif x == x.parent.left:
			x.parent.left = y
		else:
			x.parent.right = y
		# x and y
		y.left = x
		x.parent = y

	def right_rotate(self, root):
		'''
		围绕self转root根结点
		'''
		y = self
		x = y.left

		if x == None:
			return
		b = x.right
		# y and b
		y.left = b
		if b != None:
			b.parent = y
		# x and y.parent
		x.parent = y.parent
		if y.parent == None:
			root = x
		elif y == y.parent.left:
			y.parent.left = x
		else:
			y.parent.right = x
		# x and y
		x.right = y
		y.parent = x

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

		insertNode = self.createNode(data) # red initial
		if data < cur.data:
			cur.left = insertNode
			cur.left.parent = cur
		else:
			cur.right = insertNode
			cur.right.parent = cur

		insertNode.re_insert_fixup(self) # maintian the feature
		return insertNode

	def re_insert_fixup(self, root):
		z = self

		while z.parent != None and z.parent.color == 'red': #如果有父亲结点且他为红色
			if z.parent == z.parent.parent.left:
				y = z.parent.parent.right   #y是z的叔父
				if y.color == 'red':        #case 1
					z.parent.color = 'black'
					y.color = 'black'
					z.parent.parent.color = 'red'
					z = z.parent.parent
				else:
					if z == z.parent.right: #case 2 --->case3
						z = z.parent
						z.right_rotate(root)
					z.parent.color = 'black'
					z.parent.parent.color = 'red'
					z.parent.parent.right_rotate(root)
			else:
				y = z.parent.parent.left   #y是z的叔父
				if y.color == 'red':        #case 1
					z.parent.color = 'black'
					y.color = 'black'
					z.parent.parent = 'red'
					z = z.parent.parent
				else:
					if z == z.parent.left: #case 2 --->case3
						z = z.parent
						z.left_rotate(root)
					z.parent.color = 'black'
					z.parent.parent.color = 'red'
					z.parent.parent.left_rotate(root)

		root.color = 'black'