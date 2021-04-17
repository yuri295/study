N = int(input('N 입력: '))
while N <= 2:
    print('N은 2보다 큰 자연수여야 합니다.')
    N = int(input('N 입력: '))
a = 3
while a <= N:
    s = 0
    i = 1
    while i <= a/2:
        if a % i == 0:
            s += i
        i += 1
    if s == a:
        print(a, end=' ')
    a += 1

