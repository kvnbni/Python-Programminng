#Given a string, find the length of the longest substring without repeating characters.

#Examples:

#Given "abcabcbb", the answer is "abc", which the length is 3.

#Given "bbbbb", the answer is "b", with the length of 1.

#Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        self.s=s
        word=list(s)
        length=len(word)
        if length==1:
            return 1
        elif length==0:
            return 0
        count=0
        count_no_repeat=0
        
        substring=""
        
        
        for i in range(0,length-1):
            
            substring=substring+word[i]
            
            sublist=list(substring)
            length_of_substring=len(sublist)
            for j in range(0,length_of_substring):
                
                if sublist[j]==word[i+1]:
                    if (len(sublist)>count):
                        count=len(sublist)
                        
                        substring=substring[j+1:]
                        break
                    else:
                        substring=substring[j+1:]
                        break
                else:
                    count_no_repeat=len(sublist)
                    if i==length-2 and j==length_of_substring-1:
                        count_no_repeat+=1
                        flag=1
                    
                    
            
            
        
        return max(count,count_no_repeat)
        
                    
            
            
        """
        :type s: str
        :rtype: int
        """
        
