# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lst = []
        curr = head
        while curr is not None:
            lst.append(curr.val)
            curr = curr.next

        lst = lst[::-1]
        if lst == []:
            return None
        new = ListNode()
        hold = new
        for i in range(len(lst)):
            hold.val = lst[i]
            if i == len(lst) - 1:
                hold.next = None
            else:
                hold.next = ListNode()
            hold = hold.next
        return new