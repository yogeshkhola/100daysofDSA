#program for insertion of node in the linked list at different postion

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None #pointer


    #function to insert a new node at the begining
    def push(self,new_data):
        newNode=Node(new_data)
        newNode.next=self.head
        self.head=newNode

    #function to insert a node at given previous node
    def insertAfter(self,prev_node,new_data):

        if prev_node is None:
            print("given previous node must in linked list")
            return

    #create new node
        newNode=Node(new_data)
        newNode.next=prev_node.next
        prev_node.next=newNode

    #function to insert array at the end of the linked list

    def append(self,new_data):
        newNode=Node(new_data)
        if self.head is None: #if linkedlist is empty
            self.head=newNode
            return
        #else traverse till lastnode
        last=self.head
        while last.next:
            last=last.next

        last.next=newNode

    #function to print linked list
    def printlist(self):
        temp=self.head
        while temp:
            print(temp.data)
            temp=temp.next

llist=LinkedList()


llist.append(6)
llist.push(7)
llist.append(9)
llist.push(34)
llist.insertAfter(llist.head.next,8)

llist.printlist()