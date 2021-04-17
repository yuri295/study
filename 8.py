while True:
    a = int(input('a='))
    b = int(input('b='))
    if a < 0 and b > 0 or a > 0 and b < 0:
        print('음수')
    elif a == 0 or b == 0:
        print('입력오류')
    else:
        print('양수')