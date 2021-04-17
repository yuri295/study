def isPrime(a):
    i = 2
    while i <= a/2:
        if a % i == 0:
            return False
        i += 1
    return True

N = int(input('N='))
while N < 2:
    print(N, '은(는) 2이상의 자연수가 아닙니다.')
    N = int(input('N='))
for i in range(1, N+1):
    if isPrime(i):
        print(i, end=' ')
