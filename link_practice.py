"""
    practicing linked data structure
"""


class Data:
    def __init__(self, name: str):
        self.name = name

    def get_name(self) -> str:
        return self.name

    def __str__(self):
        return self.name


class Node:
    def __init__(self, data: Data):
        self.data = data
        self.next = None

    def get_data(self) -> Data:
        return self.data

    def get_next(self):
        return self.next

    def set_next(self, next_node) -> None:
        self.next = next_node

    def __str__(self):
        return str(self.data)


class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def append(self, data: Data):
        node = Node(data)
        if self.size == 0:
            self.first = node
        else:
            self.last.set_next(node)

        self.last = node
        self.size += 1

    def add_front(self, data: Data):
        node = Node(data)
        node.next = self.first
        self.first = node
        self.size += 1

    def remove_front(self):
        front = self.first

        if self.size > 0:
            self.first = self.first.get_next()
            self.size -= 1

        return front

    def get_size(self):
        return self.size

    def get_front(self):
        return self.first

    def __str__(self):
        lst = ['[']
        tmp = self.first
        while tmp is not None:
            lst.append(str(tmp))
            tmp = tmp.get_next()

            if tmp is not None:
                lst.append(", ")

        lst.append(']')

        return ''.join(lst)


def main():
    lst = LinkedList()

    for i in range(5):
        lst.add_front(Data(str(i)))

    first = lst.remove_front()
    print(lst, str(first))


if __name__ == "__main__":
    main()
