n = int(input())

for i in range(n):
    m = int(input())
    if m == 1:
        print("NO")
        continue
    prime = True
    for x in range(2, m):
        if x * x > m:
            break
        if m % x == 0:
            prime = False
            break
    if prime:
        print("YES")
    else:
        print("NO")
