"""This modules implements a queue data structure."""
from typing import Generic, TypeVar

T = TypeVar("T")


class Queue(Generic[T]):
    """Represents a queue data structure."""

    def __init__(self, n: int):
        """Initializes a new Queue instance with the provided size.

        This is a constant time operation.

        :param n: The size of the queue.
        """
        self._list: list[T] = []
        self.front_pointer: int = 0
        self.count: int = 0
        self.max_size: int = n

    def enqueue(self, item: T) -> bool:
        """Adds the provided `item` to the queue.

        Items are added to the back of the queue. This is a constant
        time operation.

        :param item: The item to add to the queue.
        :return: True if the operation succeeded, false otherwise.
        """
        if self.count == self.max_size:
            return False
        self._list.append(item)
        self.count += 1
        return True

    def dequeue(self) -> bool:
        """Removes the first item from the queue.

        Items are removed from the front of the queue. This is a
        constant time operation.

        :return: True if the operation succeeded, false otherwise.
        """
        if self.count == 0:
            return False
        self.front_pointer += 1
        self.count -= 1
        return True

    def front(self) -> None | T:
        """Returns the item from the front of the queue.

        The item is not removed from queue. This is a constant time
        operation.
        """
        if self.count == 0:
            return None
        return self._list[self.front_pointer]

    def end(self) -> None | T:
        """Returns the item from the end of the queue.

        The item is not removed from queue. This is a constant time
        operation.
        """
        if self.count == 0:
            return None
        return self._list[-1]

    def is_empty(self) -> bool:
        """Returns True if the queue is empty, False otherwise.

        This is a constant time operation.
        """
        return self.count == 0

    def is_full(self) -> bool:
        """Returns True if the queue is full, False otherwise.

        This is a constant time operation.
        """
        return self.count == self.max_size

    def __len__(self) -> int:
        """Returns the length of the queue.

        This is a constant time operation.
        """
        return self.count


if __name__ == "__main__":
    int_queue: Queue[int] = Queue(3)
    assert int_queue.dequeue() is False
    assert int_queue.front() is None
    assert int_queue.end() is None
    assert int_queue.is_empty() is True
    assert int_queue.is_full() is False
    assert len(int_queue) == 0

    int_queue.enqueue(1)
    int_queue.enqueue(2)
    int_queue.enqueue(3)

    assert int_queue.front() == 1
    assert int_queue.end() == 3
    assert int_queue.is_empty() is False
    assert int_queue.is_full() is True
    assert len(int_queue) == 3

    assert int_queue.dequeue() is True

    assert int_queue.front() == 2
    assert int_queue.end() == 3
    assert int_queue.is_empty() is False
    assert int_queue.is_full() is False
    assert len(int_queue) == 2

    assert int_queue.dequeue() is True
    assert int_queue.dequeue() is True

    assert int_queue.front() is None
    assert int_queue.end() is None
    assert int_queue.is_empty() is True
    assert int_queue.is_full() is False
    assert len(int_queue) == 0

    int_queue.enqueue(1)
    int_queue.enqueue(2)

    assert int_queue.front() == 1
    assert int_queue.end() == 2
    assert int_queue.is_empty() is False
    assert int_queue.is_full() is False
    assert len(int_queue) == 2
