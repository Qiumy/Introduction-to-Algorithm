'''
	binary tree
'''

class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

def add(root, x):
	parent = None
	cur = root
	while cur:
		parent = cur
		if x < cur.val:
			cur = cur.left
		else:
			cur = cur.right
	if not parent:
		root = TreeNode(x)
	elif x < parent.val:
		parent.left = TreeNode(x)
	else:
		parent.right = TreeNode(x)

def preOrder_rec(root):
	if root == None:
		return
	print root.val,
	preOrder_rec(root.left)
	preOrder_rec(root.right)
	print

def inOrder_rec(root):
	if root == None:
		return
	inOrder_rec(root.left)
	print root.val,
	inOrder_rec(root.right)
	print

def postOrder_rec(root):
	if root == None:
		return
	postOrder_rec(root.left)
	postOrder_rec(root.right)
	print root.val,
	print

def preOrder(root):
	if root == None:
		return
	stack = [root]
	while stack:
		p = stack.pop()
		print p.val,
		if p.right:
			stack.append(p.right)
		if p.left:
			stack.append(p.left)
	print

def inOrder(root):
	if root == None:
		return
	p = root
	stack = []
	while p or stack:
		if p:
			stack.append(p)
			p = p.left
		else:
			p = stack.pop()
			print p.val,
			p = p.right
	print

def postOrder(root):
	if root == None:
		return
	stack = []
	cur = pre = None
	stack.append(root)
	while stack:
		cur = stack.top()
		if (cur.left == None and cur.right == None) or (pre and (pre == cur.left or pre == cur.right)):
			print cur.val,
			s.pop()
			pre = cur
		else:
			if cur.right: 
				s.append(cur.right)
			if cur.left: 
				s.append(cur.left)
	print

def isFound(root, key):
	if root == None:
		return False
	if root.val == key:
		return True
	elif key < root.val:
		return isFound(root.left, key)
	else:
		return isFound(root.right, key)

def minVal(root):
	if root == None:
		print "error: the tree is empty"
		return
	cur = root
	while cur.left:
		cur = cur.left
	return cur.val

def maxVal(root):
	if root == None:
		print "error: the tree is empty"
		return
	cur = root
	while cur.right:
		cur = cur.right
	return cur.val

# delete function to be modified
def delete(root, key):
	if not isFound(root, key):
		print "not found"
		return
	if root.val == key:
		root = deleteNode(root)	
	elif root.val > key:
		delete(root.left, key)
	else:
		delete(root.right, key)

def deleteNode(node):
	if node.left==None and node.right==None:
		node = None
	elif node.right==None:
		node = node.left
	elif node.left==None:
		node = node.right
	else:
		leftMax = maxVal(node.left)
		node.val = leftMax
		delete(node.left, leftMax)
	return node

def levelTraverse(root):
	if root == None:
		return
	stack = [root]
	while stack:
		p = stack.pop(0)
		print p.val,
		if p.left:
			stack.append(p.left)
		if p.right:
			stack.append(p.right)
	print

if __name__ == '__main__':
	tree = TreeNode(10)
	add(tree,3)
	add(tree,14)
	levelTraverse(tree)
	inOrder(tree)
	add(tree,6)
	add(tree,5)
	add(tree,7)
	levelTraverse(tree)
	delete(tree, 7) #wrong
	levelTraverse(tree)