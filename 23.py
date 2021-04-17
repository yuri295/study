def isPrime(a):
    i = 2
    while i <= a/2:
        if a % i == 0:
            return False
        i += 1
    return True
N = int(input('2이상의 자연수 입력: '))
while N < 2:
    print('2이상의 자연수를 입력해주세요.')
    N = int(input('2이상의 자연수 입력: '))
if isPrime(N):
    print(N, '은(는) 소수입니다.')
else:
    print(N, '은(는) 소수가 아닙니다.')