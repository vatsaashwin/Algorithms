
#function for insertion sort
def insertionSort(arr):
	for i in range(1, len(arr)):
		j = i-1
		while arr[j] > arr[j+1] and j >= 0:
			arr[j], arr[j+1] = arr[j+1], arr[j]
			j = j-1

#print input
arr= [5, 3, 2, 2, 1]
print("Input is: ", arr)

#call method
insertionSort(arr)

#print output
print("Output is: ", arr)
