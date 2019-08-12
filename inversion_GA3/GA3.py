import numpy as np
import time
import matplotlib.pyplot as plt


def brute_count(A):
    count=0
    for i in range(0,len(A)):
        for j in range(i,len(A)):
            if A[i]>A[j]:
                count+=1
    return count

def generateArrays(i, n, s):
    arr = [];
    while i<=n:
        randArr = np.random.randint(-100, 100, i)
        arr.append(randArr.tolist())
        i+=s         
    return arr
        
def mergecount_inversion(lst):
    if len(lst) <= 1:
        return lst, 0
    middle = int( len(lst) / 2 )
    left, a = mergecount_inversion(lst[:middle])
    right, b = mergecount_inversion(lst[middle:])
    res, c = merge(left, right)
    return res, (a + b + c)

def merge(left, right):
    res = []
    count = 0
    i, j = 0, 0
    left_len = len(left)
    while i < left_len and j < len(right):
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            count += left_len - i
            j += 1
    res += left[i:]
    res += right[j:]
    return res, count        


def randarr_experiment(start, stop, step):
	i=0
	alist = []
	addtime1 = []
	addtime2=[]
	for t in range(10):
	    timeArr_bf=[]
	    timeArr_ms=[]
	    print("\nFor Iter:", t)
	    alist = generateArrays(start, stop, step) 
	    for i in range(len(alist)):

	        # Brute Force Method
	        startTime = time.clock()
	        calc = brute_count(alist[i])
	        endTime = time.clock()
	        timediff = endTime-startTime
	        timeArr_bf.append(timediff)

	        print("Brute Force:: For array size = %d in time %f"%(len(alist[i]), timediff))

	        # Divide-and-conquer
	        startTime = time.clock()
	        calc = mergecount_inversion(alist[i])
	        endTime = time.clock()
	        timediff = endTime-startTime
	        timeArr_ms.append(timediff)  

	        print("Divide-and-conquer:: For array size = %d in time %f"%(len(alist[i]), timediff))

	        i += 1
	    t += 1

	    #appending time taken to the addtime list
	    addtime1.append((timeArr_bf))
	    addtime2.append((timeArr_ms))

	#Taking average of time taken by all the iterations
	bf_time= [sum(x)/10 for x in zip(*addtime1)]

	ms_time = [sum(x)/10 for x in zip(*addtime2)]

	return bf_time, ms_time



if __name__ == '__main__':
	
	input_array_1 = [1,9,6,4,5]
	input_array_2 = [2,4,1,3,5]
	input_array_3 = [1,2,3,4,5,6]

	print("*****   BRUTE-FORCE     *****")
	print("inversion count", brute_count(input_array_1))
	print("inversion count", brute_count(input_array_2))
	print("inversion count", brute_count(input_array_3))


	print("\n*****   DIVIDE-AND-CONQUER     *****")
	print("inversion count", mergecount_inversion(input_array_1))
	print("inversion count", mergecount_inversion(input_array_2))
	print("inversion count", mergecount_inversion(input_array_3))


	print("\n*****   (Random Arrays)     *****")

	bf_time1, ms_time1= randarr_experiment(100, 900, 100) 
	bf_time2, ms_time2= randarr_experiment(1000, 9000, 1000) 

	ttime_bf= bf_time1+bf_time2
	ttime_ms= ms_time1+ms_time2


	# imput sizes from 100-900 and then 1000-9000
	x = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000]

	# blue for brute-force approach and green for divide and conquer
	plt.plot(x, ttime_bf, 'b-', ttime_ms, 'g-')
	plt.xlabel('Input Size(100-900, 1000-9000)')
	plt.ylabel('Average Runtime')
	plt.title('Input size vs. avg. runtime')
	plt.show()





