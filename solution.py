class Solution:
    def reverse(self, head, k):
        cnt = 0
        target = head
        while target != None and cnt != k:
            target = target.next
            cnt += 1
            
        if cnt < k:
            return head
        
        b = head
        a = None
        nextNode = self.reverse(target, k)
        while b != None and cnt != 0:
            c = b.next
            b.next = a
            a = b
            b = c
            cnt -= 1
        head.next = nextNode
        return a
        
        
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        return self.reverse(head, k)