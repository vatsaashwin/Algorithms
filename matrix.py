# Change all elements of row i and column j in a matrix to 0 if cell (i, j) has value 0
arr = [[0,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print(arr)

def changeVal(arr, r, c):
	rows= len(arr)
	cols = len(arr[0])

	if arr[r][c] == 0:
		for i in range(rows):

			arr[i][c]=0
			for j in range(cols):
				arr[r][j]=0

	print(arr)


changeVal(arr, 0, 0)
