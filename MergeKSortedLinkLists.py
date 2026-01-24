# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
1. Edge Case - if lists is not there, just return None
2. Start with the second LinkedList in the input array, merge that with its previous one in array -> do this merge in a seperate helper function
3. Once thats merged, return a linked list
4. Use this list, pass it on to the function and just keep moving the index in the original array. 
"""
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        def merge(array, index):
            copy = array
            temp = ListNode(-1)
            second = temp
            copySecond = lists[index]
            while copy and copySecond:
                if copy.val <= copySecond.val:
                    second.next = copy
                    copy = copy.next
                else:
                    second.next = copySecond
                    copySecond = copySecond.next
                second = second.next
            if copy:
                second.next = copy
            if copySecond:
                second.next = copySecond
            return temp.next
        
        mergedArray = lists[0]
        ind = 1
        while ind < len(lists):
            currArray = merge(mergedArray, ind)
            mergedArray = currArray
            ind+=1
        return mergedArray
        
        



