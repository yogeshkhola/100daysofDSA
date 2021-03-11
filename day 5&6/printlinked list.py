class Node:
    def __init__(self,data):
        self.data=data
        self.next=None #initialize next as null
class LinkedList:
    def __init__(self):
        self.head=None #pointer

        #program to print content of the lsit
    def printlist(self):
        temp=self.head
        while temp:
            print(temp.data)
            temp=temp.next


llist = LinkedList()

llist.head = Node(1)
second = Node(2)
third = Node(3)

llist.head.next = second;  # Link first node with second
second.next = third;  # Link second node with the third node

llist.printlist()
