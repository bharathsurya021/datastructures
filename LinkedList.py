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

    def addAtStart(self, data):
        newNode = Node(data)  #create new node
        newNode.next = self.head  # assign newnode ref to current first node which is stored in head
        self.head = newNode  # assign head to newnode

    def addAtEnd(self, data):
        newNode = Node(data)  #create new node
        if self.head is None:
            self.head = newNode
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = newNode
            newNode.next = None

    def addAfterNode(self, data, x):
        temp = self.head
        while temp is not None:
            if temp.data == x:
                newNode = Node(data)
                newNode.next = temp.next
                temp.next = newNode
                break
            temp = temp.next
        if temp is None:
            print("Node is not found")

    def addBeforeNode(self, data, x):
        if self.head is None:
            print('Linked list is empty')
            return
        if self.head.data == x:
            newNode = Node(data)
            newNode.next = self.head
            self.head = newNode
            return
        current = self.head
        while current.next is not None:
            if current.next.data == x:
                newNode = Node(data)
                newNode.next = current.next
                current.next = newNode
                break
            current = current.next
        if current.next is None:
            print("Node is not found")


myList = LinkedList()

myList.head = Node(1)
second = Node(2)
third = Node(3)

myList.head.next = second
second.next = third
print(myList.isEmpty())
myList.addAtStart(10)
myList.addAtStart(20)
myList.addAtEnd(100)
myList.addAtEnd(40)
# myList.addAfterNode(200, 60)
myList.addBeforeNode(200, 20)
myList.traversal()