class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class Linked_List(object):
    def __init__(self, head = None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
        current.next = new_element
        else self.head = new_element

    def is_empty(self):
        return not self.head

    def insert(self, position, new_element):
        if position < 0 or position > self.get_length():
            raise IndexError('insert 插入时，key的值超出了范围')
        temp = self.head
        if position == 0:
            new_element.next = temp
            self.head = new_element
            return
        i = 1
        while i < position:
            pre = temp
            temp = temp.next
            i += 1
        pre.next = new_element
        new_element.next = temp