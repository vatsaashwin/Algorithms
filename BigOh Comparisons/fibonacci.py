import time

def recursive_fibonacci(num):
	# print(num)
	
	if num==0:
		return 0

	elif num==1:
		return 1

	elif num>=2:
		return recursive_fibonacci(num-1) + recursive_fibonacci(num-2)


memo = {}
def memoised_dp(num):
	if num in memo:
		return memo[num]

	if num <=1:
		f = num

	else:
		f = memoised_dp(num-1)+ memoised_dp(num-2)

	memo[num] = f
	return f


def dp_fib(num):
	fib = {}
	fib[0] = 0
	fib[1] = 1
	for i in range(2, num+1):
		fib[i] = fib[i-1]+fib[i-2]
	
	return fib[num]

#Recursion
print("Calculating by recursion...")
start = time.time()
rec_answer = recursive_fibonacci(40)
stop= time.time()
timediff = stop-start
print("Fibonacci number is:", rec_answer)
print("Time taken(*100000) by recursion:", timediff)


#Memoised DP algorithm
print("\nCalculating by memoised...")
start = time.time()
mem_answer = memoised_dp(40)
stop= time.time()
timediff = stop-start
print("Fibonacci number is:",  mem_answer)
print("Time taken(*100000) by Memoised DP algorithm:", timediff)

#DP algorithm
print("\nCalculating by DP...")
start = time.time()
fib = dp_fib(40)
stop= time.time()
timediff = stop-start
print("Fibonacci number is:",  fib)
print("Time taken(*100000) by Memoised DP algorithm:", timediff)

