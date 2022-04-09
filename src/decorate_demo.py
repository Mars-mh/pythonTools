import functools
import time


def clock(func):
    def clocked(*args):
        t0 = time.perf_counter()
        res = func(*args)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)

        print('{} - {}({}) : {}'.format(elapsed, name, arg_str, res))
        return res
    return clocked


@functools.lru_cache()
@clock
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-2) + fibonacci(n-1)


if __name__ == '__main__':
    print('The final res is {}'.format(fibonacci(6)))
