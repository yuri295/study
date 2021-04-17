N = int(input('자연수 입력:'))
while N <= 0:
    print(N, '은(는) 자연수가 아닙니다.')
    N = int(input('자연수 입력:'))
print(N, '의 모든 약수:', end=' ')
i = 1
while i <= N:
    if N % i == 0:
        print(i, end=' ')
    i += 1
