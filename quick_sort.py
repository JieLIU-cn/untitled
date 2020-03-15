def quick_sort(sequence):
    def recursive(begin, end):
        if begin > end:
            return
        left, right = begin, end
        pivot = sequence[left]
        while left < right:
            while left < right and sequence[right] > pivot:  # 因为是以left作为pivot，因此要把right侧分析放到前面，这样才能left = right = 比pivot小的值
                right -= 1
            while left < right and sequence[left] <= pivot:
                left += 1
            sequence[left], sequence[right] = sequence[right], sequence[left]
        sequence[left], sequence[begin] = pivot, sequence[left]  # 将pivot放到中间位置，之前对于left的方法，pivot一直处于begin的位置
        recursive(begin, left-1)
        recursive(right+1, end)

    recursive(0, len(sequence)-1)
    return sequence


if __name__ == '__main__':
    sequence = [3,5,2,6,8,2]
    print(quick_sort(sequence))
