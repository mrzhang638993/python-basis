class CountList:
    def __init__(self, *args):
        self.values = [x for x in args]
        self.count = {}.fromkeys(range(len(self.values)), 0)

    def __len__(self):
        return len(self.values)

    def __getitem__(self, item):
        self.count[item] += 1
        return self.values[item]


#  传递的可变参数不是数组的
c1 = CountList(1, 3, 5, 7)
print(c1.values)
c1.__getitem__(1)  # 对应的是索引的数值操作的
print(c1.count)
