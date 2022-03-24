'''
Created with GitHub Copilot. 
'''


class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1

    def print(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev


# Find nodes in a linked list that equal 5
def find_nodes(linked_list):
    current = linked_list.head
    while current:
        if current.data == 5:
            print("found value", current.data)
        current = current.next


if __name__ == '__main__':

    ll = LinkedList()
    ll.add(1)
    ll.add(3)
    ll.add(7)
    ll.add(5)
    ll.add(2)

    ll.print()

    find_nodes(ll)
