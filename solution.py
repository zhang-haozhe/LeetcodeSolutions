# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        left = head
        right = head
        try:
            right = head.next
            left.val, right.val = right.val, left.val
        except:
            return head
        
        while right.next and right.next.next:
            left = left.next.next
            right = right.next.next
            left.val, right.val = right.val, left.val
        
        return head