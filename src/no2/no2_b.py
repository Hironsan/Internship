from no2_a import Stack


class Queue(object):

    def __init__(self):
        self.st1 = Stack()
        self.st2 = Stack()

    def add(self, value):
        self.st1.push(value)

    def peek(self):
        if not self.st2.empty():
            return self.st2.peek()
        self.refill()
        return self.st2.peek()

    def remove(self):
        if not self.st2.empty():
            return self.st2.pop()
        self.refill()
        return self.st2.pop()

    def size(self):
        return self.st1.size() + self.st2.size()

    def refill(self):
        """
        move value from st1 to st2
        """
        while not self.st1.empty():
            self.st2.push(self.st1.pop())

if __name__ == "__main__":
    queue = Queue()
    for i in range(3):
        queue.add(i)
    queue.st1.printstack()
    queue.st2.printstack()
    print queue.remove()
    print queue.remove()
    for i in range(5,8):
        queue.add(i)
    queue.st1.printstack()
    queue.st2.printstack()
    print queue.remove()
    for i in range(queue.size()):
        print queue.remove()