def find_max(num):
    max = num[0]
    for i in num:
        if i > max:
            max = i
    return max


if __name__ == "__main__":
    a = find_max([1,3,5,3,5,6])
    print(a)