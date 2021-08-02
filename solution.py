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
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        try:
            temp = head.next.next
        except:
            return head
        output = list()
        temp = head
        while temp is not None:
            output.append(temp)
            temp = temp.next

        for i in range(len(output) // 2):
            temp = output[i].next
            output[i].next = output[-i - 1]
            output[-i - 1].next = temp
        else:
            if len(output) % 2 == 0:
                output[i].next.next = None
            else:
                output[i].next.next.next = None

# lst = [1]
# head = list_to_link(lst)

# sol = Solution()
# sol.reorderList(head)
# print_list(head)
