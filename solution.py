# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA is None or headB is None:
            return None
        
        pA = headA
        pB = headB
        redirectA = True
        redirectB = False
        # False means headA.
        # True means headB.
        end = None
        while pA is not pB:
            if pA.next != None:
                pA = pA.next
            else:
                if end is None:
                    end = pA
                else:
                    if pA is not end:
                        return None
                pA = headB if redirectA else headA
                redirectA = not redirectA
                
            if pB.next != None:
                pB = pB.next
            else:
                if end is None:
                    end = pB
                else:
                    if pB is not end:
                        return None
                pB = headB if redirectB else headA
                redirectB = not redirectB
        return pA