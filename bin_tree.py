class Node:
	def __init__(self, data):
		self.right = None
		self.left = None
		self.data = data

	def printTree(self):
		print(self.data)

root = Node(10)
root.printTree()