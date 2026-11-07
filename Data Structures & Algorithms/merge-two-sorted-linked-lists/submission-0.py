# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        start = ListNode()
        to_add = start
        curr1 = list1
        curr2 = list2
        while curr1 or curr2:
            if curr1 and curr2:
                if curr1.val <= curr2.val:
                    to_add.next = curr1
                    temp = curr1
                    curr1 = curr1.next
                    temp.next = None
                    to_add = to_add.next
                else:
                    to_add.next = curr2
                    temp = curr2
                    curr2 = curr2.next
                    temp.next = None
                    to_add = to_add.next
            elif not curr1 and curr2:
                to_add.next = curr2
                curr1 = None
                curr2 = None
            else:
                to_add.next = curr1
                curr1 = None
                curr2 = None
        return start.next