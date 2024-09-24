# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        # dummy head for even ll
        even_head = ListNode(0)

        # dummy ll for odd ll
        odd_head = ListNode(0)

        even_tail, odd_tail = even_head, odd_head

        pos = 1
        current = head

        while current : 
            if pos % 2 == 0:
                even_tail.next = current
                even_tail = even_tail.next

            else:
                odd_tail.next = current
                odd_tail = odd_tail.next
            
            current = current.next
            pos = pos +1
        
        # combiine even list with odd llst

        odd_tail.next = even_head.next

        even_tail.next = None

        return odd_head.next


