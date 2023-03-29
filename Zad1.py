import math


def main(x, y):
    value = math.sqrt(87 * (x ** 3) - (34 * y))
    value1 = 82 * (math.cos(1 + x ** 3) ** 3)
    value2 = ((1 - (y ** 2 / 2) - y ** 3) ** 6)
    value3 = value + value1 + value2
    return value3
