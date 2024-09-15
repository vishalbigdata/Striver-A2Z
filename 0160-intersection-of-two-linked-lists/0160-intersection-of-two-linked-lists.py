class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        # get lineked_list lenght each seperately
        m = self.findLength(headA)
        n = self.findLength(headB)

        # now fixed one pointer to each Linked_list
        fp = headA
        sp = headB

        # mark both the poiinter to same level 
        if m <= n :
            for i in range(n-m):
                sp = sp.next
        else:
            for i in range(m-n):
                fp = fp.next

        # traverse the linkedlist and compare  --> if match : return any pointer value , fp or sp
        
        while fp != None or sp != None:
            if fp == sp:
                return fp or sp
            sp = sp.next
            fp = fp.next
        
        return None


    def findLength(self,head):
        length = 0
        curr = head
        while curr != None:
            curr = curr.next
            length = length + 1
        return length


    #     m = self.findLength(headA)
    #     n = self.findLength(headB)
    #     fp  = headA
    #     sp = headB
    #     if m <= n: 
    #         for i in range(n-m): sp = sp.next
    #     else: 
    #         for i in range(m-n): fp = fp.next
    #     while fp is not None:
    #         if fp == sp: return fp # or sp
    #         fp = fp.next
    #         sp = sp.next
    #     return None
    # def findLength(self,head):
    #     length = 0
    #     curr = head
    #     while(curr is not None):
    #         curr = curr.next
    #         length = length + 1
    #     return length

