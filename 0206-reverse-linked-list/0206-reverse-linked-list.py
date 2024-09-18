# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # recursively 
        # if head is None or head.next is None :
        #     return head
        # new_head = self.reverseList(head.next)
        # front  = head.next
        # front.next = head
        # head.next = None
        # return  new_head

        # using 3 poiter

        temp  = head
        prev = None
        while temp:
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front
        return prev




