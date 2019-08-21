#TC: Logn

arr = [2, 8, 16, 22, 25, 89, 99, 100, 109, 999, 1200]
f = 999

def binarySearch(arr, f , s, d):
	
	mid = (d+s)//2
	# print(arr[mid])

	if arr[mid] == f:
		return mid

	elif arr[mid] > f:
		return binarySearch(arr, f, s, mid)


	elif arr[mid] < f:
		 return binarySearch(arr, f, mid+1, d)
		 
print("The position of the element is: ", binarySearch(arr, f, 0, len(arr)-1))




