a = int(input('자연수 a 입력:'))
b = int(input('자연수 b 입력:'))
while a % b != 0:
    r = a % b
    a, b = b, r
print('최대공약수:', b)