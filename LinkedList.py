#!/usr/bin/python
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def init_list():
    global node1, node2, node3, node4
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3.33333)
    node4 = Node("four")
    node1.next = node2
    node2.next = node3
    node3.next = node4

def Main():
    init_list()

def Print(node):
    while node:
       print(node.data)
       node = node.next

def Insert(node, data):
    if node:
        node = Insert(node.next, data)
    else:
        return Node(data)


Main()
node = node1
#Print(node)
Insert(node, "Test")
Print(node)
