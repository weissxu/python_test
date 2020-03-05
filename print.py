sum = 0
for i in range(5):
    sum += i
    print(sum)

print('==============')

sum = 0
index = 5
while index > 0:
    sum += index
    index = index - 1

print(sum)

print('==============')


def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


print(power(5))

print('==============')


def add_end(L):
    if L is None:
        L = []
    L.append('END')
    return L


print(add_end(['hello']))

print('==============')


def calc(*numbers):
    sum = 0
    for num in numbers:
        sum += num

    return sum


# print(calc([1,2,3]))
# print(calc((1,2,3)))
print(calc(1, 2, 3))

print('==============')


def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)


print(f1(1, 2))
print(f1(1, 2, c=3))
print(f1(1, 2, 3, 'a', 'b'))
print(f1(1, 2, 3, 'a', 'b', x=99))

# 循环遍历
print('==============')
array = []
index = 0
while index < 100:
    index += 2
    array.append(index)
print(array)

print('==============')
L = ['1', '2', '3', '4', '5', '6']
print(L[0])
print(L[1])
print(L[2])

print(L[0:2])
print(L[2:])
print(L[-2:])

print('==============')
L = list(range(5, 10))
print(L)

print('==============')
# from collections import ABCs
import collections

isinstance('abc', collections.Iterable)

for i, value in enumerate(['A', 'b', 'c']):
    print(i, value)

print('==================')
print([x * x for x in range(1, 11)])
print([x * x for x in range(1, 11) if x % 2 == 0])
print([m + n for m in 'ABC' for n in 'XYZ'])

print('===================')
import os

print([d for d in os.listdir('.')])

print('===================')
d = {'x': 'A', 'y': 'B', 'z': 'C'}
for k, v in d.items():
    print(k, v)

print([k + '=' + v for k, v in d.items()])

print('===================')
g = (x * x for x in range(5))

for x in g:
    print(x)

print('===================')
from collections import Iterable
from collections import Iterator

print(isinstance([],Iterable))
print(isinstance({},Iterable))
print(isinstance('abc',Iterable))
print(isinstance('abc',Iterable))
print(isinstance((x for x in range(10)),Iterator))


print('===================')
def f(x):
    return x * x

r=map(f,[1,2,3,4])
print(list(r))

print('===================')
def createCounter():
    def counter():
        return 1
    return counter
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')




print('====================')
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
    print('2015-3-25')

now()


exit()
