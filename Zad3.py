def main(a, n, x):

    f = 0
    for c in range(1, n + 1):
        for j in range(1, a + 1):
            f += (87 * pow(j, 2) + 34 * pow(x, 5) + 67 *
                  (32 - 89 * pow(c, 2) - 44 * pow(j, 3)) ** 6)
    return f





a = int(input())
n = int(input())
x = float(input())
print(main(a, n, x))


