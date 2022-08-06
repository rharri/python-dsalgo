from typing import Generic, TypeVar

T = TypeVar("T")


class Node(Generic[T]):
    def __init__(self, value: T, next: "Node" | None) -> None:
        self.value = value
        self.next = next

    @staticmethod
    def empty() -> "Node":
        return Node(None, next=None)


class LinkedList(Generic[T]):
    def __init__(self, x: list[T] | None = None) -> None:
        self._head: Node[T] | None = None
        self._tail: Node[T] | None = None
        self._size: int = 0

        if x:
            self._init_from_list(x)

    def _init_from_list(self, x: list[T]) -> None:
        if not x:
            raise ValueError("non-empty list required")

        # Replace the current linked list with the source list
        self._head = None
        self._tail = None

        # Iterate every element in the list, create a new node,
        # and join it with its predecessor
        forward_cursor = Node.empty()
        for elem in x:
            new_node: Node = Node(elem, next=None)
            if not self._head:
                # _head is None during the first iteration
                self._head = new_node
                forward_cursor = self._head
                continue
            # Connect the current node to the new node
            forward_cursor.next = new_node
            # The forward cursor only moves forward :)
            forward_cursor = new_node
            self._size += 1

        # The last new_node will be last element in the source list
        self._tail = new_node

    def prepend(self, value: T) -> None:
        new_head_node = Node(value, next=self._head)

        if self.is_empty():
            self._head = new_head_node
            self._tail = new_head_node
        else:
            self._head = new_head_node
        self._size += 1

    def append(self, value: T) -> None:
        new_tail_node = Node(value, next=None)

        if self.is_empty():
            # _head and _tail are None
            self._head = new_tail_node
            self._tail = new_tail_node
        else:
            # We should have a _tail or something is wrong
            assert self._tail
            # Connect the previous _tail node to the new tail node
            self._tail.next = new_tail_node
            self._tail = new_tail_node
        self._size += 1

    def head(self) -> Node | None:
        return self._head

    def tail(self) -> Node | None:
        return self._tail

    def delete(self, value) -> bool:
        if self.is_empty():
            return False

        forward_cursor: Node[T] | None = self.head()
        # List is not empty, we should have a _head
        assert forward_cursor

        if forward_cursor.value == value:
            return self.delete_head()

        tail_node: Node[T] | None = self.tail()
        # List is not empty, we should have a _tail
        assert tail_node

        if tail_node.value == value:
            return self.delete_tail()

        # Handle in-between node
        previous_node = Node.empty()
        while forward_cursor:
            if forward_cursor.value == value:
                # Remove the target node from the list
                previous_node.next = forward_cursor.next
                self._size -= 1
                return True
            previous_node = forward_cursor
            forward_cursor = forward_cursor.next
        return False

    def is_empty(self) -> int:
        return len(self) == 0

    def delete_head(self) -> bool:
        if not self._head:
            return False

        # We only have one node
        if self._head == self._tail:
            self._head = None
            self._tail = None
            self._size -= 1
            return True

        self._head = self._head.next
        self._size -= 1
        return True

    def delete_tail(self) -> bool:
        if not self._tail:
            return False

        # We only have one node
        if self._head == self._tail:
            self._head = None
            self._tail = None
            self._size -= 1
            return True

        # Delete the _tail node if we have more than one node
        previous_node = Node.empty()
        forward_cursor: Node[T] | None = self.head()
        while forward_cursor:
            # If the next node is None, our cursor is on the _tail node
            if not forward_cursor.next:
                # Set the next pointer on the node that precedes the
                # _tail node to None, deleting the _tail
                previous_node.next = None
                # Reset the _tail pointer
                self._tail = previous_node
                self._size -= 1
                return True
            previous_node = forward_cursor
            forward_cursor = forward_cursor.next
        return False

    def reverse(self) -> None:
        # Change each node's next pointer to point to their predecessor
        # 1 -> 2 -> 3 -> None
        # 1 -> None 2 -> 3 -> None
        # 2 -> 1 -> None 3 -> None
        # 3 -> 2 -> 1 -> None
        previous_node = None
        forward_cursor: Node[T] | None = self.head()
        while forward_cursor:
            if not previous_node:
                # Set the _head node to the _tail node
                self._tail = forward_cursor
            # Get a reference to the next node
            next_node: Node[T] | None = forward_cursor.next
            # Set 'this' node's next pointer to the previous node
            # Flip the relationship between predecessor node and 'this' node
            forward_cursor.next = previous_node
            # Keep a reference to 'this' node
            previous_node = forward_cursor
            # Move to the next node
            forward_cursor = next_node
        # At the end of the loop, previous_node will be the former _tail node,
        # which should now be the _head
        self._head = previous_node

    def mid_point(self) -> Node | None:
        if self.is_empty():
            return None

        slow_cursor: Node[T] | None = self.head()
        assert slow_cursor

        fast_cursor: Node[T] | None = slow_cursor.next

        # fast_cursor moves at 2x where x is the position of the slow_cursor
        # When fast_cursor reaches the end of the list, slow_cursor
        # will be at the mid point of the list
        while slow_cursor:
            if not fast_cursor or fast_cursor == self.tail():
                return slow_cursor
            slow_cursor = slow_cursor.next
            fast_cursor = fast_cursor.next.next  # type: ignore
        return None

    def __getitem__(self, index: int) -> Node | None:
        if index < 0 or index > len(self) - 1:
            return None
        if index == 0:
            return self.head()

        position = 0
        forward_cursor = self.head()
        while forward_cursor:
            if position == index:
                return forward_cursor
            forward_cursor = forward_cursor.next
            position += 1
        return None

    def __contains__(self, value) -> bool:
        forward_cursor: Node[T] | None = self.head()
        while forward_cursor:
            if forward_cursor.value == value:
                return True
            forward_cursor = forward_cursor.next
        return False

    def __len__(self) -> int:
        return self._size

    def __str__(self) -> str:
        forward_cursor: Node[T] | None = self.head()
        string_values: list[str] = []
        while forward_cursor:
            string_values.append(str(forward_cursor.value))
            forward_cursor = forward_cursor.next
        string_values.append(str(None))
        return "->".join(string_values)
