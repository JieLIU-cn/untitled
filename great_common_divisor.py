#  两个整数的最大公约数等于其中较小的那个数和两数相除余数的最大公约数
def gcd(a, b):
    if a < b:
        a, b = b, a
    c = a % b
    if c == 0:
        return b
    else:
        return gcd(b, c)


def lcm(a, b):
    #  两个数的最小公倍数和最大公约数的积 = 两数乘积
    return a*b // gcd(a, b)


def three_gcd(a, b, c):
    return gcd(gcd(a, b), c)


def three_lcm(a, b, c):
    return lcm(lcm(a, b), c)

if __name__ == "__main__":
    print(gcd(765, 615))
    print(lcm(2, 4))
    print(three_gcd(34,5,24))
    print(three_lcm(342,34,3))
