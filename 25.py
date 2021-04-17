arr = []
N = int(input('정수 입력(종료 시는 999):'))
while N != 999:
    if arr.count(N) == 0:
        arr.append(N)
    N = int(input('정수 입력(종료 시는 999):'))
print(arr)