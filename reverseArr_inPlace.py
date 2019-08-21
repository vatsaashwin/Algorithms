
# TC: O(n)

arr = [5, 9, 9, 2, 3]


def reverseArray(arr):
	alen = len(arr)
	for i in range(alen//2):
		temp = arr[i]
		arr[i] = arr[alen-i-1]
		arr[alen-i-1] = temp

	print(arr)
	return arr

reverseArray(arr)


