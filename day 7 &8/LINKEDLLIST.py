class Node:  # represent individual elment in the linked list and it is two class members data and next(pointer)
    def __init__(self, data=None, next=None):
        self.data = data  # data can contains integer or complex no.
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None  # head variable points the head of the linked list

    def insert_at_begining(self, data):  # insert value at the begining of the linked list
        node = Node(data, self.head)
        self.head = node  # it refer the next node

    def print(self):  # to print the linked list
        if self.head is None:
            print("linked list is empty")
            return
        # if it is not blanked

        itr = self.head
        llstr = ' '
        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next
        print(llstr)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next

        return count


if __name__ == '__main__':
    ll = LinkedList()
    # ll.insert_at_begining(5)
    # ll.insert_at_begining(23)
    # ll.insert_at_begining(54)
    # # ll.print()
    # ll.insert_at_end(76)
    # ll.insert_at_end(1)
    # ll.print()

    ll.insert_at_end(["banana", "apple", "mango", "grapes"])
    ll.print()

    print("length", ll.get_length())