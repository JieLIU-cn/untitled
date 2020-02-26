class Graph:
    # 无向图
    def __init__(self):
        self.nodes = []  # 储存节点
        self.edge = {}  # 以字典存储邻接表，key是节点，value用list存储邻接节点

    def insert(self, a, b):
        #  插入a，b节点的连接
        if not (a in self.nodes):
            self.nodes.append(a)
            self.edge[a] = list()

        if not (b in self.nodes):
            self.nodes.append(b)
            self.edge[b] = list()

        self.edge[a].append(b)
        self.edge[b].append(a)

    def succ(self, a):
        # 显示某个节点的边
        return self.edge[a]

    def show(self):
        # 显示所有节点
        return self.nodes

    def show_edge(self):
        # 显示所有节点的边
        print(self.edge)


if __name__ == "__main__":
    graph = Graph()
    graph.insert(0, 1)
    graph.insert(0, 2)
    graph.insert(0, 3)
    graph.insert(1, 3)
    graph.insert(2, 3)
    print(graph.succ(0))
    print(graph.show())
    graph.show_edge()
