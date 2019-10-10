#Heaps: min or max order + complete binary tree

# To traverse to a child of a node, in the array representing heap:
# 1) Current node at n: right child will be at 2n+1
#						left child will be at 2n-1

#Insert method:
#1. Add element to bottom level of the heap
#2. Compare added element to the parent, if they are in correct order: stop.
#3. If not, swap the element with its parent and return to step #2

#Extract/Delete method:
#1.Replace the root of the heap with the last element on the last level
#2. Compare the new root with its children; if they are in the correct order, stop
#3. If not, swap the element with one of its children and return to the previous step. 
#	(Swap with its smaller child in a min-heap and its larger child in a max-heap.)

class BinHeap:
	def __init__(self):
		self.heapList = [0]
		self.currentSize = 0

	# def percUp(self, i):
	# 	while i//2>0:
	# 		if self.heapList[i] < self.heapList[i//2]:
	# 			tmp = self.heapList[i//2]
	# 			self.heapList[i//2] = self.heapList[i]
	# 			self.heapList[i] = tmp
	# 		i = i//2

	# def insert(self, k)
	# 	self.heapList.append(k)
	# 	self.currentSize = self.currentSize + 1
	# 	self.percUp(self.currentSize)

	# def percDown(self, i):
	# 	while (i*2) <= self.currentSize:
	# 	mc = self.minChild(i)
	# 	if self.heapList[i] > self.heapList[mc]:
	# 	tmp = self.heapList[i]
	# 	self.heapList[i] = self.heapList[mc]
	# 	self.heapList[mc] = tmp

	
