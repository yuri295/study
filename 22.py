def sum_avg(x, y, z):
    global d
    d = x+y+z
    global e
    e = (x+y+z)/3
a = int(input('a='))
b = int(input('b='))
c = int(input('c='))
sum_avg(a, b, c)
print('합:', d)
print('평균:', e)
