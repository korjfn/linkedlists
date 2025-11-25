# Basic Singly Linked List Implimintation

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
node1 = Node(3)
node2 = Node(5)
node3 = Node(13)
node4 = Node(2)


node1.next = node2
node1.prev = node4


node2.prev = node1
node2.next = node3

node3.prev = node2
node3.next = node4

node4.next = node1
node4.prev = node3

print("traversing forward")

currentnode = node1
startnode = node1
print(currentnode.data, end = " ->")
currentnode = currentnode.next

while currentnode != startnode:
    print(currentnode.data, end = " -> ")
    currentnode = currentnode.next

print(" . . .")

print("traversing backward")
currentnode = node4
startnode = node4
print(currentnode.data, end = " ->")
currentnode = currentnode.prev

while currentnode != startnode:
    print(currentnode.data, end = " -> ")
    currentnode = currentnode.prev

print(" . . .")
