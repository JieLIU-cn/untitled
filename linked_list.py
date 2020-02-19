class Node:
    # 结点： 每个结点是一个对象，包括数据和下一个节点（对象）
    def __init__(self, data):
        self.data = data  # 数据
        self.next = None  # 下一个链点


class LinkedList:
    #
    def __init__(self, head=None):
        self.head = head  # 链表头结点

    def append(self, new_element):
        current = self.head  # 用current表示遍历的每个结点
        if self.head:
            # 从头结点找到尾结点
            while current.next:  # 尾结点的判定条件
                current = current.next
            current.next = new_element  # 将值赋予尾结点的next
        else:
            self.head = new_element

    def is_empty(self):
        return not self.head  # 只判断头结点

    def insert(self, position, new_element):  # new_element 也是节点对象
        if position < 0 or position > self.get_length():  # 可以插入队尾 position = self.get_length
            raise IndexError('insert 插入时，key的值超出了范围')

        temp = self.head
        if position == 0:  # 插入头结点
            new_element.next = temp
            self.head = new_element
            return

        i = 0
        while i < position:  # pre（前一节点） 和 temp 组成的间隙即所要插入的位置， 移动position次即间隙到达位置
            pre = temp
            temp = temp.next
            i += 1
        pre.next = new_element  # 插入新节点
        new_element.next = temp

    def remove(self, position):
        if position < 0 or position > self.get_length() - 1:
            raise IndexError('删除的元素索引超出范围')

        temp = self.head
        if position == 0:
            self.head = temp.next
            temp.next = None  # 将原头结点的next释放
            return

        i = 0
        while i < position:
            pre = temp
            temp = temp.next
            i += 1
        pre.next = temp.next
        temp.next = None

    def get_length(self):
        temp = self.head
        length = 0
        while temp:
            length += 1
            temp = temp.next  # 从头结点遍历到尾结点
        return length

    def print_list(self):
        print('Link_list:')
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def reverse(self):
        prev = None
        temp = self.head
        while temp:
            next_node = temp.next
            temp.next = prev
            prev = temp
            temp = next_node
        self.head = prev

    def initlist(self, data_list):
        # 通过list建立链表
        self.head = Node(data_list[0])
        temp = self.head
        for i in data_list[1:]:
            node = Node(i)
            temp.next = node
            temp = temp.next

    def swap_nodes(self, d1, d2):

        # 若d1、d2相等，则不需交换
        if d1 == d2:
            return

        # 遍历查找d1
        prevD1 = None
        D1 = self.head
        while D1 and D1.data != d1:  # D1为None说明遍历到最后也未匹配或链表为空；D1.data为d1，说明找到了元素对应的节点
            prevD1 = D1
            D1 = D1.next

        # 遍历查找d1
        prevD2 = None
        D2 = self.head
        while D2 and D2.data != d1:
            prevD2 = D2
            D2 = D2.next

        # 若为空链表或有元素未找到，则不执行
        if D1 is None or D2 is None:
            return

        # 交换元素
        if prevD1:  # 找到了元素
            prevD1.next = D2
        else:  # 元素为头结点，所以prev为空
            self.head = D2

        if prevD2:
            prevD2.next = D1
        else:
            self.head = D1

        # 交换指针
        temp = D1.next
        D1.next = D2.next
        D2.next = temp


if __name__ == '__main__':
    lst = LinkedList
    lst.append(n1=Node(5))
    lst.append(Node(4))
    lst.append(Node(3))
    lst.append(Node(2))
    lst.append(Node(1))
    lst.print_list()
    lst.swap_nodes(1,4)
    print('After swapping:')
    lst.print_list()

