class Queue(object):

	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def enqueue(self, item):
		self.items.insert(0, item)

	def dequeue(self):
		return self.items.pop()

	def size(self):
		return len(self.items)

class Stack():
	def __init__(self):
		self.q1= Queue()
		self.q2= Queue()
	
	def push(self, item):
		# self.items.append(item)

		self.q2.enqueue(item)
		while (self.q1.isEmpty()==False):
			self.q2.enqueue(self.q1.dequeue())
		temp = self.q1
		self.q1=self.q2
		self.q2 = temp

	def pop(self):
		return self.q1.dequeue()


q= Queue()

s= Stack()

s.push(1)
s.push(2)
print(s.pop())
print(s.pop())
