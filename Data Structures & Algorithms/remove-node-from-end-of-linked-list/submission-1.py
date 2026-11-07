# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        lens = self.lengths(head)
        
        curr = head
        start = head
        if lens - n == 0:
            start = head.next
        i = 0
        while i < lens - n - 1:
            i=i+1
            curr = curr.next 
       
        if lens - i < 2:
            curr.next = None
            return  None
        else:
            curr.next = curr.next.next
        return start
        
    def lengths(self, head: Optional[ListNode]) -> int:
        count = 0
        curr = head
        while curr is not None:
            count += 1
            curr = curr.next
        return count