#Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple #copies of the substring together. You may assume the given string consists of lowercase English letters only #and its length will not exceed 10000.

#Example 1:

#Input: "abab"

#Output: True

#Explanation: It's the substring "ab" twice.

#Example 2:

#Input: "aba"

#Output: False

#Example 3:

#Input: "abcabcabcabc"

#Output: True

#Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)





class Solution(object):
    def repeatedSubstringPattern(self, str):
        self.str=str
        length=len(str)
        for i in range(1,length/2+1):   # looping half the string to find substring as it can't be any bigger than this
            substring=str[0:i]          # substring which starts from the first charecter to half the string
            if substring==str[len(substring):len(substring)*2] :  # checking if substring equals the substring that makes up the entire string
                val = length / len(substring)   # determining the total number of substrings that make up the string
                substring=substring*(int(val))  # making a copy of the string using the determined substring
                if str==substring:              # check if match
                    return True
        return False
            

            
        """
        :type str: str
        :rtype: bool
        """

