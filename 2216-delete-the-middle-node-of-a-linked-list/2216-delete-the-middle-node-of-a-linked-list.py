# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None

        # Initialize slow and fast pointers
        slow = head
        fast = head.next.next  #if head.next else None

        # Move 'fast' pointer twice as fast as 'slow'
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Delete the middle node by skipping it
        slow.next = slow.next.next
        return head