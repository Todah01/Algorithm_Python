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

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def get_node(self, index):
        idx = 0
        cur = self.head

        while cur is not None:
            if idx == index:
                return cur.data
            else:
                idx += 1
                cur = cur.next
        return "값을 찾을 수 없습니다."

linked_list = LinkedList(5)
linked_list.append(12)
print(linked_list.get_node(1)) # -> 5를 들고 있는 노드를 반환해야 합니다!