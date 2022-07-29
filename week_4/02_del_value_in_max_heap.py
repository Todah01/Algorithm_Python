class MaxHeap:
    def __init__(self):
        self.items = [None]

    def insert(self, value):
        self.items.append(value)
        cur_index = len(self.items) - 1

        while cur_index > 1:  # cur_index 가 1이 되면 정상을 찍은거라 다른 것과 비교 안하셔도 됩니다!
            parent_index = cur_index // 2
            if self.items[parent_index] < self.items[cur_index]:
                self.items[parent_index], self.items[cur_index] = self.items[cur_index], self.items[parent_index]
                cur_index = parent_index
            else:
                break

    def delete(self):
        cur_idx = 1
        # 1. 루트 노드와 맨 끝 노드를 변경
        self.items[cur_idx], self.items[len(self.items) - 1] = self.items[len(self.items) - 1], self.items[cur_idx]
        # 2. 맨 뒤에 있는 노드를 삭제
        del_value = self.items.pop()

        # 4. 자식 노드 둘보다 부모노드가 크거나 가장 바닥에 도달하지 않을때까지 3의 과정을 반복
        while cur_idx < len(self.items) - 1:
            first_kid_idx = cur_idx * 2
            second_kid_idx = (cur_idx * 2) + 1
            # 가장 큰 값만 찾으면 되기 때문에 max_idx 만 비교하면 되기 때문에 max_idx 를 비교
            max_idx = cur_idx

            # 3. 변경된 노드와 자식 노드들을 비교, 두 자식들 중 더 큰 노드와 비교해서 자신보다 자식이 더 크다면 자리를 변경
            if first_kid_idx < len(self.items) - 1 and self.items[first_kid_idx] > self.items[max_idx]:
                max_idx = first_kid_idx

            if second_kid_idx < len(self.items) - 1 and self.items[second_kid_idx] > self.items[max_idx]:
                max_idx = second_kid_idx

            if max_idx == cur_idx:
                break

            self.items[cur_idx], self.items[max_idx] = self.items[max_idx], self.items[cur_idx]
            cur_idx = max_idx

        return del_value


max_heap = MaxHeap()
max_heap.insert(8)
max_heap.insert(6)
max_heap.insert(7)
max_heap.insert(2)
max_heap.insert(5)
max_heap.insert(4)
print(max_heap.items)  # [None, 8, 6, 7, 2, 5, 4]
print(max_heap.delete())  # 8 을 반환해야 합니다!
print(max_heap.items)  # [None, 7, 6, 4, 2, 5]