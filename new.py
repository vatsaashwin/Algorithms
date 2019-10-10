import time

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
    n = len(arr)
    qs_end(arr, 0, n-1)
    return arr

def qs_end(arr, start, end):
    if start <end:
        pi = partition(arr, start, end)
        qs_end(arr, start, pi-1)
        qs_end(arr, pi+1, end)
    return arr

def partition(arr, start, end):
    i = start-1
    pivot = arr[end]

    for j in range(start, end):
        if arr[j] < pivot:
            i +=1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[end] = arr[end], arr[i+1]
    return i+1
  


arr= [5,4,2,8,9,5,2,1]
print(mergeSort(arr))
print(quickSort(arr))


