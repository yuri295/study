N = int(input('자연수 N='))
i = 1
s = 0
while i <= N/2:
    if N % i == 0:
        s += i
    i += 1
if s == N:
    print(N, '은(는) 완전수입니다.')
else:
    print(N, '은(는) 완전수가 아닙니다.')