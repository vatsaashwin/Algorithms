import time
import math
import matplotlib.pyplot as plt



def factoring(num):
    i = 2
    output = []
    
    while i <= math.sqrt(num):
        if num % i == 0:
            num = num // i
            output.append(i)
        else:
            i += 1
            
    output.append(num)
    
    return output

startTime = time.clock()
factoring(2134787561)
endTime = time.clock()
timeDiff = endTime - startTime
print(timeDiff)