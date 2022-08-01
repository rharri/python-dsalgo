"""This modules implements a stack data structure.

The provided implementation can grow dynamically and
does not require an initial size.

    Usage:

    >>> int_stack = Stack()
    >>> int_stack.push(1)
    >>> int_stack.push(2)
    >>> int_stack.top()
    2
    >>> int_stack.pop()
    2
    >>> int_stack.top()
    1
"""
from typing import Generic, TypeVar

T = TypeVar("T")


class Stack(Generic[T]):
    """Represents a stack data structure."""

    def __init__(self):
        """Initializes a new instance of Stack.

        This is a constant time operation.
        """
        self._list: list[T] = []
        self.top_index: int = 0
        self.size: int = 0
        self.max_size: int = 0

    def push(self, item: T):
        """Pushes the `item` onto the stack.

        This is a constant time operation.

        :param item: The item to push onto the stack.
        """
        if len(self._list) - 1 > self.top_index:
            self._list[self.top_index + 1] = item
            self.top_index += 1
        else:
            self._list.append(item)
            self.top_index = len(self._list) - 1
        self.size += 1

        if self.size > self.max_size:
            self.max_size = self.size

    def pop(self) -> T | None:
        """Removes the item at the top of the stack.

        This is a constant time operation.

        :return: The removed item or None if the stack is empty.
        """
        if self.size == 0:
            return None
        item = self._list[self.top_index]

        self.top_index -= 1
        self.size -= 1

        return item

    def top(self) -> T | None:
        """Returns the item that is currently at the top of the stack.

        This is a constant time operation.

        :return: The item at the top of the stack or None if the stack
        is empty.
        """
        if self.size == 0:
            return None
        return self._list[self.top_index]

    def empty(self) -> bool:
        """Returns True if the stack is empty, false otherwise.

        This is a constant time operation.
        """
        return self.size == 0

    def is_full(self) -> bool:
        """Returns True if the stack is full, false otherwise.

        This is a constant time operation.
        """
        return False

    def space(self) -> int:
        """Returns the maximum number of items that were held in the stack.

        This is a constant time operation.
        """
        return self.max_size

    def __len__(self) -> int:
        """Returns the length of the stack.

        This is a constant time operation.
        """
        return self.size


if __name__ == "__main__":
    int_stack: Stack[int] = Stack()
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
    assert int_stack.pop() == 3
    assert int_stack.empty() is False
    assert int_stack.space() == 3
    assert len(int_stack) == 2
    assert int_stack.top() == 2

    assert int_stack.pop() == 2
    assert int_stack.pop() == 1

    assert int_stack.pop() is None
    assert int_stack.top() is None
    assert int_stack.empty() is True
    assert int_stack.space() == 3
    assert len(int_stack) == 0

    int_stack.push(2)
    int_stack.push(3)

    assert int_stack.empty() is False
    assert int_stack.space() == 3
    assert len(int_stack) == 2

    assert int_stack.top() == 3

    int_stack.push(88)
    int_stack.push(1)
    int_stack.push(98)
    int_stack.pop()
    int_stack.pop()
    int_stack.push(45)
    int_stack.pop()
    assert int_stack.top() == 88
