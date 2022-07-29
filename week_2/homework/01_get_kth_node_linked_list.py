# 나의 풀이
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def get_kth_node_from_last(self, k):
        node_pointer = []
        cur = self.head
        while cur.next is not None:
            cur = cur.next
            node_pointer.append(cur)
        return node_pointer[-k]


linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)
linked_list.append(9)
linked_list.append(10)

print(linked_list.get_kth_node_from_last(2).data)  # 9가 나와야 합니다!]


# 튜터님 풀이
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def get_kth_node_from_last(self, k):
        length = 0
        cur = self.head
        cur_k = self.head

        while length < k:
            cur = cur.next
            length += 1

        while cur is not None:
            cur = cur.next
            cur_k = cur_k.next

        return cur_k


linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)
linked_list.append(9)
linked_list.append(10)

print(linked_list.get_kth_node_from_last(2).data)  # 9가 나와야 합니다!]