import math


def main(*lst):
    def f(y, x):
        return 3 * ((45 * y) - (50 * y ** 2) - (52 * x ** 3))

    c, z = lst
    res = 0
    n = len(c)
    for i in range(n):
        res += f(z[math.ceil(i // 3)], c[n - 1 - i])
    return res

# print(f([-0.82, -0.62, -0.58, 0.83, -0.19, -0.49, 0.93], [0.29, -0.85, -0.97, -0.21, -0.52, 0.67, -0.38]))
