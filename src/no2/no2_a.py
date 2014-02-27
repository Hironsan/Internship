class Stack(object):
    def __init__(self):
        self.contents = []

    def empty(self):
        return True if len(self.contents) == 0 else False

    def peek(self):
        if self.empty():
            return None
        else:
            return self.contents[-1]

    def pop(self):
        if self.empty():
            return None
        else:
            return self.contents.pop()

    def push(self, value):
        self.contents.append(value)

    def size(self):
        return len(self.contents)

    def printstack(self):
        print self.contents


if __name__ == "__main__":
    stack = Stack()
    print stack.empty()
    print stack.pop()
    print stack.peek()
    stack.push(1)
    print stack.empty()
    print stack.pop()
    print stack.peek()
    for i in range(3):
        stack.push(i)
    while not stack.empty():
        print "size=", stack.size()
        print stack.pop()