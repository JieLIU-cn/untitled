a = int(input('Please input a number'))

if a <= 1:
    print("Wrong number, number should be lager than 0")

num = 0
lst = [a]

while a != 1:
    if a % 2 == 1:
        a = 3*a + 1
    else:
        a = int(a / 2)
    lst.append(a)
    num += 1

print(lst, num)