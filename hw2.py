
import random
import numpy as np
import matplotlib.pyplot as plt
import time
import sys
sys.setrecursionlimit(1000000)

def mergeSort(arr):
    if len(arr)>1:
        m = len(arr)//2

        left = arr[:m]
        right = arr[m:]
        #divide array into smallest units
        mergeSort(left)
        mergeSort(right)

        i=j=k=0

        while i <len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i+=1
            k+=1

        while j < len(right):
            arr[k] = right[j]
            j+=1
            k+=1

    return arr


def quickSort(arr):
    quickSort_rand(arr, 0, len(arr))
    return arr

def quickSort_rand(arr, left, right):
    if left < right:
        pivot = random.randint(left, right-1)

        arr[pivot], arr[left] = (arr[left], arr[pivot])

        pi = partition(arr, left, right)

        quickSort_rand(arr, left, pi)
        quickSort_rand(arr, pi+1, right)
    return arr

def partition(arr, li, ri):
    pivot = arr[li]
    i = li+1
    for j in range(li+1, ri):
        if arr[j] < pivot:
            arr[j], arr[i] = arr[i], arr[j]
            i += 1
    arr[li], arr[i-1] = arr[i-1], arr[li]
    return i-1

timems_rand = []
timeqs_rand = []
n = []

for i in range(0, 100):
    
    nums = np.random.randint(1, 100, i)
    n.append(len(nums))
    # nums = np.sort(nums)

    start = time.time()
    # print(randnums)
    mergeSort(nums)
    stop = time.time()
    timediff = stop-start
    timems_rand.append(timediff)
    
    startqs = time.time()
    quickSort(nums)
    stopqs = time.time()
    timediffqs = stopqs-startqs
    timeqs_rand.append(timediffqs)


plt.plot(n, timems_rand, 'r.', label='Merge Sort')
plt.plot(n, timeqs_rand, 'b.', label='Quick Sort')
plt.legend(loc='upper left')
plt.xlabel('Input Size(n)')
plt.ylabel('Runtime')
plt.title("Input size vs. Runtime")
plt.show()





    


    