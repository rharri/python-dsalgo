from linked_list import LinkedList, Node


class IntList(LinkedList):
    # Time: O(N), Space: O(N)
    def __init__(self, n: int | None) -> None:
        super().__init__(None)
        if n or n == 0:
            self._init_from_n(n)

    # Time: Θ(N), Space: Θ(N)
    def _init_from_n(self, n: int) -> None:
        digits: list[int] = self._get_digits(n)
        self._init_from_list(digits)

    # Time: Θ(N), Space: Θ(N)
    def _get_digits(self, n: int) -> list[int]:
        if n == 0:
            return [0]
        digits: list[int] = []
        total: int = 0
        place_value: int = 10
        while total != n:
            digit = n % place_value // (place_value // 10)
            total += digit * (place_value // 10)
            place_value *= 10
            digits.append(digit)
        return digits

    # Time: Θ(N), Space: O(N)
    def get_value(self) -> int:
        forward_cursor: Node[int] | None = self.head()
        value_from_list: int = 0
        place_value: int = 1
        while forward_cursor:
            number: int = forward_cursor.value
            value_from_list += number * place_value
            place_value *= 10
            forward_cursor = forward_cursor.next
        return value_from_list

    # Time: Θ(N), Space: O(N)
    def __add__(self, other: "IntList") -> "IntList":
        addend_column_1: Node[int] | None = self.head()
        addend_column_2: Node[int] | None = other.head()

        # Keep the longer number on 'top'
        if len(self) < len(other):
            addend_column_1 = other.head()
            addend_column_2 = self.head()

        # first addend
        # second addend
        # -------------
        # sum

        #  129
        # + 12
        # -----
        #  141

        # 9 -> 2 -> 1 -> NONE
        # 2 -> 1 -> NONE
        # -----------
        # 1 -> 4 -> 1 -> NONE

        carry: int = 0
        sum: IntList = IntList(None)
        while addend_column_1:
            column_value_1 = addend_column_1.value
            column_value_2 = addend_column_2.value if addend_column_2 else 0

            column_sum = column_value_1 + column_value_2 + carry
            carry = 1 if column_sum >= 10 else 0

            if column_sum >= 10:
                sum.append(column_sum - 10)
            else:
                sum.append(column_sum)

            # Ensure the carry digit is appended to sum list
            # if we are at the end of first addend
            # 9 -> 9 -> NONE
            # 9 -> NONE
            # --------------
            # 8 -> 0 -> 1 - NONE
            if carry and not addend_column_1.next:
                sum.append(carry)

            # Move to the next digit
            addend_column_1 = addend_column_1.next
            if addend_column_2:
                addend_column_2 = addend_column_2.next
        return sum


if __name__ == "__main__":
    int_list: IntList = IntList(1995)
    print(int_list)

    print(f"value={int_list.get_value()}")

    another_int_list: IntList = IntList(2022)
    print(another_int_list)

    sum = int_list + another_int_list
    print(sum)
    print(f"1995 + 2022 = {sum.get_value()}")

    a = IntList(9999999)
    b = IntList(9999)
    c = a + b
    print(f"a={a}, value={a.get_value()}")
    print(f"b={b}, value={b.get_value()}")
    print(f"c={c}, value={c.get_value()}")
