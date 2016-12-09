##Given an array of integers, return indices of the two numbers such that they add up to a specific target.
##You may assume that each input would have exactly one solution.
##Example:
##Given nums = [2, 7, 11, 15], target = 9,
##Because nums[0] + nums[1] = 2 + 7 = 9,
##return [0, 1].


class Solution(object):
    def twoSum(self, nums, target):
        self.nums=nums
        self.target=target
        placeholder=[]
	k=0
        for i in range(0,len(nums)):
            for j in range (i+1,len(nums)):
                 sum=nums[i]+nums[j]
                 if(sum==target):
                     placeholder.extend([i,j])
		     
                     break
        return placeholder

sol1=Solution()
answer=sol1.twoSum([1,3,5,7],8)
print answer
