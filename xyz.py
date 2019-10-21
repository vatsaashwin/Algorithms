# class Solution:
def twoSumBruteForce(nums, target):
    for i in range(0, len(nums)-1):
    	for j in range(i+1,len(nums)):
    		if (nums[i] + nums[j] == target):
        		return [i, j]


def twoSumHash(nums, target):
	complementMap= dict()
	for i in range(len(nums)):
		num = nums[i]
		complement = target - num
		# print(complementMap)
		if num in complementMap:
			return [complementMap[num], i]
		else:
			complementMap[complement] = i

nums = [3, 2, 4]
# nums = [15, 1, 9, 4, 29]
target = 6

print(twoSumBruteForce(nums, target))
print(twoSumHash(nums, target))