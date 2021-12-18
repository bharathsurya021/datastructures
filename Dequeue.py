class Deque(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def insertFront(self, item):
        return self.items.append(item)

    def insertRear(self, item):
        return self.items.insert(0, item)

    def deleteFront(self):
        return self.items.pop()

    def deleteRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)


d = Deque()
d.insertFront('hello')
d.insertRear('world')
print(d.size())
print(d.deleteFront() + ' ' + d.deleteRear())
print(d.size())
