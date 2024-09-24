# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
         # find middlle -- move slow t mid
        
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        first_half, second_half = head , prev

        while second_half:
            if first_half.val!= second_half.val:
                return False

            first_half =  first_half.next

            second_half = second_half.next

        return True

