# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return

        # Step 1: Find the middle of the linked list
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse the second half of the list
        # 'slow.next' is the start of the second half
        second = slow.next
        slow.next = None # Split the list into two halves
        prev = None
        
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # Step 3: Merge the two halves alternately
        # 'head' is the start of the first half, 'prev' is the start of the reversed second half
        first, second = head, prev
        while second:
            # Store next pointers
            tmp1, tmp2 = first.next, second.next
            
            # Link the nodes together
            first.next = second
            second.next = tmp1
            
            # Move forward in both halves
            first = tmp1
            second = tmp2