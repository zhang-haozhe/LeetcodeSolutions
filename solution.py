# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, root, prev):
        # your code here
        c = root
        b = prev
        a = None
        default = root
        while c != None:
            a = b
            b = c
            c = c.next
            b.next = a
        default.next = None
        return b
    def isPalindrome(self, head: ListNode) -> bool:
        length = 0
        curr = head
        while curr != None:
            curr = curr.next
            length += 1
        
        if length <= 1:
            return True
        
        start = head
        prev = None
        constant = 1 if length % 2 == 1 else 0
        for _ in range(length // 2 + constant):
            prev = start
            start = start.next
        
        if length // 2 != 1:
            prev.next = self.reverseList(start, prev)
        curr = head
        curr2 = prev.next
        for _ in range(length // 2):
            if curr.val == curr2.val:
                curr = curr.next
                curr2 = curr2.next
            else:
                return False
        return True