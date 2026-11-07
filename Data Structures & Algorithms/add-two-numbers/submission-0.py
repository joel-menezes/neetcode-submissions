# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        l1r = self.reverse(l1)
        l2r = self.reverse(l2)

        l1n = self.to_num(l1r)
        l2n = self.to_num(l2r)
        print(l1n, l2n)

        tn = self.to_nodes(l1n + l2n)

        return self.reverse(tn)

    def reverse(self, head: ListNode) -> ListNode:
        curr = head
        start = None
        while curr:
            new = ListNode(curr.val)
            start, new.next = new, start
            curr = curr.next
        return start 
    
    def to_num(self, head: ListNode) -> int:
        curr = head
        count = 0
        while curr:
            count *= 10
            count += curr.val
            curr = curr.next
        return count
    
    def to_nodes(self, n: int) -> ListNode:
        start = None
        if n == 0:
            return ListNode(0)
        while n != 0:
            new = ListNode(n % 10)
            n //= 10
            new.next = start
            start = new
        return start