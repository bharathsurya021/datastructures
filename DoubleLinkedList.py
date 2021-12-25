class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def traversalForward(self):
        if self.head is None:
            print('Linked Lsit is empty')
        else:
            current = self.head
            while current:
                print(current.data, end=" ")
                current = current.next

    def traversalBackword(self):
        if self.head is None:
            print('Linked Lsit is empty')
        else:
            current = self.head
            while current.next:
                current = current.next
            while current:
                print(current.data, end=" ")
                current = current.prev


DLinkedList = DoubleLinkedList()
DLinkedList.head = Node(10)
second = Node(20)
third = Node(30)
DLinkedList.head.next = second
second.next = third
third.prev = second
second.prev = DLinkedList.head
DLinkedList.head.prev = None
DLinkedList.traversalForward()
print(end='\n')
DLinkedList.traversalBackword()