#! /usr/bin/env python3

# data tree

class Tree:

	def __init__(self, data):
		self.data = data
		self.right = None
		self.left = None

	def addNode(self, data):

		if (self.data):
			
			if (self.left is None):
				self.left = Tree(data)

			elif (self.left and self.right):
				self.left.addNode(data)

			elif (self.right is None):
				self.right = Tree(data)
			
			elif (self.right):
				self.right.addNode(data)

		else:
			self.data = data

t = Tree(1)
t.addNode(11)
t.addNode(22)

t.addNode(111)
t.addNode(112)

t.addNode(221)
t.addNode(222)

print(t.left.data)
print(t.left.left.data)
print(t.left.right.data)

print(t.right.data)
print(t.right.left.data)
