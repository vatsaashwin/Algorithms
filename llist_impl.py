#singly linked list implementation
#Access element in llist: O(k) to access kth element, 
#but constant time insertion/deletion

#Note: that array only take constant time to access an element
#but O(n) time insertion/deletion

#singly linked list
class Node(object):

	def __init__(self, value):
		self.value = value
		self.nextnode = None


a= Node(1)
b=Node(2)
c= Node(3)

a.nextnode = b
b.nextnode = c
# print(a.value)

print(b.nextnode.value)


