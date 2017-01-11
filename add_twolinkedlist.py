#You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

#You may assume the two numbers do not contain any leading zero, except the number 0 itself.

#Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
#Output: 7 -> 0 -> 8
        
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        self.l1=l1
        self.l2=l2
        data=self.sum(l1,l2)
        print data
        head=None
        for i in reversed(data):
            l3=ListNode(i)
            l3.next=head
            head=l3
        return l3
        
    def length(self,l):
        self.l=l
        current=l.next
        count=1
        while current:
            count+=1
            current=current.next
        return count
        
    def sum(self,l1,l2):
        self.l1=l1
        self.l2=l2
        data=[]
        len_l1=self.length(l1)
        len_l2=self.length(l2)
        tens=0
        
        while l1 or l2:
            if l1==None:
            	l1=ListNode(0)
            if l2==None:
                l2=ListNode(0)
            sum1=l1.val+l2.val
            unit1=sum1%10
            if unit1+tens>=10:
                data.append((unit1+tens)%10)
                tens=(unit1+tens)/10
            else:    
                data.append(unit1+tens)
                tens=sum1/10
            l1=l1.next
            l2=l2.next
            if l1==None and l2==None and tens!=0:
                data.append(tens)
        
        return data
        

        
        
        
            
        
        
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
