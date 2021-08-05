def list_to_link(lst):
    """Takes a Python list and returns a Link with the same elements.
    """
    if len(lst) == 1:
        return ListNode(lst[0])
    return ListNode(lst[0], list_to_link(lst[1:]))  # <<<< RECURSIVE

def print_list(lst):
    temp = lst
    while temp is not None:
        print(temp.val)
        temp = temp.next

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        temp = head
        nodes = []
        
        while temp != None:
            nodes.append(temp)
            temp = temp.next
        
        nodes.sort(key=lambda x: x.val)
        
        node = None
        
        for index, key in enumerate(nodes):
            if index == 0:
                node = key
            else:
                node.next = key
                node = node.next
        else:
            node.next = None
        return nodes[0]

lst = [4,2,1,3]
head = list_to_link(lst)

sol = Solution()
sol.sortList(head)
print_list(head)
