
#["화물차"]

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, data):
        self.head = Node(data)

    def append(self, data):
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = Node(data)

    def print_all(self):
        current = self.head

        while current is not None:
            print(current.data)
            current = current.next

    def get_node(self, index):
        cur = self.head
        cur_index = 0

        while (cur_index != index):
            cur = cur.next
            cur_index += 1
        return cur

    def add_node(self, index, data):

        if index == 0:
            next_node = self.head
            self.head = Node(data)
            self.head.next = next_node
        else:
            new_node = Node(data)
            prev_node = self.get_node(index-1)
            next_node = prev_node.next
            prev_node.next = new_node
            new_node.next = next_node

    def remove_node(self, index):
        if index == 0:
            self.head = self.get_node(index+1)
            return

        prev_node = self.get_node(index-1)
        next_node = self.get_node(index+1)
        prev_node.next = next_node



linked_list = LinkedList(10)
linked_list.append(40)
linked_list.append(50)
linked_list.append(65)
linked_list.add_node(0, 5440)

linked_list.remove_node(1)

print(linked_list.print_all())





































