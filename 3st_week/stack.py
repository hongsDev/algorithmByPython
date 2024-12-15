from operator import truediv


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = Node(3)

    def push(self, value):
        # 어떻게 하면 될까요?
        new_head = Node(value)
        new_head.next = self.head
        self.head = new_head

    # pop 기능 구현
    def pop(self):
        # 어떻게 하면 될까요?
        if self.is_empty():
            return "stack is empty"

        del_node = self.head
        self.head =  self.head.next
        return del_node

    def peek(self):
        # 어떻게 하면 될까요?
        if self.is_empty():
            return "stack is empty"
        return self.head.data

    # isEmpty 기능 구현
    def is_empty(self):
        # 어떻게 하면 될까요?
        return self.head is None

stack = []
stack.append(3)  
stack.append(4)
stack.append(5)
stack.append(6)

print(stack[0])