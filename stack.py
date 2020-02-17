class Stack(object):
    def __init__(self, limit=10):
        """
        定义栈为数组
        定义栈最大空间, 默认10
        """

        self.stack = []
        self.limit = limit

    def push(self, data):
        """
        入栈
        """
        if len(self.stack) >= self.limit:
            raise IndexError('超出栈容量')
        self.stack.append(data)

    def pop(self):
        """
        出栈
        """
        if self.stack:
            self.stack.pop()
        else:
            raise IndexError('pop from an empty stack')

    def peek(self):
        # 栈顶元素
        if self.stack:
            return self.stack[-1]

    def is_empty(self):
        # 判断空栈
        return not bool(self.stack)

    def size(self):
        # 返回栈大小
        return len(self.stack)


def is_balanced_parentheses(parentheses):
    """
    判断字符串中括号是否成对
    :param parentheses:  含括号的字符串
    :return: 真值
    """
    stack = Stack(len(parentheses))
    for i in parentheses:
        if i == '(':
            stack.push(i)
        elif i == ')':
            if stack.is_empty():
                return False
            else:
                stack.pop()
    return stack.is_empty()


if __name__ == '__main__':
    examples = ['((()))', '((())', '(()))']
    print('Balanced parentheses demonstration:\n')
    for example in examples:
        print('{}:{}'.format(example, str(is_balanced_parentheses(example))))
