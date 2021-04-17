def isPerfect(m):
    i = 1
    s = 0
    while i <= m/2:
        if m % i == 0:
            s += i
        i += 1
    if s == m:
        return True
    else:
        return False

N = int(input('N= '))
for i in range(1, N+1):
    if isPerfect(i):
        print(i, end=' ')
