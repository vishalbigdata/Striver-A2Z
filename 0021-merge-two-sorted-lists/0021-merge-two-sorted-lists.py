# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        head = ListNode()
        tmp1, tmp2, tmp3 = list1, list2, head
        if tmp1 is None or tmp2 is None:
            if tmp1 is None: head.next = tmp2
            else: head.next=tmp1
        else:
            while(tmp1 is not None and tmp2 is not None):
                if (tmp1.val <= tmp2.val):
                    tmp3.next = tmp1
                    tmp1 = tmp1.next
                else: 
                    tmp3.next = tmp2
                    tmp2 = tmp2.next
                tmp3 = tmp3.next
                if tmp1 is not None:
                    tmp3.next = tmp1
                if tmp2 is not None:
                    tmp3.next = tmp2
        
        head = head.next
        return head


                 


























    #     p1 = list1
    #     p2 = list2
    #     tail = None
    #     head = None

    #     while(p1 is not None or p2 is not None):
    #         data = None

    #         if (p1 is not None and p2 is not None):
    #             if p1.val <= p2.val:
    #                 data = p1.val
    #                 p1 = p1.next
    #             else:
    #                 data = p2.val
    #                 p2 = p2.next
    #         elif( p1 is not None):
    #             data = p1.val
    #             p1 = p1.next
    #         else:
    #             data = p2.val
    #             p2 = p2.next

    #         if tail is None:
    #             head = self.insertAtEnd(tail,data)
    #             tail = head
    #         else:
    #             tail = self.insertAtEnd(tail,data)
    #     return  head


                

    # def insertAtEnd(self, tail, data):
    #     ntbi = ListNode(data)
    #     if tail is not None:
    #         tail.next = ntbi
    #     return ntbi


        