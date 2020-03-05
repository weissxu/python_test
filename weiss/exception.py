try:
    print('try...')
    r = 10 / 0
    print('result: ', r)
except ZeroDivisionError as e:
    print('exception: ', e.args)
finally:
    print('finally..')
print('=============')

import logging

logging.basicConfig(level=logging.INFO)


def foo(s):
    try:
        n = int(s)
        return 10 / n
    except:
        logging.error('n=%s' % s)


def main():
    foo('0')


main()

exit()
