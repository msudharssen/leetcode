"""
1. If given in reverse order, just traverse each list, 
2. keep a carry, and calcuate the remainder + carry for each addition
3. start a new dummy node. add each remanider to this dummy node list, and move it to the 
4. Move each lists as well near the end of the while loop
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        prev = l1
        secondPrev = l2
        carry = 0
        res = ListNode(-1)
        toRet = res
        
        
        while prev or secondPrev or carry:
            val1 = prev.val if prev else 0
            val2 = secondPrev.val if secondPrev else 0
            total = val1 + val2 + carry
            carry = total // 10
            valToAdd = total % 10
            newNode = ListNode(valToAdd)
            res.next = newNode
            res = res.next
            prev = prev.next if prev else None
            secondPrev = secondPrev.next if secondPrev else None
        
        return toRet.next