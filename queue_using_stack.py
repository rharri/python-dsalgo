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
        self._stack: Stack[T] = Stack()
        self._temp_stack: Stack[T] = Stack()
        self._front_item = None

    def enqueue(self, item: T) -> None:
        """Adds the provided `item` to the queue.

        Items are added to the back of the queue. This is a constant
        time operation.

        :param item: The item to add to the queue.
        """
        self._stack.push(item)

        if len(self._stack) == 1:
            self._front_item = item

    def dequeue(self) -> T | None:
        """Removes the first item from the queue.

        Items are removed from the front of the queue.
        Time: O(N), Space: Θ(1)

        :return: The removed item.
        """
        if self._stack.is_empty():
            return None

        top_item: T | None = None

        while not self._stack.is_empty():
            item = self._stack.pop()
            if item and len(self._stack) >= 1:
                self._temp_stack.push(item)
            else:
                top_item = item

        assert self._stack.is_empty() is True

        self._front_item = self._temp_stack.top()
        while not self._temp_stack.is_empty():
            item = self._temp_stack.pop()
            if item:
                self._stack.push(item)

        assert self._temp_stack.is_empty() is True

        return top_item

    def front(self) -> T | None:
        """Returns the item from the front of the queue.

        The item is not removed from queue. Time: Θ(1), Space: Θ(1)
        """
        return self._front_item

    def peek(self) -> T | None:
        """Returns the item from the front of the queue.

        The item is not removed from queue. Time: Θ(1), Space: Θ(1)
        """
        return self.front()

    def is_empty(self) -> bool:
        """Returns True if the queue is empty, False otherwise.

        Time: Θ(1), Space: Θ(1)
        """
        return self._stack.is_empty()

    def is_full(self) -> bool:
        """Returns True if the queue is full, False otherwise.

        Time: Θ(1), Space: Θ(1)
        """
        return self._stack.is_full()

    def space(self) -> int:
        """Returns the maximum number of items that were held in the queue.

        Time: Θ(1), Space: Θ(1)
        """
        return self._stack.space()

    def __len__(self) -> int:
        """Returns the length of the queue.

        Time: Θ(1), Space: Θ(1)
        """
        return len(self._stack)


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
