class Queue(object):
    def __init__(self):
        self.items = []

    def isEmpty(self, items):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


q = Queue()

q.enqueue(5)
print(q.items)

q.enqueue(4)
print(q.items)

q.enqueue(7)
print(q.items)

q.enqueue(1)
print(q.items)
print(q.dequeue())
print(q.dequeue())
print(q.items)