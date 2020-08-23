# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None, last=None):
        self.val = val
        self.next = next
        self.last = last
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        curr = head
        prev = ListNode()
        check = head
        count = 0
        
        while curr:
            if prev != None:
                curr.last = prev
            prev = curr
            curr = curr.next
            count += 1
        for _ in range(count):
            # print(prev.val, check.val)
            if prev.val != check.val:
                return False
            prev = prev.last
            check = check.next
        return True