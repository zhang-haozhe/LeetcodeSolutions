# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge(self, list1, list2):
        prehead = ListNode(-1)
        prev = prehead
        
        while list1 and list2:
            if list1.val > list2.val:
                prev.next = ListNode(list2.val)
                list2 = list2.next
                prev = prev.next
            else:
                prev.next = ListNode(list1.val)
                list1 = list1.next
                prev = prev.next
        
        prev.next = list1 if list1 else list2
        
        return prehead.next
    
    def sortList(self, head: ListNode) -> ListNode:
        temp = head
        length = 0
        while temp:
            temp = temp.next
            length += 1
        
        if length == 0:
            return None
        
        if length == 1:
            return head
        
        if length == 2:
            val1 = head.val
            val2 = head.next.val
            if val1 > val2:
                node1 = head
                node2 = head.next
                node1.next = None
                node2.next = node1
                return node2
            return head
        
        midway = head
        for _ in range(length // 2 - 1):
            midway = midway.next
        
        leftList = head
        rightList = midway.next
        midway.next = None
        
        
        left = self.sortList(leftList)
        right = self.sortList(rightList)
        
        
        return self.merge(left, right)