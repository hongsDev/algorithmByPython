class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value):
        # 어떻게 하면 될까요
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            self.head.next = self.tail
            return

        self.tail.next = new_node
        self.tail = new_node

    def dequeue(self):
        # 어떻게 하면 될까요?

        if self.is_empty():
            return "12312"

        result = self.head
        self.head = self.head.next
        return result

    def peek(self):
        # 어떻게 하면 될까요?
        if self.is_empty():
            return "sdkfjkls"

        return self.head

    def is_empty(self):
        # 어떻게 하면 될까요?
        return self.head is None


queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
