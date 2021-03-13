# Python program to find length of a linked list
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None


	def push(self, new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node

	def getCount(self):
		temp = self.head # Initialise temp
		count = 0 # Initialise count

		# Loop while end of linked list is not reached
		while (temp):
			count += 1
			temp = temp.next
		return count


if __name__=='__main__':
	llist = LinkedList()
	llist.push(1)
	llist.push(3)
	llist.push(1)
	llist.push(2)
	llist.push(1)
	print ("Count of nodes is :",llist.getCount())
