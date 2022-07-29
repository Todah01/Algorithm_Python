class Dict:
    def __init__(self):
        self.items = [None] * 8

    def put(self, key, value):
        idx = hash(key) % len(self.items)
        self.items[idx] = value
        return

    def get(self, key):
        return self.items[hash(key) % 8]


my_dict = Dict()
my_dict.put("test", 3)
print(my_dict.get("test"))  # 3이 반환되어야 합니다!