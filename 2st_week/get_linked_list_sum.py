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


def get_single_linked_list_sum(linked_list):
    liked_sum=0
    cur = linked_list.head
    while cur is not None:
        liked_sum = liked_sum * 10 + cur.data
        cur = cur.next
    return liked_sum

def get_linked_list_sum(linked_list1, linked_list2):
    return get_single_linked_list_sum(linked_list1) +  get_single_linked_list_sum(linked_list2)


linked_list1 = LinkedList(6)
linked_list1.append(7)
linked_list1.append(8)

linked_list2 = LinkedList(3)
linked_list2.append(5)
linked_list2.append(7)


print(get_linked_list_sum(linked_list1, linked_list2))
