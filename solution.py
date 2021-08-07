# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head):
        a = None
        b, c = head, head
        while c is not None:
            c = c.next
            b.next = a
            a = b
            b = c
        return a
        
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        leftNode, rightNode = None, None
        temp = head
        prev = None
        before = None
        cnt = 1
        while temp != None:
            if cnt == left:
                leftNode = temp
                before = prev
            if cnt == right:
                rightNode = temp
            prev = temp
            temp = temp.next
            cnt += 1
        after = rightNode.next
        rightNode.next = None
        
        if before is not None:
            before.next = self.reverse(leftNode)
        else:
            head = self.reverse(leftNode)
        leftNode.next = after
        return head
        