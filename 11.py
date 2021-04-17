a = int(input('자연수 a 입력:'))
b = int(input('자연수 b 입력:'))
A = a
B = b
while A != B:
    if A < B:
        A += a
    else:
        B += b
print('최소공배수:', A)