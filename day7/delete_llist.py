 # Python3 program to delete all
# the nodes of singly linked list

class Node:

	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	def deleteList(self):

		current = self.head
		while current:
			prev = current.next # move next node

			del current.data

			current = prev

	def push(self, new_data):

		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node


if __name__ == '__main__':

	llist = LinkedList()
	llist.push(1)
	llist.push(4)
	llist.push(1)
	llist.push(12)
	llist.push(1)

	print("Deleting linked list")
	llist.deleteList()

	print("Linked list deleted")


