"""This module implements a queue data structure using a stack
data structure.
"""
from typing import Generic, TypeVar

from stack import Stack

T = TypeVar("T")


class QueueUsingStack(Generic[T]):
    """Represents a queue data structure.

    The underlying implementation uses a stack data structure.
    """

    def __init__(self):
        """Initializes a new QueueUsingStack instance."""
        self.stack: Stack[T] = Stack()
        self.front_item = None

    def enqueue(self, item: T) -> None:
        """Adds the provided `item` to the queue.

        Items are added to the back of the queue. This is a constant
        time operation.

        :param item: The item to add to the queue.
        """
        self.stack.push(item)

        if len(self.stack) == 1:
            self.front_item = item

    # Time: Theta(n), Space: Theta(n)
    def dequeue(self) -> T | None:
        """Removes the first item from the queue.

        Items are removed from the front of the queue. This is a
        Theta(n) operation.

        :return: The removed item.
        """
        if self.stack.empty():
            return None

        top_item: T | None = None
        put_back_items: list[T] = []
        while True:
            top_item = self.stack.pop()
            if top_item and len(self.stack) >= 1:
                put_back_items.append(top_item)
            else:
                break

        for item in reversed(put_back_items):
            self.stack.push(item)

        if put_back_items:
            self.front_item = put_back_items[-1]

        return top_item

    def front(self) -> T | None:
        """Returns the item from the front of the queue.

        The item is not removed from queue. This is a constant time
        operation.
        """
        return self.front_item

    def peek(self) -> T | None:
        """Returns the item from the front of the queue.

        The item is not removed from queue. This is a constant time
        operation.
        """
        return self.front()

    def is_empty(self) -> bool:
        """Returns True if the queue is empty, False otherwise.

        This is a constant time operation.
        """
        return self.stack.empty()

    def is_full(self) -> bool:
        """Returns True if the queue is full, False otherwise.

        This is a constant time operation.
        """
        return self.stack.is_full()

    def space(self) -> int:
        """Returns the maximum number of items that were held in the queue.

        This is a constant time operation.
        """
        return self.stack.space()

    def __len__(self) -> int:
        """Returns the length of the queue.

        This is a constant time operation.
        """
        return len(self.stack)


if __name__ == "__main__":
    int_queue: QueueUsingStack[int] = QueueUsingStack()
    assert int_queue.is_empty() is True
    assert int_queue.is_full() is False
    assert int_queue.space() == 0
    assert len(int_queue) == 0

    int_queue.enqueue(1)
    int_queue.enqueue(2)
    int_queue.enqueue(3)

    assert int_queue.front() == 1
    assert int_queue.peek() == 1
    assert int_queue.is_empty() is False
    assert int_queue.is_full() is False
    assert int_queue.space() == 3
    assert len(int_queue) == 3

    assert int_queue.dequeue() == 1

    assert int_queue.front() == 2
    assert int_queue.peek() == 2
    assert int_queue.is_empty() is False
    assert int_queue.is_full() is False
    assert int_queue.space() == 3
    assert len(int_queue) == 2
