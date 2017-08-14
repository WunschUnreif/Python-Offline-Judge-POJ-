n = int(input())
for i in range(n):
    m = int(input())
    t = 0
    while m != 1:
        m = m / 2 if m % 2 == 0 else 3 * m + 1
        t += 1
    print(t)
