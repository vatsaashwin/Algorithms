#Heaps: min or max order + complete binary tree



#Insert method:
#1. Add element to bottom level of the heap
#2. Compare added element to the parent, if they are in correct order: stop.
#3. If not, swap the element with its parent and return to step #2

#Extract/Delete method:
#1.Replace the root of the heap with the last element on the last level
#2. Compare the new root with its children; if they are in the correct order, stop
#3. If not, swap the element with one of its children and return to the previous step. 
#	(Swap with its smaller child in a min-heap and its larger child in a max-heap.)
