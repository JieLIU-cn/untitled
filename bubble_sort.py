def bubble_sort(sequence):
    for i in range(0, len(sequence)-2):
        for j in range(i, len(sequence) - 1):
            if sequence[j] > sequence[j+1]:
                sequence[j], sequence[j+1] = sequence[j+1], sequence[j]
    return sequence


if __name__ == '__main__':
    sequence = [1,2,5,3,4]
    print(bubble_sort(sequence))

