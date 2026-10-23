# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def partition(self, head: ListNode | None, x: int) -> ListNode | None:
        # Dummy heads for both partitions
        less_dummy = ListNode(0)
        greater_dummy = ListNode(0)
        
        # Pointers to track current tails
        less_tail = less_dummy
        greater_tail = greater_dummy
        
        curr = head
        while curr:
            if curr.val < x:
                less_tail.next = curr
                less_tail = less_tail.next
            else:
                greater_tail.next = curr
                greater_tail = greater_tail.next
            curr = curr.next
            
        # Break any cycle by setting the end of greater list to None
        greater_tail.next = None
        
        # Connect the less list with the greater list
        less_tail.next = greater_dummy.next
        
        return less_dummy.next