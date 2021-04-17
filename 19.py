def lcm(m, n):
    if m > n:
        m, n = n, m
    N = n
    while N % m != 0:
        N += n
    return N

a = int(input('a= '))
b = int(input('b= '))
print('최소공배수: ', lcm(a, b))
