# Write a function that takes two parameters n and k and returns the value of
# Binomial Coefficient C(n, k).

import time

def recursive_comb(n, k):
	if k==0 or k==n:
		return 1

	return recursive_comb(n-1, k-1)+recursive_comb(n-1, k)


def dp_comb(n, k):
	table = [0 for i in range(k+1)] 
	table[0] = 1

	for i in range(1, n+1):
		j = min(i, k)
		while j>0:

			table[j] = table[j]+ table[j-1]
			j-=1
	return table[k]



#Recursion
print("Calculating by recursion...")
start = time.time()
rec_answer = recursive_comb(5, 2)
stop= time.time()
timediff = stop-start
print("Result:", rec_answer)
print("Time taken(*100000) by recursion:", timediff*100000)


#DP algorithm
print("\nCalculating by DP...")
start = time.time()
dp_answer = dp_comb(5, 2)
stop= time.time()
timediff = stop-start
print("Result:", dp_answer)
print("Time taken(*100000) by DP algorithm:", timediff)

