def gcd(m, n):
    i = 1
    while i <= m and i <= n:
        if m % i == 0 and n % i == 0:
            g = i
        i += 1
    return g

a = int(input('a='))   
b = int(input('b='))
print('최대공약수:', gcd(a, b))

