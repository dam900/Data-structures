from LinkedList import LinkedList, Node

# The goal of this project is to show ability implement and work with queues.
# Queue is build on top of the LinkedList


class Queue:

    def __init__(self, list=None):
        if list is None:
            self.queue = LinkedList()
        if isinstance(list, LinkedList):
            self.queue = list
        else:
            self.queue = LinkedList()
            self.queue.add_multiple_nodes(list)

    def add_item(self, item) -> None:
        if isinstance(item, list):
            self.queue.add_multiple_nodes(item)
        else:
            self.queue.add_node(item)

    def take(self) -> Node:
        if self.queue.head is None:
            return None
        start = self.queue.head
        self.queue.head = self.queue.head.next_node
        return start

    def __len__(self):
        return len(self.queue)

    def __iter__(self):
        while self.queue.head is not None:
            yield self.take()


if __name__ == '__main__':
    queue = Queue(range(0, 11))
    queue.add_item([12, 34])
    print(queue.take())
    for i in queue:
        print(i, end=' ')
    print()
    print(queue.take())  # queue is empty
