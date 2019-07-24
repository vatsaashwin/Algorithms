import time

def knapsack(W, wt, val):

	n = len(val)

	#initialise
	table = [[0 for x in range(W+1)] for x in range(n+1)]
	 
	for i in range(n+1):
		for w in range(W+1):
			
			if i==0 or w==0:
				table[i][w] = 0

			elif wt[i-1] <= w:
				table[i][w] = max(val[i-1]+table[i-1][w-wt[i-1]], table[i-1][w])

			else:
				table[i][w] = table[i-1][w]

	return table[n][W]




#DP algorithm
print("Calculating by DP...")
start = time.time()
val = [60, 100, 120] 
wt = [10, 20, 30] 
W = 50
print(knapsack(W, wt, val)) 
stop= time.time()
timediff = stop-start
print("Time taken(*100000) by DP:", timediff)

