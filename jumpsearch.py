import math


def jumpsearch(sequence, target):
    n = len(sequence)
    step = int(math.sqrt(n))
    i = 0
    if target < sequence[0] or target > sequence[n-1]:
        return None
    while sequence[i] < target:
        i += step
    j = i - step
    while sequence[j] < target:
        j += 1
    if sequence[j] == target:
        return j
    else:
        return None