#implementation using stack

class Stack():
	def __init__(self):
		self.items =[]

	def isEmpty(self):
		return self.items == []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def peek(self):
		return self.items[len(self.items)-1]

	def size(self):
		return len(self.items)

s= Stack()

a="[(])"

for i in range(len(a)-1):

	if s.isEmpty():
		s.push(a[i])

	if (s.peek()== '(' and a[i+1]== ')'):		
		print("peeked, equal, poppin")
		s.pop()

	elif (s.peek()== '[' and a[i+1]== ']'):		
		print("peeked, equal, poppin")
		s.pop()

	elif (s.peek()== '{' and a[i+1]== '}'):		
		print("peeked, equal, poppin")
		s.pop()

	else:
		print("peeked, unequal, pushin")
		s.push(a[i])


if s.isEmpty():
	print("Balanced")
else:
	print("Not Balanced")


