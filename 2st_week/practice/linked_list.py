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

    def printAll(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def get_kth_node_from_last1(self, k):
        length = 1
        cur = self.head
        while cur.next is not None:
            cur = cur.next
            length += 1

        cur = self.head
        for i in range(length - k):
            cur = cur.next


    def get_kth_node_from_last2(self, k):
        fast = self.head
        slow = self.head

        for i in range(k-1):
            fast = fast.next

        while fast.next is not None:
            fast = fast.next
            slow = slow.next
        return slow.data

########################################################################################################################

list1 = LinkedList(10)
list1.append(20)
list1.append(40)
list1.append(70)
list1.append(80)


#print(list1.get_kth_node_from_last1(3))
print(list1.get_kth_node_from_last2(1))












