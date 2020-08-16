# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        curr = head
        prev = ListNode(None)

        while curr:
            jumpOver = -100
            while curr and curr.next and curr.val == curr.next.val:
                # print(jumpOver:=curr.val)
                jumpOver = curr.val
                curr = curr.next
            else:
                if curr and not curr.next and curr.val == jumpOver:
                    prev.next = None
            if jumpOver == -100:
                prev.next = curr
                prev = prev.next
            if jumpOver == head.val:
                head = curr.next
            curr = curr.next
        return head
