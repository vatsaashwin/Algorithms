import time

def lis(A):

	n = len(A)

	table = [1]*n

	for i in range(1, n):
		for j in range(0, i):
			if A[i]>A[j] and table[i]<table[j]+1:
				table[i] = table[j]+1
	
	maximum = 0
	
	for i in range(n):
		maximum = max(maximum, table[i])

	return maximum


#DP algorithm
print("Calculating by DP...")
start = time.time()
arr = [10, 22, 9, 33, 21, 50, 41, 60] 
print("Length of lis is: ", lis(arr) )
stop= time.time()
timediff = stop-start
print("Time taken(*100000) by DP:", timediff)


