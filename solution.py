# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        head = dummy
        
        fast = head
        prev = head
        cnt = 0
        
        while cnt < n:
            fast = fast.next
            cnt += 1
        
        slow = head
        
        while fast:
            prev = slow
            fast = fast.next
            slow = slow.next
            
        prev.next = slow.next 
        
        return head.next