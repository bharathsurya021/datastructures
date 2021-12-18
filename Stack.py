class Stack(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def top(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


s = Stack()
print(s.isEmpty())
s.push(5)
s.push(3)
s.push(4)
s.pop()
s.push(1)
print(s.size())
stacks = s
print(s.items)
print(s.top())
