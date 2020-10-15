from link_practice import LinkedList, Node, Data


class Stack:
    def __init__(self):
        self.stack = LinkedList()

    def push(self, item):
        self.stack.add_front(Data(item))

    def pop(self):
        return self.stack.remove_front()

    def top(self):
        return self.stack.get_front()

    def is_empty(self):
        return self.stack.get_size() == 0


def main():
    s = Stack()

    for i in range(1, 11):
        s.push(str(i))

    while not s.is_empty():
        print(str(s.pop()))


if __name__ == '__main__':
    main()
