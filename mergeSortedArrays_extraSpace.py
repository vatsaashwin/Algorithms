# ar1 = [1, 10]
# ar2 = [2, 3]

ar1= [1, 5, 9, 10, 15, 20]
ar2= [2, 3, 8, 13]

def mergeExtraSpace(ar1, ar2):
	m= len(ar1)
	n= len(ar2)
	temp = 0
	i=0
	j=0
	for i in range(m):
		if ar1[i]>ar2[j]:
			temp = ar1[i]
			ar1[i] = ar2[j]
			ar2[j] = temp
			print(ar1, ar2)

		for k in range(n-1):
			if ar2[k]>ar2[k+1]:
				temp = ar2[k]
				ar2[k] = ar2[k+1]
				ar2[k+1] = temp
				print("sorting in place",ar2)

	print(ar1, ar2)


print(mergeExtraSpace(ar1, ar2))