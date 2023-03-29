import math


def main(y):
    if(y < 44):
        return pow(y, 5)
    elif(44 <= y < 138):
        return pow(y, 6) - 1 - (pow((70 - pow(y, 2) - y), 3) / 49)
    elif(138 <= y < 237):
        a = pow((5 * pow(y, 2) + 1 + 65 * (pow(y, 3))), 2)
        return ((math.ceil(pow(y, 3))) / 53) + 26 * a
    elif(y >= 237):
        return 87 * pow(y, 2) + 34 * pow(y, 5) + 67 * \
               (32 - 89 * pow(y, 2) - 44 * pow(y, 3)) ** 6


y = int(input())

print(main(y))
