class Hashtable(object):
    def __init__(self):
        self.capacity = 10  # 分配的总容量
        self.hash_table = [[None, None]for i in range(self.capacity)]  # 哈希表
        self.num = 0
        self.load_factor = 0.75  # 载荷因子

    def hash(self, k, i):  # 哈希函数
        h_value = (k+i) % self.capacity
        if self.hash_table[h_value][0] == k:  # 如果哈希表中键值和键值一致
            return h_value
        if self.hash_table[h_value][0] is not None:  # 如果哈希表中的值已经被占用（和其他哈希值重复）
            i = i+1
            h_value = self.hash(k, i)
        return h_value

    def resize(self):
        # 扩容到原有元素数量的两倍
        self.capacity = self.num * 2
        temp = self.hash_table[:]
        self.hash_table = [[None, None]for i in range(self.capacity)]
        for i in temp:
            # 把原来已有的元素存入
            if(i[0] != None):  # 存有key 值
                hash_v = self.hash(i[0], 0)
                self.hash_table[hash_v][0] = i[0]
                self.hash_table[hash_v][1] = i[1]

    def put(self, k, v):
        hash_v = self.hash(k, 0)
        self.hash_table[hash_v][0] = k
        self.hash_table[hash_v][1] = v
        # 暂不考虑 key 重复的情况，具体自己可以优化
        self.num = self.num+1
        # 如果比例大于载荷因子
        if (self.num/len(self.hash_table) > self.load_factor):
            self.resize()

    def get(self, k):
        hash_v = self.hash(k, 0)
        return self.hash_table[hash_v][1]


table = Hashtable()
table.put(25,1)
#for i in range(1, 13):
#    table.put(i, i)
table.put(25,2)
print(table.get(3))
print(table.hash_table)