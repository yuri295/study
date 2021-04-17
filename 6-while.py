N = int(input('N:'))
M = int(input('홀수/짝수 선택(1:홀수,2:짝수):'))
i = 1
if M == 1:
    while i <= N:
        if i % 2 == 1:
            print(i, end=' ')
        i += 1
elif M == 2:
    while i <= N:
        if i % 2 == 0:
            print(i, end=' ')
        i += 1
else:
    print('입력오류')