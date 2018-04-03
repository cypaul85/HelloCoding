class Node(object):
    def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

def Insert(head, data):
    if (head == None):
        head = Node(data)
    else:
        current = head
        while (current.next != None):
            current = current.next
        current.next = Node(data)
    return head

head = None
head = Insert(head, 5)
head = Insert(head, 6)
head = Insert(head, 7)

while head:
    print(head.data)
    head = head.next