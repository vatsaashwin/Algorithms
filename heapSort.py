# 1.  Implement Heap sort. (You could see pages 151--160 of CLRS for a description 
# and analysis, but note that the arrays are indexed starting with 1). 

# You write three routines, Maxheapify which heapifies the input array,
# BuildMaxHeap, which builds the MaxHeap and finally HeapSort, which
# sorts the input array. The testing program tests HeapSort which should
# use the other two.

def Maxheapify(arr, n, i):
	# n = len(arr)
	max = i
	left = 2*i + 1
	right = 2*i + 2

	if left < n and arr[i] < arr[left]:
			max = left

	if right < n and arr[max] < arr[right]:
			max = right

	if max != i:
		arr[i], arr[max] = arr[max], arr[i]
		Maxheapify(arr, n, max)
		

def BuildMaxHeap(arr):
	#given an array, exchange elements so that the heap property is satisfied
	#we assume that the rest of the nodes are all leaves
	n = len(arr)
	for i in range (n//2-1, -1, -1):
		Maxheapify(arr, n, i)
	

def HeapSort(arr):
	#build the array into a max heap first
	BuildMaxHeap(arr)
	n = len(arr)

	#now the array has the highest number at root of max heap
	for i in range(n-1, 0, -1):
		#we exchange the last node with the root and cut it out of our unsorted array
		arr[i], arr[0] = arr[0], arr[i]
		#then again create a max heap out of the remaining unsorted array
		Maxheapify(arr, i, 0)
	return arr

arr = [5,6,7,1,2,3,5,6,7,3,2,1,5,6,7,3,2,44,33,11]
print(HeapSort(arr))
