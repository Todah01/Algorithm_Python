# 스택처럼 맨 위의 원소만 제거할 수 있습니다.
class MaxHeap:
    def __init__(self):
        self.items = [None]

    def insert(self, value):
        self.items.append(value)
        idx = len(self.items) - 1

        while idx > 1:
            if self.items[idx] > self.items[idx//2]:
                self.items[idx], self.items[idx//2] = self.items[idx//2], self.items[idx]
                idx = idx//2
            else:
                break


max_heap = MaxHeap()
max_heap.insert(3)
max_heap.insert(4)
max_heap.insert(2)
max_heap.insert(9)
print(max_heap.items)  # [None, 9, 4, 2, 3] 가 출력되어야 합니다!