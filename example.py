# coding=utf-8
import time
import sudoku


def time_couter(f):
    def decorator(*args, **kwargs):
        a = time.time()
        r = f(*args, **kwargs)
        elap = (time.time() - a) * 1000
        print(f'Elapse time {elap:.2f}ms')
        return r
    return decorator


def print_map(m):
    n = len(m)
    for row in m:
        _r = ' | '.join(map(str, row))
        print(_r)
        print('-'*n*4)


if __name__ == '__main__':
    size = 3
    print_map(time_couter(sudoku.randomize_algorithm)(size))
    print_map(time_couter(sudoku.backtrack_algorithm)(size))
