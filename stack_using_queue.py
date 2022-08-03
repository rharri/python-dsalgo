"""This module implements a stack data structure using a queue
data structure.
"""
from typing import Generic, TypeVar

from circular_queue import Queue

T = TypeVar("T")


class StackUsingQueue(Generic[T]):
    """Represents a stack data structure.

    The underlying implementation uses a queue data structure.
    """

    def __init__(self, n: int = 10):
        """Initializes a new StackUsingQueue instance.

        Time: Θ(1), Space: Θ(N)
        """
        self._queue: Queue[T] = Queue(n)
        self._temp_queue: Queue[T] = Queue(n)
        self._max_size = 0

    def push(self, item: T) -> None:
        """Pushes the `item` onto the stack.

        Time: Θ(1), Space: Θ(1)

        :param item: The item to push onto the stack.
        """
        self._queue.enqueue(item)
        self._max_size += 1

    # Dequeuing from one queue into another queue (enqueue)
    # maintains the order of items
    def pop(self) -> T | None:
        """Removes the item at the top of the stack.

        Time: O(N), Space: Θ(1)

        :return: The removed item or None if the stack is empty.
        """
        if self._queue.is_empty():
            return None

        end_item: T | None = self._queue.end()

        # Take an item from the front of the 'real' queue and enqueue it
        # on the temporary queue. Do not enqueue the item that is
        # currently at the end of the 'real' queue.
        while not self._queue.is_empty():
            item = self._queue.front()
            if item and item != end_item:
                self._temp_queue.enqueue(item)
            self._queue.dequeue()

        # The queue should be empty
        assert self._queue.is_empty() is True

        # Enqueue the items from the temp queue on to the 'real' queue,
        # effectively putting back the items in their original order
        while not self._temp_queue.is_empty():
            item = self._temp_queue.front()
            if item:
                self._queue.enqueue(item)
            self._temp_queue.dequeue()

        # The temp queue should be empty
        assert self._temp_queue.is_empty() is True

        return end_item  # type: ignore

    def top(self) -> T | None:
        """Returns the item that is currently at the top of the stack.

        Time: Θ(1), Space: Θ(1)

        :return: The item at the top of the stack or None if the stack
        is empty.
        """
        if self._queue.is_empty():
            return None
        return self._queue.end()

    def peek(self) -> T | None:
        """Returns the item that is currently at the top of the stack.

        Time: Θ(1), Space: Θ(1)

        :return: The item at the top of the stack or None if the stack
        is empty.
        """
        return self.top()

    def empty(self) -> bool:
        """Returns True if the stack is empty, false otherwise.

        Time: Θ(1), Space: Θ(1)
        """
        return self._queue.is_empty()

    def is_full(self) -> bool:
        """Returns True if the stack is full, false otherwise.

        Time: Θ(1), Space: Θ(1)
        """
        return self._queue.is_full()

    def space(self) -> int:
        """Returns the maximum number of items that were held in the stack.

        Time: Θ(1), Space: Θ(1)
        """
        return self._max_size

    def __len__(self) -> int:
        """Returns the length of the stack.

        Time: Θ(1), Space: Θ(1)
        """
        return len(self._queue)


if __name__ == "__main__":
    int_stack: StackUsingQueue[int] = StackUsingQueue()
    assert int_stack.pop() is None
    assert int_stack.top() is None
    assert int_stack.empty() is True
    assert int_stack.space() == 0
    assert len(int_stack) == 0

    int_stack.push(1)
    int_stack.push(2)
    int_stack.push(3)

    assert int_stack.empty() is False
    assert int_stack.space() == 3
    assert len(int_stack) == 3

    assert int_stack.top() == 3
    assert int_stack.peek() == 3
    assert int_stack.pop() == 3
    assert int_stack.empty() is False
    assert int_stack.space() == 3
    assert len(int_stack) == 2
    assert int_stack.top() == 2
