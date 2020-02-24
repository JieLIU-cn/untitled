class Node:
    def __init__(self, element):
        self.item = element
        self.left = None
        self.right = None

    def __str__(self):
        return self.item


class Tree:
    def __init__(self):
        self.root = None

    def add(self, element):
        """
        插入元素到树
        :param element: 要插入的元素
        :return:  无返回值
        """
        node = Node(element)

        if self.root is None:  # 树为空时
            self.root = node
            return

        else:
            q = [self.root]  # 通过数组建立队列，pop(0)出队，append入队，可以保证插入的位置靠左、靠上
            while Ture:  # 因为是插入，所以不必设置终止条件
                pop_node = q.pop(0)  # 出队
                if pop_node.left is None:  # 判断左孩子
                    pop_node.left = node
                    return
                elif pop_node.right is None:  # 判断右孩子
                    pop_node.right = node
                    return
                else:  # 如果都非空则左右孩子入队
                    q.append(pop_node.left)
                    q.append(pop_node.right)

    def get_parent(self, element):

        if self.root is None or self.item == element:  # 如果树为空，或搜索值为根节点，则没有父节点
            return None

        q = [self.root]  # 数组队列
        while q is not None:  # 队列为空，说明遍历完树，未发生匹配
            pop_node = q.pop(0)  # 出队
            if pop_node.left.item == element:  # 判断左孩子
                return pop_node
            if pop_node.right.item == element:  # 判断右孩子
                return pop_node
            if pop_node.left is not None:  # 左孩子入列
                q.append(pop_node.left)
            if pop_node.right is not None:  # 右孩子入列
                q.append(pop_node.right)
        return None  # 遍历完成后无返回，则未匹配到

    def delete(self, element):

        if self.root is None:
            return False

        parent = self.get_parent(element)

        if parent:
            if parent.left.item == element:
                del_node = parent.left
            else:
                del_node = parent.right

            if del_node.left is None:
                if parent.left.item == element:
                    parent.left = del_node.right
                else:
                    parent.right = del_node.right

                del del_node

            elif del_node.right is None:
                if parent.left.item == element:
                    parent.left = del_node.left
                else:
                    parent.right = del_node.right

                del del_node
                return True

            else:
                






