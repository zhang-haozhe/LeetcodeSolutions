class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head
        cnt = -1
        while fast != None:
            fast = fast.next
            if cnt % 2 == 0:
                slow = slow.next
            cnt += 1
        
        return slow