# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        slowp = head
        fastp = head

        for i in range(n):
            fastp = fastp.next
        
        if fastp is None:
            return head.next

        while fastp.next is not None:
            slowp= slowp.next
            fastp =fastp.next

        delnode = slowp.next
        slowp.next = slowp.next.next
        delnode = None

        return head