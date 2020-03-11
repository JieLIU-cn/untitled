def shell_sort(sequence):
    # nothing good
    gap = len(sequence)
    while gap > 1:
        gap = gap//2
        for i in range(gap, len(sequence)):
            for j in range(i % gap, i, gap):
                if sequence[i] < sequence[j]:
                    sequence[i], sequence[j] = sequence[j], sequence[i]
    return sequence


if __name__ == '__main__':
    shell_sort([9,8,7,6,5,4,3,2,1])