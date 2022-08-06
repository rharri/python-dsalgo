from linked_list import LinkedList


class IntList(LinkedList):
    def __init__(self, n: int | None) -> None:
        super().__init__(None)
        if n or n == 0:
            self._init_from_n(n)

    def _init_from_n(self, n: int) -> None:
        digits: list[int] = self._get_digits(n)
        self._init_from_list(digits)

    def _get_digits(self, n: int) -> list[int]:
        if n == 0:
            return [0]
        digits = []
        total, place_value = 0, 10
        while total != n:
            digit = n % place_value // (place_value // 10)
            total += digit * (place_value // 10)
            place_value *= 10
            digits.append(digit)
        return digits

    def get_value(self) -> int:
        forward_cursor = self.head()
        value_from_list, place_value = 0, 1
        while forward_cursor:
            number = forward_cursor._value
            value_from_list += number * place_value
            place_value *= 10
            forward_cursor = forward_cursor._next
        return value_from_list

    def __add__(self, other: "IntList") -> "IntList":
        # Keep the longer number on 'top'
        if len(self) < len(other):
            first_addend, second_addend = other.head(), self.head()
        else:
            first_addend, second_addend = self.head(), other.head()

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

        carry = 0
        sum = IntList(None)
        while first_addend:
            first_addend_value = first_addend._value
            second_addend_value = 0
            if second_addend:
                second_addend_value = second_addend._value

            itermediate_sum = first_addend_value + second_addend_value + carry

            if itermediate_sum >= 10:
                sum.append(itermediate_sum - 10)
                carry = 1
            else:
                sum.append(itermediate_sum)
                carry = 0

            # Ensure the carry digit is appended to sum list
            # if we are at the end of first addend
            # 9 -> 9 -> NONE
            # 9 -> NONE
            # --------------
            # 8 -> 0 -> 1 - NONE
            if carry and not first_addend._next:
                sum.append(carry)

            # Move to the next digit
            first_addend = first_addend._next
            if second_addend:
                second_addend = second_addend._next
        return sum
