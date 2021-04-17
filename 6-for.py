N = int(input('N:'))
M = int(input('홀수/짝수 선택(1:홀수,2:짝수):'))
if M == 1:
    for i in range(1, N + 1):
        if i % 2 == 1:
            print(i, end=' ')
elif M == 2:
    for i in range(1, N + 1):
        if i % 2 == 0:
            print(i, end=' ')
else:
    print('입력 오류')
