"""This modules implements a queue data structure.

The implementation uses circular buffering.

See: https://en.wikipedia.org/wiki/Circular_buffer
"""
from typing import Generic, TypeVar

T = TypeVar("T")


class Queue(Generic[T]):
    """Represents a queue data structure.

    The implementation uses circular buffering.
    """

    def __init__(self, size: int = 10):
        """Initializes a new Queue instance with the provided size.

        Time: Θ(1), Space: Θ(N)

        :param size: The size of the queue.
        """
        self._list: list[T | None] = [None] * size
        self._head: int = 0
        self._tail: int = 0
        self._count: int = 0
        self._capacity: int = size

    def enqueue(self, item: T) -> bool:
        """Adds the provided `item` to the queue.

        Items are added to the back of the queue.
        Time: Θ(1), Space: Θ(1)

        :param item: The item to add to the queue.
        :return: True if the operation succeeded, false otherwise.
        """
        if self.is_full():
            return False

        if self._tail == self._capacity:
            self._tail = 0

        self._list[self._tail] = item
        self._tail += 1
        self._count += 1

        return True

    def dequeue(self) -> bool:
        """Removes the first item from the queue.

        Items are removed from the front of the queue.
        Time: Θ(1), Space: Θ(1)

        :return: True if the operation succeeded, false otherwise.
        """
        if self.is_empty():
            return False

        self._head += 1
        self._count -= 1

        if self._head == self._capacity:
            self._head = 0

        return True

    def front(self) -> None | T:
        """Returns the item from the front of the queue.

        The item is not removed from queue. Time: Θ(1), Space: Θ(1)
        """
        if self.is_empty():
            return None
        return self._list[self._head]

    def end(self) -> None | T:
        """Returns the item from the end of the queue.

        The item is not removed from queue. Time: Θ(1), Space: Θ(1)
        """
        if self.is_empty():
            return None
        return self._list[self._tail - 1]

    def is_empty(self) -> bool:
        """Returns True if the queue is empty, False otherwise.

        Time: Θ(1), Space: Θ(1)
        """
        return self._count == 0

    def is_full(self) -> bool:
        """Returns True if the queue is full, False otherwise.

        Time: Θ(1), Space: Θ(1)
        """
        return len(self) == self._capacity

    def __len__(self) -> int:
        """Returns the length of the queue.

        Time: Θ(1), Space: Θ(1)
        """
        return self._count

    def __repr__(self):
        return f"queue={self._list}, head={self._head}, tail={self._tail}"


if __name__ == "__main__":
    # TEST CASE #1
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

    int_queue.enqueue(4)
    int_queue.enqueue(5)

    assert int_queue.front() == 4
    assert int_queue.end() == 5
    assert int_queue.is_empty() is False
    assert int_queue.is_full() is False
    assert len(int_queue) == 2

    assert int_queue.dequeue() is True

    assert int_queue.front() == 5
    assert int_queue.end() == 5
    assert int_queue.is_full() is False
    assert len(int_queue) == 1

    print(int_queue)

    # TEST CASE #2
    int_queue = Queue(6)
    int_queue.enqueue(14)
    assert int_queue.end() == 14
    assert int_queue.front() == 14

    int_queue.enqueue(22)
    assert int_queue.end() == 22
    assert int_queue.front() == 14

    int_queue.enqueue(13)
    assert int_queue.end() == 13
    assert int_queue.front() == 14

    int_queue.enqueue(-6)
    assert int_queue.end() == -6
    assert int_queue.front() == 14

    int_queue.dequeue()
    assert int_queue.end() == -6
    assert int_queue.front() == 22

    int_queue.dequeue()
    assert int_queue.end() == -6
    assert int_queue.front() == 13

    int_queue.enqueue(9)
    assert int_queue.end() == 9
    assert int_queue.front() == 13

    int_queue.enqueue(20)
    assert int_queue.end() == 20
    assert int_queue.front() == 13

    int_queue.enqueue(5)
    assert int_queue.end() == 5
    assert int_queue.front() == 13

    print(int_queue)

    # TEST CASE #3
    int_queue = Queue(3)
    int_queue.enqueue(1)
    int_queue.enqueue(2)
    int_queue.enqueue(3)
    int_queue.dequeue()
    int_queue.dequeue()
    int_queue.enqueue(4)

    print(int_queue)
