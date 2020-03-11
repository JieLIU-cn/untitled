def insertion_sort(sequence):
    for i in range(1, len(sequence)):
        j = i
        while sequence[j] < sequence[j-1] and j > 0:
            sequence[j-1], sequence[j] = sequence[j], sequence[j-1]
            j -= 1

    return sequence


if __name__ == '__main__':
    sequence = [5,4,6,3,1]
    print(insertion_sort(sequence))