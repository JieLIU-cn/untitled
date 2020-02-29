import math

def find_prime(num):
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                print('{} is not prime number'.format(num))
                print(i, '*', num/i, '=', num)
                break

        print(num, "is prime number")

    else:
        print(num, "is not prime number")

def find_prime_2(num):


if __name__ == "__main__":
    num = int(input('please input a number'))
    find_prime(num)