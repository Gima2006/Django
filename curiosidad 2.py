def find_remainder(dividend: int, divisor: int) -> int:
    # your code here
    return dividend - sum([divisor]*divisor)


print(find_remainder(6, 3))

assert find_remainder(10, 3) == 1