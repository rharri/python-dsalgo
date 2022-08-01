"""This module implements a stack data structure using a queue
data structure.
"""
from typing import Generic, TypeVar

from my_queue import Queue

T = TypeVar("T")


class StackUsingQueue(Generic[T]):
    """Represents a stack data structure.

    The underlying implementation uses a queue data structure.
    """

    def __init__(self, n: int = 10):
        """Initializes a new StackUsingQueue instance."""
        self.queue: Queue[T] = Queue(n)
        self.max_size = 0

    def push(self, item: T) -> None:
        """Pushes the `item` onto the stack.

        This is a constant time operation.

        :param item: The item to push onto the stack.
        """
        self.queue.enqueue(item)
        self.max_size += 1

    # Time: Theta(n), Space: Theta(n)
    def pop(self) -> T | None:
        """Removes the item at the top of the stack.

        This is a Theta(n) operation.

        :return: The removed item or None if the stack is empty.
        """
        if self.queue.is_empty():
            return None

        end_item: T | None = self.queue.end()

        put_back_items: list[T] = []
        while True:
            front_item: T | None = self.queue.front()
            if front_item not in {None, end_item}:
                put_back_items.append(front_item)  # type: ignore
            if self.queue.dequeue() is False:
                break

        for item in put_back_items:
            self.queue.enqueue(item)

        return end_item  # type: ignore

    def top(self) -> T | None:
        """Returns the item that is currently at the top of the stack.

        This is a constant time operation.

        :return: The item at the top of the stack or None if the stack
        is empty.
        """
        if self.queue.is_empty():
            return None
        return self.queue.end()

    def peek(self) -> T | None:
        """Returns the item that is currently at the top of the stack.

        This is a constant time operation.

        :return: The item at the top of the stack or None if the stack
        is empty.
        """
        return self.top()

    def empty(self) -> bool:
        """Returns True if the stack is empty, false otherwise.

        This is a constant time operation.
        """
        return self.queue.is_empty()

    def is_full(self) -> bool:
        """Returns True if the stack is full, false otherwise.

        This is a constant time operation.
        """
        return self.queue.is_full()

    def space(self) -> int:
        """Returns the maximum number of items that were held in the stack.

        This is a constant time operation.
        """
        return self.max_size

    def __len__(self) -> int:
        """Returns the length of the stack.

        This is a constant time operation.
        """
        return len(self.queue)


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
