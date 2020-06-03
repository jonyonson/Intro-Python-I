import sys

arg = sys.argv[1]


def is_prime(n):
    if int(n) <= 1:
        return False
    for i in range(2, int(n)):
        if int(n) % i == 0:
            return False
    return True


if is_prime(arg):
    print(f'{arg} is a prime number.')
else:
    print(f'{arg} is not a prime number.')
