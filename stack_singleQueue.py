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
		self.q= Queue()
	
	def push(self, item):
		# self.items.append(item)
		if self.q.isEmpty():
			self.q.enqueue(item)
		else:
			self.q.enqueue(item)
			for i in range(self.q.size()-1):
				self.q.enqueue(self.q.dequeue())

	def pop(self):
		return self.q.dequeue()


q= Queue()

s= Stack()

s.push(1)
s.push(2)
print(s.pop())
print(s.pop())
