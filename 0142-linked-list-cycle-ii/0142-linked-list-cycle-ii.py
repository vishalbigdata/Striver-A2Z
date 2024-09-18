# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # Optimal Approach

        slow = head
        fast = head

        while fast and fast.next : 

            slow = slow.next
            fast = fast.next.next

            # if they meet
            if slow == fast:
                # reset slow pointer
                slow = head

                while slow!=fast :
                    slow = slow.next
                    fast = fast.next

                return slow
        return None























        # Bruteforce apprach 

        # temp  = head
        # node_map = {}
        # while temp is not None:

        #     if temp in node_map:
        #         return temp
            
        #     node_map[temp] = True
        #     temp = temp.next
        # return None


        # Optimal Approach 






