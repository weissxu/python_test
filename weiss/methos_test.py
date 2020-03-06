from functools import reduce


def power(x):
    return x * x


f = power
r = map(f, range(5))

for k in r:
    print(k)

print('===============')


def fn(x, y):
    return x * 10 + y


reduce_num = reduce(fn, range(5))
print('reduce: ', reduce_num)
