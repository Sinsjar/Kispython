import math


def main(n):
    if(n == 0):
        return -0.97
    elif(n == 1):
        return 0.21
    elif(n >= 2):
        return (main(n - 1) / 24 + 1) ** 3 + math.ceil(main(n - 2) + 1)


n = int(input())
print(main(n))
