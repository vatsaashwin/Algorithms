# Merge two sorted arrays:

# arr1 = [1, 2, 5, 9]
# arr2 = [3, 4, 8, 10, 18]

arr1 = [1, 3, 4, 5]
arr2 = [2, 4, 6, 8]

def mergeSortedArrays(a, b):
    m = len(a)
    n = len(b)
    c = [0]*(m+n)
    i=0
    j=0
    
    for k in range(m+n):
        if (i<m and j<n):
            if a[i] < b[j]:
                c[k] = a[i]
                i+=1
            else:
                c[k] = b[j]
                j+=1
        elif (i==m and j<n):
            c[k] = b[j]
            j+=1
            
        elif (i<m and j==n):
            c[k] = a[i]
            i+=1
        
        k+=1
    
    return c


            
m_arr=mergeSortedArrays(arr1, arr2)
print(m_arr)