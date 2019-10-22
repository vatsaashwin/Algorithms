# Given a 32-bit signed integer, reverse digits of an integer.

class Solution:
    def reverse(self, x: int) -> int:
        if x>0:
            a = int(str(x)[::-1])
        if x<=0:                
            a = -1*int(str(x*-1)[::-1])
        
        if a in range(-2**31, (2**31)-1):
            return a
        else:
            return 0
            