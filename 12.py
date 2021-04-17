a = int(input('자연수 a 입력:'))
b = int(input('자연수 b 입력:'))
if a > b:
    a, b = b, a
else:
    B = b
    while B % a != 0:
        B += b
    print('최소공배수:', B)