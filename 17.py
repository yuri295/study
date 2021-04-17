def isDivisor(m,n):
    if m % n == 0:
        return True
    else:
        return False

a = int(input('a= '))
i = 1
while i <= a:
    if isDivisor(a, i):
        print(i, end=' ')
    i += 1