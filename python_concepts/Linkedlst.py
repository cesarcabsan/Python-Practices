#Singly Linked List
class Node:
    def __init__(self, item):
        self.item = item 
        self.next = None 

class LinkedList:
    def __init__(self):
        self.head = None

singly = LinkedList()

singly.head = Node(1)
sec = Node(2)
third = Node(3)
fourth = Node(4)
fifth = Node(5)
sixth = Node(6)

singly.head.next = sec
sec.next = third
third.next = fourth
fourth.next = fifth
fifth.next = sixth

while singly.head != None:
    print(singly.head.item, '', end='')
    singly.head = singly.head.next 
