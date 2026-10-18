# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:

  def insertionSortList(self, head: ListNode | None) -> ListNode | None:
    if not head or not head.next:
      return head

    # Dummy node pointing to the head of the sorted list
    dummy = ListNode(0)
    dummy.next = head

    curr = head.next
    last_sorted = head  # Tail of the sorted part

    while curr:
      # If the current node is already in order relative to the sorted tail, simply advance
      if last_sorted.val <= curr.val:
        last_sorted = curr
      else:
        # Search from the dummy head to find the correct insertion position
        prev = dummy
        while prev.next.val < curr.val:
          prev = prev.next

        # Detach curr and insert it between prev and prev.next
        last_sorted.next = curr.next
        curr.next = prev.next
        prev.next = curr

      # Move to the next node in the unsorted portion
      curr = last_sorted.next

    return dummy.next