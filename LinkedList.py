
"""
Goal of this project is to show ability to implement and work with linked lists
"""


class Node:

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    def __str__(self):
        return str(self.data)


class LinkedList:

    def __init__(self):
        self.head: Node | None = None
        self.tail: Node | None = None

    def add_as_head(self, data):
        current_head = self.head
        self.head = Node(data)
        self.head.next_node = current_head

    def add_node(self, data) -> None:
        if self.head is None:
            self.tail = self.head = Node(data)
        else:
            self.tail.next_node = Node(data)
            self.tail = self.tail.next_node

    def add_multiple_nodes(self, data) -> None:
        for d in data:
            self.add_node(d)

    def travel_to(self, pos: int) -> Node:
        current_node = self.head
        for _ in range(pos):
            current_node = current_node.next_node
        return current_node

    def __iter__(self) -> Node:
        current_node = self.head
        while current_node is not None:
            yield current_node
            current_node = current_node.next_node

    def __len__(self) -> int:
        i = 0
        current_node = self.head
        while current_node is not None:
            current_node = current_node.next_node
            i += 1
        return i


if __name__ == '__main__':

    linked_list = LinkedList()
    linked_list.add_multiple_nodes(range(0, 11))
    print('node at index 2: ', linked_list.travel_to(2))
    print('len before adding node', len(linked_list))
    linked_list.add_as_head(45)
    print('len after adding node', len(linked_list))
    print('all nodes in a list')
    for i in linked_list:
        print(i, end=' ')


