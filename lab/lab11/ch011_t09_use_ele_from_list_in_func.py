from typing import List

def double_first(n: List[int]):
    n[0] = n[0] * 2

numbers = [1, 2, 3, 4]
double_first(numbers)
print(numbers)
