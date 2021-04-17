import time
N = int(input('자연수 N 입력:'))
s = 0
start = time.time()
for i in range(1, N**2+1):
    s += i
print('합계:', s)
end = time.time() - start
print('실행시간:', end)