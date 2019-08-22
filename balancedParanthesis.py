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

def balanceChecker(a):
	for i in range(len(a)-1):

		if s.isEmpty():
			s.push(a[i])

		if (s.peek()== '(' and a[i+1]== ')'):
			s.pop()

		elif (s.peek()== '[' and a[i+1]== ']'):		
			s.pop()

		elif (s.peek()== '{' and a[i+1]== '}'):		
			s.pop()

		else:
			s.push(a[i])


	if s.isEmpty():
		return print("Balanced")
	else:
		return print("Not Balanced")

a= "(()[{()((()[))]()}()}"
balanceChecker(a)
