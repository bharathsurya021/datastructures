class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


node1 = Node(10)  #create node with data=10,ref=None
print(node1)  # prints ref of the node1 obj


class LinkedList:
    def __init__(self):
        self.head = None  # intializing empty Linked List(no nodes)

    def isEmpty(self):
        return self.head == None

    def traversal(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next


myList = LinkedList()

myList.head = Node(1)
second = Node(2)
third = Node(3)

myList.head.next = second
second.next = third

myList.traversal()