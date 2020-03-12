def merge_sort(sequence):
    if len(sequence) < 2:
        return sequence
    mid = int(len(sequence)//2)
    left = sequence[0:mid]
    right = sequence[mid:]
    return merge(merge_sort(left), merge_sort(right))


def merge(left, right):
    result = []
    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    while left:
        result.append(left.pop(0))

    while right:
        result.append(right.pop(0))

    return result


if __name__ == '__main__':
    sequence = [12,27,46,16,25,37,22,29,15,47,48,34]
    print(merge_sort(sequence))