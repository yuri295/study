a = int(input('자연수 a 입력:'))
b = int(input('자연수 b 입력:'))
i = 1
while i <= a and i <= b:
    if a % i == 0 and b % i == 0:
        gcd = i
    i += 1
print('최대공약수:', gcd)
