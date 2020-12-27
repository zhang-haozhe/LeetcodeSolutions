class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self, head = None):
        self.head = head

    def link_the_list(self, the_list):
        iterator = self.head
        for i in range (len(the_list)):
            temp = Node(the_list[i])
            iterator.next = temp
            iterator = iterator.next
    
    def print_list(self):
        iterator = self.head
        while iterator != None:
            print(iterator.data)
            iterator = iterator.next
        
# Parameters:
#  list: LinkedList
# return type: None

def reverseList(list):
    # your code here
    c = list.head
    b = None
    a = None
    while c != None:
        a = b
        b = c
        c = c.next
        b.next = a
    list.head = b
    
linked = LinkedList(Node(5))
linked.link_the_list([5,5,5])

linked.print_list()
reverseList(linked)