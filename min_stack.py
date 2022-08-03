"""This module implements a MinStack data structure."""
from stack import Stack


class MinStack:
    """Represents a MinStack.

    The MinStack provides standard stack operations in addition to
    retrieving the minimum item in constant time.
    """

    def __init__(self):
        """Initializes a new MinStack instance.

        This is a constant time operation.
        """
        self._stack: Stack[int] = Stack()
        self._min_stack: Stack[int] = Stack()

    def push(self, item: int) -> None:
        """Pushes the `item` onto the stack.

        This is a constant time operation.

        :param item: The item to push onto the stack.
        """
        self._stack.push(item)

        if self._min_stack.is_empty():
            self._min_stack.push(item)
        else:
            min_item = self._min_stack.top()
            if item <= min_item:  # type: ignore
                self._min_stack.push(item)

    def pop(self) -> int | None:
        """Removes the top item from the stack.

        This is a constant time operation.

        :return: The removed item or None if the stack is empty.
        """
        top_item: int | None = self._stack.top()
        if top_item == self._min_stack.top():
            self._min_stack.pop()
        return self._stack.pop()

    def top(self) -> int | None:
        """Returns the item at the top of the stack.

        This is a constant time operation.

        The item is not removed from the stack.
        """
        return self._stack.top()

    def min(self) -> int | None:
        """Returns the minimum item from the stack.

        This is a constant time operation.

        The minimum item is not removed from the stack.
        """
        return self._min_stack.top()


if __name__ == "__main__":
    min_stack = MinStack()
    min_stack.push(2)

    assert min_stack.min() == 2
    min_stack.push(15)
    assert min_stack.min() == 2
    min_stack.push(1)
    assert min_stack.min() == 1
    min_stack.push(-50)
    assert min_stack.min() == -50
    min_stack.push(1000)
    assert min_stack.min() == -50
    min_stack.pop()
    assert min_stack.min() == -50
    min_stack.pop()
    assert min_stack.min() == 1
