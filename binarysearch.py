def binarysearch(sorted_sequence, target):
    left = 0
    right = len(sorted_sequence) - 1
    while left < right:
        midpoint = (left + right) // 2
        if sorted_sequence[midpoint] == target:
            return midpoint
        elif sorted_sequence[midpoint] > target:
            right = midpoint - 1
        elif sorted_sequence[midpoint] < target:
            left = midpoint + 1
    return None  # 循环到最后也没匹配


if __name__ == "__main__":
    sequence = [1,2,3,4,5,6,7,8,9,10]
    target = 6
    print(binarysearch(sequence, target))
