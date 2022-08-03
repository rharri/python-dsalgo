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

        Time: Θ(1), Space: Θ(1)
        """
        self._list: list[T] = []
        # The stack pointer always points to the 'top' item + 1
        self._stack_pointer: int = 0
        # How many items were appended to the list?
        self._max_size: int = 0

    def push(self, item: T):
        """Pushes the `item` onto the stack.

        Time: Θ(1), Space: Θ(1)

        :param item: The item to push onto the stack.
        """
        # Reuse the end of the list if the last item in the list was popped
        # The stack pointer will be less than the length of the list
        if self._stack_pointer < len(self._list):
            self._list[self._stack_pointer] = item
            self._stack_pointer += 1
        else:
            # Otherwise append to the end of the list
            self._list.append(item)
            self._max_size += 1
            self._stack_pointer += 1
            assert len(self) == len(self._list)

    def pop(self) -> T | None:
        """Removes the item at the top of the stack.

        Time: Θ(1), Space: Θ(1)

        :return: The removed item or None if the stack is empty.
        """
        if self.is_empty():
            return None
        self._stack_pointer -= 1
        return self._list[self._stack_pointer]

    def top(self) -> T | None:
        """Returns the item that is currently at the top of the stack.

        Time: Θ(1), Space: Θ(1)

        :return: The item at the top of the stack or None if the stack
        is empty.
        """
        if self.is_empty():
            return None
        return self._list[self._stack_pointer - 1]

    def is_empty(self) -> bool:
        """Returns True if the stack is empty, false otherwise.

        Time: Θ(1), Space: Θ(1)
        """
        return len(self) == 0

    def is_full(self) -> bool:
        """Returns True if the stack is full, false otherwise.

        Time: Θ(1), Space: Θ(1)
        """
        return False

    def space(self) -> int:
        """Returns the maximum number of items that were held in the stack.

        Time: Θ(1), Space: Θ(1)
        """
        return self._max_size

    def __len__(self) -> int:
        """Returns the length of the stack.

        Time: Θ(1), Space: Θ(1)
        """
        return self._stack_pointer

    def __repr__(self) -> str:
        return f"stack={self._list}"


if __name__ == "__main__":
    int_stack: Stack[int] = Stack()
    assert int_stack.pop() is None
    assert int_stack.top() is None
    assert int_stack.is_empty() is True
    assert int_stack.space() == 0
    assert len(int_stack) == 0

    int_stack.push(1)
    int_stack.push(2)
    int_stack.push(3)

    assert int_stack.is_empty() is False
    assert int_stack.space() == 3
    assert len(int_stack) == 3

    assert int_stack.top() == 3
    assert int_stack.pop() == 3
    assert int_stack.is_empty() is False
    assert int_stack.space() == 3
    assert len(int_stack) == 2
    assert int_stack.top() == 2

    assert int_stack.pop() == 2
    assert int_stack.pop() == 1

    assert int_stack.pop() is None
    assert int_stack.top() is None
    assert int_stack.is_empty() is True
    assert int_stack.space() == 3
    assert len(int_stack) == 0

    int_stack.push(2)
    int_stack.push(3)

    assert int_stack.is_empty() is False
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
