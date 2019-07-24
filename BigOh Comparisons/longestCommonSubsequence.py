import time

def lcm(x, y):

	m = len(x)
	n = len(y)
	# declaring the array for storing the dp values 
	table = [[None]*(n+1) for i in range(m+1)] 

	for i in range(m+1):
		for j in range(n+1):

			if i==0 or j==0:
				table[i][j]=0
			elif x[i-1] == y[j-1]:
				table[i][j] = table[i-1][j-1]+1
			else:
				table[i][j] = max(table[i-1][j], table[i][j-1]) 

	return table[m][n]


#DP algorithm
print("Calculating by DP...")
start = time.time()
a = "AGGTABN"
b = "GXTXAYBD"
longestcommonsub = lcm(a,b)
stop= time.time()
timediff = stop-start
print("Length of LCM is:", longestcommonsub)
print("Time taken(*100000) by DP:", timediff)


