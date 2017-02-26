Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:

Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.

Example 2:

Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

Note: The length of the given binary array will not exceed 50,000. 

Solution:

class Solution(object):
    def findMaxLength(self, nums):
        count=0
        maximum_length=0
        table={0:0}  #{count:index}
        
        for index,num in enumerate(nums,1): #index of the nums array starts from 1 instead of 0
            if num==0:
                count-=1
            else:
                count+=1
                
            if count in table:
                maximum_length=max( maximum_length,index-table[count])
            else:
                table[count]=index
                
        return maximum_length
            
        """
        :type nums: List[int]
        :rtype: int
        """
