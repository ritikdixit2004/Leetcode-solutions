# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
        if not head or left == right:
            return head

        dummy = ListNode(0, head)
        prev = dummy

        # 1. Advance `prev` to the node immediately before position `left`
        for _ in range(left - 1):
            prev = prev.next

        # `curr` will become the tail of the reversed sublist
        curr = prev.next

        # 2. Reverse nodes between `left` and `right` using head insertion
        for _ in range(right - left):
            temp = curr.next
            curr.next = temp.next
            temp.next = prev.next
            prev.next = temp

        return dummy.next