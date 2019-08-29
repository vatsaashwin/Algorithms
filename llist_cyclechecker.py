
class Node(object):

	def __init__(self, value):
		self.value = value
		self.nextnode = None

#creating a cycle
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

a.nextnode = b
b.nextnode = a


def loopChecker(node):

	if node==None:
		return print("Nothing on the list")

	n1 = node
	n2 = node.nextnode

	while ((n2!=None and n2.nextnode != None) or (n1.nextnode!= None)):
		n1 = n1.nextnode
		n2 = n2.nextnode.nextnode

		if (n1 == n2):
			return print("cycle found")
			

loopChecker(a)


			


		 
