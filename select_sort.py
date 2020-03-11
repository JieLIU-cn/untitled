def select_sort(sequene):
    for i in range(0, len(sequene)-2):
        index_min = i
        for j in range(i+1, len(sequene)):
            if sequence[index_min] > sequence[j]:
                index_min = j
        sequene[index_min], sequene[i] = sequene[i], sequene[index_min]

    return sequene


if __name__ == '__main__':
    sequence = [5,4,3,2,1]
    print(select_sort(sequence))
